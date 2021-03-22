import protos.bank_system_pb2
import json


def serialize_customer(data):
    return protos.bank_system_pb2.Customer(id=1, type="", balance=200)
