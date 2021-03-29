import grpc
import protos.bank_system_pb2
import protos.bank_system_pb2_grpc

from utils.Operations import QUERY, DEPOSIT, WITHDRAW
from utils.constant import PORT


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
        pass

    # This function receives request from customer and branch processes and return results from the requested process
    def MsgDelivery(self, request, context):
        num_branch = request.number_of_fellow
        recvs = []
        for event in request.events:
            interface = event.interface
            money = event.money
            result = self.operate_money(interface, money, num_branch)
            recvs.append(protos.bank_system_pb2.Recv(result=result))
            print(f'branch {self.id} {interface} {money}, result in {self.balance}')
            if interface != 'query':
                self.recvMsg.append(protos.bank_system_pb2.Recv(interface=interface, result=result))
        return protos.bank_system_pb2.Output(id=self.id, recv=recvs)

    # This function receives request from branch processes and sync the current Branch by performing
    # events from incoming branch id
    # i.e. branch 1 send SyncBranch request to branch 2, branch 2 will execute all events in branch 1
    # if events are deposit call Propogate_Deposit otherwise call Propogate_Withdraw
    def Propogate_Deposit(self, request, context):
        interface = request.interface
        money = request.money
        result = self.operate_money(interface, money, 0)
        print(f'syncing branch {self.id} {interface} {money}, result in {self.balance}')
        return protos.bank_system_pb2.Recv(result=result)

    def Propogate_Withdraw(self, request, context):
        interface = request.interface
        money = request.money
        result = self.operate_money(interface, money, 0)
        print(f'syncing branch {self.id} {interface} {money}, result in {self.balance}')
        return protos.bank_system_pb2.Recv(result=result)

    # This grpc end point is for getting the final balance
    def getFinalBalance(self, request, context):
        self.recvMsg.append(protos.bank_system_pb2.Recv(interface='query', result='success', money=self.balance))
        return protos.bank_system_pb2.Event(id=self.id, interface='query', money=self.balance)

    # This grpc end point is for getting the output txt line for current branch
    def getOutput(self, request, context):
        return protos.bank_system_pb2.Output(id=self.id, recv=self.recvMsg)

    # return the current balance
    def Query(self):
        return str(self.balance)

    # perform withdraw from current branch
    # send request to fellow branches and perform withdraw in those branches
    # return result
    def Withdraw(self, interface, money, num_branch):
        tmp_balance = self.balance
        tmp_balance = tmp_balance - money
        if tmp_balance < 0:
            return 'failure'
        else:
            self.balance = tmp_balance
            for i in range(1, num_branch + 1):
                if i != int(self.id):
                    p = PORT + i
                    channel = grpc.insecure_channel(f'localhost:{p}')
                    stub = protos.bank_system_pb2_grpc.BranchServiceStub(channel)
                    stub.Propogate_Withdraw(protos.bank_system_pb2.Event(id=self.id, interface=interface, money=money))
            return 'success'

    # perform Deposit from current branch
    # send request to fellow branches and perform Deposit in those branches
    # return result
    def Deposit(self, interface, money, num_branch):
        tmp_balance = self.balance
        tmp_balance = tmp_balance + money
        if tmp_balance < 0:
            return 'failure'
        else:
            self.balance = tmp_balance
            for i in range(1, num_branch + 1):
                if i != int(self.id):
                    p = PORT + i
                    channel = grpc.insecure_channel(f'localhost:{p}')
                    stub = protos.bank_system_pb2_grpc.BranchServiceStub(channel)
                    stub.Propogate_Deposit(protos.bank_system_pb2.Event(id=self.id, interface=interface, money=money))
            return 'success'

    # a switch function on interface
    def operate_money(self, interface, money, num_branch):
        if interface == QUERY:
            return self.Query()
        elif interface == DEPOSIT:
            return self.Deposit(interface, money, num_branch)
        elif interface == WITHDRAW:
            return self.Withdraw(interface, money, num_branch)
        else:
            return str(self.balance)
