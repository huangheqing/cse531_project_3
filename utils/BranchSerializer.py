import protos.bank_system_pb2
import json


def serialize_branch(data):
    return protos.bank_system_pb2.Branch(id=1, type="", balance=200)
