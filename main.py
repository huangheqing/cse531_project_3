import grpc
from concurrent import futures
import json
import sys
import protos.bank_system_pb2
import protos.bank_system_pb2_grpc

from constant.Operations import WITHDRAW, QUERY, DEPOSIT
from server.Branch import Branch
from server.Customer import Customer


def client_request(id):
    customer = Customer(id, customer_requests[id], len(customer_requests))
    print(f'requesting branch {id}')
    customer.createStub()
    customer.executeEvents()


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
        customer_requests = {}
        if len(input_data) > 1:
            for data in input_data:
                if data['type'] == 'customer':
                    i = data['id']
                    events = data['events']
                    # We grab all customers process and based on the customer id
                    # create branch services
                    customer_requests[i] = events

        print(f'final balance is {balance}')
        for cus_id in customer_requests.keys():
            # make request from the client to backend
            # We passed the number of fellow branches to the Customer class so the branches can update the
            # fellow server accordingly
            client_request(cus_id)
