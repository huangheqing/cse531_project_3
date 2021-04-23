# cse531_project_3
# Client Centric Consistency on Distributed Banking System
Implement client centric consistency on our distributed banking system

This system is going to support:
* Monotonic write - Monotonic writes ensures that if a process performs write w1, then w2, then all processes observe w1 before w2.
Monotonic writes does not apply to operations performed by different processes, only writes by the same process.
* Read your write - requires that if a process performs a write w, then that same process performs a subsequent read r, then r must observe w’s effects.

 
## Setup and installation
For running this system on your computer, please make sure following the steps to install required components:
1. Make sure python 3.8 is installed
Please refer to [python 3 website](https://www.python.org/downloads/) to install it
2. Install pip on python3
```
sudo apt update
sudo apt install python3-pip
```
3. Install grpc and grpc tool to support grpc and protobuf
```
python3 -m pip install grpcio
python3 -m pip install grpcio-tools
pip3 install --upgrade protobuf
```
This system only tested on MacOs and Ubuntu 20.04.2.0

If you are willing to run this on other environment, installation steps might be different

## test and run the system

In the repo, there is a main.py which is the main entrance of running system
Please use the following command to test the system

(You can change the test input file, please create your new test file if necessary following the same format as the provided test input file)
```
python3 main.py test_files/input_test_2.txt
```

## Contribute as a developer
This project utilize the grpc lib for creating auto generated services files
Please use the following command to update your services if you modify the proto file
```
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. protos/bank_system.proto
```


