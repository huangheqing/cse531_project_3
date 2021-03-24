import grpc
from concurrent import futures
import sys

import protos.bank_system_pb2_grpc

from server.Branch import Branch
from utils.constant import PORT

if __name__ == '__main__':
    branch = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    customer_id = int(sys.argv[1])
    initial_value = int(sys.argv[2])
    protos.bank_system_pb2_grpc.add_BranchServiceServicer_to_server(Branch(customer_id, initial_value, []), branch)
    port = PORT + customer_id
    print(f'start backend at localhost:{port}')
    branch.add_insecure_port(f'localhost:{port}')
    branch.start()
    branch.wait_for_termination()
