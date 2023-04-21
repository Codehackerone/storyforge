import grpc
import textgen_pb2
import textgen_pb2_grpc

def test():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = textgen_pb2_grpc.TextGeneratorStub(channel)
        prompt = "Once upon a time"
        length = 50
        request = textgen_pb2.TextRequest(prompt=prompt, length=length)
        response = stub.GenerateText(request)
        print(f"Generated text: {response.text}")
        

if __name__ == "__main__":
    test()