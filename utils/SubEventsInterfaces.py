import protos.bank_system_pb2


def Event_Request(local_clock, event, event_id):
    return protos.bank_system_pb2.ClockProcess(id=event_id,
                                               name=event,
                                               clock=local_clock)


def Event_Execute(local_clock, event, event_id):
    return protos.bank_system_pb2.ClockProcess(id=event_id, name=event, clock=local_clock)


def Propagate_Request(local_clock, event, event_id):
    return protos.bank_system_pb2.ClockProcess(id=event_id,
                                               name=event,
                                               clock=local_clock)


def Propogate_Execute(local_clock, event, event_id):
    return protos.bank_system_pb2.ClockProcess(id=event_id, name=event, clock=local_clock)


def Propogate_Response(local_clock, event, event_id):
    return protos.bank_system_pb2.ClockProcess(id=event_id, name=event, clock=local_clock)


def selectedClockIncrement(local_clock, remote_clock):
    return max(local_clock, remote_clock) + 1


def clockIncrement(clock):
    return clock + 1
