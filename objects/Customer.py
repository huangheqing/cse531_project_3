import grpc
import time


class Customer:
    def __init__(self, id, events):
        # unique ID of the Customer
        self.id = id
        # events from the input
        self.events = events
        # a list of received messages used for debugging purpose
        self.recvMsg = list()
        # pointer for the stub
        self.stub = None

    # This function communicate with the Branch by the specified branch ID
    def createStub(self):
        pass

    # process events from the list and submit the requests to branch process
    def executeEvents(self):
        pass
