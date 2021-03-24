import grpc
import protos.bank_system_pb2
import protos.bank_system_pb2_grpc

from constant.Operations import QUERY, DEPOSIT, WITHDRAW
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
        for event in request.events:
            event_id = event.id
            interface = event.interface
            money = event.money
            self.operate_money(interface, money)
            print(f'branch {self.id} {interface} {money}, result in {self.balance}')
            if interface != 'query':
                self.recvMsg.append(protos.bank_system_pb2.Recv(interface=interface, result='success'))
        for i in range(1, num_branch + 1):
            if i != int(self.id):
                port = PORT + i
                channel = grpc.insecure_channel(f'localhost:{port}')
                stub = protos.bank_system_pb2_grpc.BranchServiceStub(channel)
                stub.SyncBranch(
                    protos.bank_system_pb2.Events(events=request.events, number_of_fellow=num_branch))
        return request

    # This function receives request from customer and branch processes and return results from the requested process
    def SyncBranch(self, request, context):
        for event in request.events:
            interface = event.interface
            money = event.money
            self.operate_money(interface, money)
            print(f'syncing branch {self.id} {interface} {money}, result in {self.balance}')
        return request

    def getFinalBalance(self, request, context):
        self.recvMsg.append(protos.bank_system_pb2.Recv(interface='query', result='success', money=self.balance))
        return protos.bank_system_pb2.Event(id=self.id, interface='query', money=self.balance)

    def getOutput(self, request, context):
        return protos.bank_system_pb2.Output(id=self.id, recv=self.recvMsg)

    def operate_money(self, interface, money):
        if interface == QUERY:
            self.balance = self.balance
        elif interface == DEPOSIT:
            self.balance = self.balance + money
        elif interface == WITHDRAW:
            self.balance = self.balance - money
        else:
            self.balance = self.balance
