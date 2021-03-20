# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import grpc

# import the generated classes
import protos.bank_system_pb2
import protos.bank_system_pb2_grpc

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # open a gRPC channel
    channel = grpc.insecure_channel('localhost:8081')

    # create a stub (client)
    stub = protos.bank_system_pb2_grpc.BankSystemStub(channel)

    # create a valid request message
    customer = protos.bank_system_pb2.Customer(id=1, type="", events=[""])
    branch = protos.bank_system_pb2.Branch(id=1, type="", balance=200)

    # make the call
    processEvent = stub.processEvent(customer)
    syncBranch = stub.syncBranch(branch)

    print(processEvent)
    print(syncBranch)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
