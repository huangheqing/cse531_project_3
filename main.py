import grpc
import json
import sys

from google.protobuf import json_format

import protos.bank_system_pb2
import protos.bank_system_pb2_grpc
import time

from utils.requests_handler import run_backend, client_request
from utils.constant import PORT

if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[0] == 'main.py':
        filename = sys.argv[1]
        try:
            with open(sys.argv[1]) as f:
                input_data = json.load(f)
        except "Not able to process file":
            print(f'not able to load the json file: {filename}')

        initial_balance = input_data[0]['events'][0]['money']
        print(f'initial balance is {initial_balance}')
        customer_requests = {}
        processes = []
        if len(input_data) > 1:
            for data in input_data:
                if data['type'] == 'customer':
                    i = data['id']
                    events = data['events']
                    # We grab all customers process and based on the customer id
                    # create branch services
                    run_backend(i, initial_balance, processes)
                    customer_requests[i] = events

        for cus_id in customer_requests.keys():
            # make request from the client to backend
            # We passed the number of fellow branches to the Customer class so the branches can update the
            # fellow server accordingly
            client_request(cus_id, customer_requests[cus_id], len(customer_requests))
            time.sleep(1)

        # This is just for sake of simplicity to make sure all processes are finished
        time.sleep(2)

        # Get results from the branch services
        for cus_id in customer_requests.keys():
            # get final balance
            port = PORT + cus_id
            channel = grpc.insecure_channel(f'localhost:{port}')
            stub = protos.bank_system_pb2_grpc.BranchServiceStub(channel)
            print(stub.getFinalBalance(protos.bank_system_pb2.Event(id=cus_id, interface='query')))

        output = ''
        # Get results from the branch services
        for cus_id in customer_requests.keys():
            # get final balance
            port = PORT + cus_id
            channel = grpc.insecure_channel(f'localhost:{port}')
            stub = protos.bank_system_pb2_grpc.BranchServiceStub(channel)
            output = output + json.dumps(
                json_format.MessageToJson(stub.getOutput(protos.bank_system_pb2.Output()))) \
                .replace('\\n', '') \
                .replace('\\"', '\'') \
                .replace('"', '') \
                .replace(' ', '') + '\n'
        print(output)
        with open(f'output/output.txt', 'w') as the_file:
            the_file.write(output + '\n')
        print('end of client')
