import grpc
from concurrent import futures
import json
import sys

import protos.bank_system_pb2
import protos.bank_system_pb2_grpc

from constant.Operations import WITHDRAW, QUERY, DEPOSIT
from server.Branch import Branch
from server.Customer import Customer

if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[0] == 'main.py':
        filename = sys.argv[1]
        try:
            with open(sys.argv[1]) as f:
                input_data = json.load(f)
        except "Not able to process file":
            print(f'not able to load the json file: {filename}')

        balance = input_data[0]['events'][0]['money']
        initial_balance = input_data[0]['events'][0]['money']
        print(f'initial balance is {initial_balance}')
        if len(input_data) > 1:
            for data in input_data:
                if data['type'] == 'customer':
                    i = data['id']
                    events = data['events']
                    for event in events:
                        if event['interface'] == QUERY:
                            balance = balance
                        elif event['interface'] == DEPOSIT:
                            balance = balance + event['money']
                        elif event['interface'] == WITHDRAW:
                            balance = balance - event['money']
                        else:
                            balance = balance
                    # We grab all customers process and based on the customer id
                    # create branch services
                    branch = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
                    protos.bank_system_pb2_grpc.add_BranchServiceServicer_to_server(Branch(i, initial_balance, []),
                                                                                    branch)
                    port = 8080 + i
                    print(f'Starting backend server. Listening on port {port}')
                    branch.add_insecure_port(f'localhost:{port}')
                    branch.start()
                    # make request from the client to backend
                    customer = Customer(i, events)
                    customer.createStub()
                    customer.executeEvents()
        print(f'final balance is {balance}')
