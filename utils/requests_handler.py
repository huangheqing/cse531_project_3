import subprocess
from server.Customer import Customer


def run_backend(customer_id, initial_value, processes):
    command = f"python3 backend_server.py {customer_id} {initial_value}"
    c = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    processes.append(c)


def client_request(id, events, branch_num):
    customer = Customer(id, events, branch_num)
    print(f'requesting branch {id}')
    customer.createStub()
    customer.executeEvents()
