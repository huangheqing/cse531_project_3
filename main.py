import grpc
from concurrent import futures
import json
import sys

import protos.bank_system_pb2
import protos.bank_system_pb2_grpc

from constant.Operations import WITHDRAW, QUERY, DEPOSIT
from server.Branch import Branch
from server.Customer import Customer

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[0] == 'main.py':
        filename = sys.argv[1]
        try:
            with open(sys.argv[1]) as f:
                input_data = json.load(f)
        except "Not able to process file":
            print(f'not able to load the json file: {filename}')

        balance = input_data[0]['events'][0]['money']
        print(f'initial balance is {balance}')
        if len(input_data) > 1:
            for data in input_data:
                if data['type'] == 'customer':
                    i = data['id']
                    for event in data['events']:
                        if event['interface'] == QUERY:
                            balance = balance
                        elif event['interface'] == DEPOSIT:
                            balance = balance + event['money']
                        elif event['interface'] == WITHDRAW:
                            balance = balance - event['money']
                        else:
                            balance = balance
                    # We grab all customers process and based on the customer id
                    # create client services and branch services
                    branch = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
                    protos.bank_system_pb2_grpc.add_BranchServiceServicer_to_server(Branch(i, 400, []), branch)
                    print(f'Starting backend server. Listening on port 808{i}')
                    branch.add_insecure_port(f'localhost:808{i}')
                    branch.start()
                    # create a stub (client)
                    channel = grpc.insecure_channel(f'localhost:808{i}')
                    stub = protos.bank_system_pb2_grpc.BranchServiceStub(channel)
                    Customer(i, data['events'], stub)
        print(f'final balance is {balance}')
