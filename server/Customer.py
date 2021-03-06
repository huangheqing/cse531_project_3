import grpc
import protos.bank_system_pb2
import protos.bank_system_pb2_grpc
from utils.constant import PORT


class Customer():
    def __init__(self, id, events, number_of_fellow):
        # unique ID of the Customer
        self.id = id
        # events from the input
        self.events = events
        # a list of received messages used for debugging purpose
        self.recvMsg = list()
        # number of branches opened
        self.num_of_fellow = number_of_fellow
        # pointer for the stub
        self.stub = None

    # process events from the list and submit the requests to branch process
    def executeEvents(self):
        for event in self.events:
            port = PORT + event['dest']
            channel = grpc.insecure_channel(f'localhost:{port}')
            self.stub = protos.bank_system_pb2_grpc.BranchServiceStub(channel)
            self.stub.MsgDelivery(
                protos.bank_system_pb2.Events(events=[event], number_of_fellow=self.num_of_fellow, clock=1))
