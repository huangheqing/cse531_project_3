import grpc
from concurrent import futures
import time

# import the generated classes
import protos.bank_system_pb2
import protos.bank_system_pb2_grpc


class Server(protos.bank_system_pb2_grpc.BankSystemServicer):

    def processEvent(self, request, context):
        print(request)
        return request

    def syncBranch(self, request, context):
        print(request)
        return request


# create a gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

protos.bank_system_pb2_grpc.add_BankSystemServicer_to_server(Server(), server)

# listen on port 8081
print('Starting server. Listening on port 8081.')
server.add_insecure_port('localhost:8081')
server.start()

# since server.start() will not block,
# a sleep-loop is added to keep alive
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    server.stop(0)
