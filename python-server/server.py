# Importing necessary modules and libraries for the TextGeneratorServicer class.
import grpc
from transformers import AutoTokenizer, AutoModelWithLMHead
import concurrent.futures as futures

# Importing the textgen_pb2 and textgen_pb2_grpc modules generated from protobuf files.
import textgen_pb2
import textgen_pb2_grpc

class TextGeneratorServicer(textgen_pb2_grpc.TextGeneratorServicer):
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("distilgpt2") # Initializing tokenizer for DistilGPT2 model.
        self.model = AutoModelWithLMHead.from_pretrained("distilgpt2") # Initializing pre-trained DistilGPT2 model.

    def GenerateText(self, request, context): 
        input_ids = self.tokenizer.encode(request.prompt, return_tensors="pt") # Tokenizing prompt into input_ids.
        output = self.model.generate( # Generating text using initialized DistilGPT2 model.
            input_ids,
            max_length=request.length,
            pad_token_id=self.tokenizer.eos_token_id,
            num_beams=5,
            no_repeat_ngram_size=2,
            early_stopping=True,
        )
        generated_text = self.tokenizer.decode(output[0], skip_special_tokens=True) # Decoding generated output to readable text.
        return textgen_pb2.TextResponse(text=generated_text) # Returning generated text from server as TextResponse.

def serve():
    # Creating a gRPC server with ThreadPoolExecutor.
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    # Adding the TextGeneratorServicer instance to the gRPC server.
    textgen_pb2_grpc.add_TextGeneratorServicer_to_server(TextGeneratorServicer(), server)

    # Binding the server to listen on port 50051.
    server.add_insecure_port("[::]:50051")

    # Starting the server and waiting for it to be terminated.
    print("Starting server. Listening on port 50051.")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve() # Calling the serve function to start the server. 
