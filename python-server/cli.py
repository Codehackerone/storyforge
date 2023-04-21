import grpc
import textgen_pb2
import textgen_pb2_grpc

def run():
  with grpc.insecure_channel("localhost:50051") as channel:
    stub = textgen_pb2_grpc.TextGeneratorStub(channel)
    while True:
        prompt = input("Enter a prompt (or 'q' to quit): ")
        if prompt == "q":
            break
        length = int(input("Enter the length of the generated text: "))
        request = textgen_pb2.TextRequest(prompt=prompt, length=length)
        response = stub.GenerateText(request)
        print(f"Generated text: {response.text}\n")
        
if __name__ == "__main__":
  run()        