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

        initial_balance = 0
        for data_item in input_data:
            if data_item['type'] == 'bank':
                initial_balance = data_item['balance']
        processes = []
        dests = {}
        events = []
        final_output_branch = 1
        if len(input_data) > 1:
            for data in input_data:
                if data['type'] == 'customer':
                    events = data['events']
                    # We grab all customers process and based on the customer id
                    # create branch services
                    for event in events:
                        dests.add(event['dest'])
                        if event['interface'] == 'query':
                            final_output_branch = event['dest']
                    for dest in dests:
                        run_backend(dest, initial_balance, processes)
                        events = events

        # Single customer process:
        time.sleep(2)
        client_request(0, events, len(dests))

        # Get results from the branch services
        events = {}
        outputList = []

        # get final balance
        port = PORT + final_output_branch
        channel = grpc.insecure_channel(f'localhost:{port}')
        stub = protos.bank_system_pb2_grpc.BranchServiceStub(channel)
        process_out = stub.getFinalBalance(protos.bank_system_pb2.BranchProcess(pid=cus_id))
        for item in process_out.data:
            eventId = item.id
            name = item.name
            clock = item.clock
            if eventId not in events:
                events[eventId] = [item]
            else:
                events[eventId].append(item)
        json_str = json.dumps(json_format.MessageToJson(process_out))
        replaced_json = json_str.replace('\\n', '').replace('\\"', '"').replace(' ', '')
        replaced_json = replaced_json[1:-1]
        outputList.append(replaced_json)
        print(replaced_json)
        for id in events.keys():
            sorted_events = sorted(events[id], key=lambda item: item.clock)
            events[id] = sorted_events
            event_list = []
            for item in sorted_events:
                event_list.append(
                    '{"clock": {item.clock}, "name": "{item.name}"}'.replace('{item.clock}', str(item.clock)).replace(
                        '{item.name}', item.name))
            json_str = '{"eventId":{id}, "data":[{",".join(event_list)}]}'.replace('{id}', str(id)).replace(
                '{",".join(event_list)}', ",".join(event_list))
            outputList.append(json_str)
        outputJson = f'[{",".join(outputList)}]'
        print(outputJson)
        json_object = json.loads(outputJson)
        json_formatted_str = json.dumps(json_object, indent=2)
        print(json_formatted_str)
        with open(f'output/output.txt', 'w') as the_file:
            the_file.write(json_formatted_str + '\n')
        print('end of client')
