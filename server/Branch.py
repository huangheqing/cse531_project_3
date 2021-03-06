import grpc
import protos.bank_system_pb2
import protos.bank_system_pb2_grpc

from utils.Operations import QUERY, DEPOSIT, WITHDRAW
from utils.constant import PORT

SUCCESS = 'success'
FAILURE = 'failure'
DEPOSIT_REQUEST = 'deposit_request'
DEPOSIT_EXECUTE = 'deposit_execute'
DEPOSIT_RESPONSE = 'deposit_response'
DEPOSIT_B_REQUEST = 'deposit_broadcast_request'
DEPOSIT_B_EXECUTE = 'deposit_broadcast_execute'
DEPOSIT_B_RESPONSE = 'deposit_broadcast_response'
WITHDRAW_REQUEST = 'withdraw_request'
WITHDRAW_EXECUTE = 'withdraw_execute'
WITHDRAW_RESPONSE = 'withdraw_response'
WITHDRAW_B_REQUEST = 'withdraw_broadcast_request'
WITHDRAW_B_EXECUTE = 'withdraw_broadcast_execute'
WITHDRAW_B_RESPONSE = 'withdraw_broadcast_response'


class Branch(protos.bank_system_pb2_grpc.BranchServiceServicer):

    def __init__(self, id, balance, branches):
        # unique ID of the Branch
        self.id = id
        # replica of the Branch's balance
        self.balance = balance
        # the list of process IDs of the branches
        self.branches = branches
        # the list of Client stubs to communicate with the branches
        self.stubList = list()
        # a list of received messages used for debugging purpose
        self.recvMsg = list()
        # iterate the processID of the branches
        self.eventId = list()
        # local clock start with initial value 1
        self.clock = 1
        self.branchProcesses = list()
        pass

    # This function receives request from customer and branch processes and return results from the requested process
    def MsgDelivery(self, request, context):
        num_branch = request.number_of_fellow
        recvs = []
        for event in request.events:
            interface = event.interface
            money = event.money
            result = self.operate_money(interface, money, num_branch, event.id)
            print(f'branch {self.id} {interface} {money}, result in {self.balance}')
            if interface != QUERY:
                self.recvMsg.append(protos.bank_system_pb2.Recv(interface=interface, result=result))
                self.clock = clockIncrement(self.clock)
                self.branchProcesses.append(protos.bank_system_pb2.ClockProcess(id=event.id,
                                                                                name=DEPOSIT_RESPONSE
                                                                                if interface == DEPOSIT
                                                                                else WITHDRAW_RESPONSE,
                                                                                clock=self.clock))
        return protos.bank_system_pb2.Output(id=self.id, recv=recvs)

    # This function receives request from branch processes and sync the current Branch by performing
    # events from incoming branch id
    # i.e. branch 1 send SyncBranch request to branch 2, branch 2 will execute all events in branch 1
    # if events are deposit call Propogate_Deposit otherwise call Propogate_Withdraw
    def Propogate_Deposit(self, request, context):
        interface = request.interface
        money = request.money
        self.branchProcesses.append(Propogate_Execute(self.clock, DEPOSIT_B_EXECUTE, request.id))
        result = self.operate_money(interface, money, 0, 0)
        print(f'syncing branch {self.id} {interface} {money}, result in {self.balance}')
        return protos.bank_system_pb2.Recv(result=result, clock=self.clock)

    def Propogate_Withdraw(self, request, context):
        interface = request.interface
        money = request.money
        self.branchProcesses.append(Propogate_Execute(self.clock, WITHDRAW_B_EXECUTE, request.id))
        result = self.operate_money(interface, money, 0, 0)
        print(f'syncing branch {self.id} {interface} {money}, result in {self.balance}')
        return protos.bank_system_pb2.Recv(result=result, clock=self.clock)

    # This grpc end point is for getting the final balance
    def getFinalBalance(self, request, context):
        self.recvMsg.append(protos.bank_system_pb2.Recv(interface=QUERY, result=SUCCESS, money=self.balance))
        return protos.bank_system_pb2.Event(id=self.id, interface=QUERY, money=self.balance)

    # return the current balance
    def Query(self):
        return str(self.balance)

    # perform withdraw from current branch
    # send request to fellow branches and perform withdraw in those branches
    # return result
    def Withdraw(self, interface, money, num_branch, event_id):
        tmp_balance = self.balance
        tmp_balance = tmp_balance - money
        if tmp_balance < 0:
            return FAILURE
        else:
            self.balance = tmp_balance
            for i in range(1, num_branch + 1):
                if i != int(self.id):
                    p = PORT + i
                    channel = grpc.insecure_channel(f'localhost:{p}')
                    stub = protos.bank_system_pb2_grpc.BranchServiceStub(channel)
                    # prpogate response
                    prop_response = stub.Propogate_Withdraw(
                        protos.bank_system_pb2.Event(id=event_id, interface=interface, money=money, clock=self.clock))
                    self.clock = selectedClockIncrement(self.clock, prop_response.clock)
                    self.branchProcesses.append(Propogate_Response(self.clock, WITHDRAW_B_RESPONSE, event_id))
            return SUCCESS

    # perform Deposit from current branch
    # send request to fellow branches and perform Deposit in those branches
    # return result
    def Deposit(self, interface, money, num_branch, event_id):
        tmp_balance = self.balance
        tmp_balance = tmp_balance + money
        if tmp_balance < 0:
            return FAILURE
        else:
            self.balance = tmp_balance
            for i in range(1, num_branch + 1):
                if i != int(self.id):
                    p = PORT + i
                    channel = grpc.insecure_channel(f'localhost:{p}')
                    stub = protos.bank_system_pb2_grpc.BranchServiceStub(channel)
                    # prpogate response
                    prop_response = stub.Propogate_Deposit(
                        protos.bank_system_pb2.Event(id=event_id, interface=interface, money=money, clock=self.clock))
                    self.clock = selectedClockIncrement(self.clock, prop_response.clock)
                    self.branchProcesses.append(Propogate_Response(self.clock, DEPOSIT_B_RESPONSE, event_id))
            return SUCCESS

    # a switch function on interface
    def operate_money(self, interface, money, num_branch, event_id):
        if interface == QUERY:
            return self.Query()
        elif interface == DEPOSIT:
            return self.Deposit(interface, money, num_branch, event_id)
        elif interface == WITHDRAW:
            return self.Withdraw(interface, money, num_branch, event_id)
        else:
            return str(self.balance)
