PROTOC = python -m grpc_tools.protoc
SERVER = python server.py
TEST = python test.py

all: compile run

compile:
	$(PROTOC) -I. --python_out=. --grpc_python_out=. textgen.proto

# Install Python dependencies
python-build:	
	pip install -r requirements.txt

run:
	$(SERVER)

test:
	$(TEST)

clean:
	rm -f textgen_pb2.py textgen_pb2_grpc.py