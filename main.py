import grpc
from concurrent import futures
import json
import sys

# import the generated classes
import protos.bank_system_pb2
import protos.bank_system_pb2_grpc


class Server(protos.bank_system_pb2_grpc.BankSystemServicer):
    def createStub(self, request, context):
        print(request)
        return request

    def executeEvents(self, request, context):
        print(request)
        return request

    def MsgDelivery(self, request, context):
        print(request)
        return request


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[0] == 'main.py':
        filename = sys.argv[1]
        try:
            with open(sys.argv[1]) as f:
                input_data = json.load(f)
        except "Not able to process file":
            print(f'not able to load the json file: {filename}')

        if len(input_data) > 1:
            for data in input_data:
                print(data)

        # open a gRPC channel
        channel = grpc.insecure_channel('localhost:8081')

        # create a stub (client)
        stub = protos.bank_system_pb2_grpc.BankSystemStub(channel)

        # Generate x amount of services based on the input files branches/custoemrs
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        protos.bank_system_pb2_grpc.add_BankSystemServicer_to_server(Server(), server)
        print('Starting server. Listening on port 8081.')
        server.add_insecure_port('localhost:8081')
        server.start()

        # create a valid request message
        customer = protos.bank_system_pb2.Customer(id=1, type="", events=[""])
        branch = protos.bank_system_pb2.Branch(id=1, type="", balance=200)

        # make the call
        processEvent = stub.createStub(customer)
        syncBranch = stub.executeEvents(branch)

        # print(processEvent)
        # print(syncBranch)
