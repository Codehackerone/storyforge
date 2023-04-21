from concurrent import futures
import grpc
import tensorflow as tf
import proto.textgen_pb2 as textgen_pb2
import proto.textgen_pb2_grpc as textgen_pb2_grpc

class TextGenServicer(textgen_pb2_grpc.TextGenServicer):
    def __init__(self, model_path):
        self.model = tf.saved_model.load(model_path)

    def Generate(self, request_iterator, context):
        for request in request_iterator:
            input_text = request.input
            length = request.length
            generated_text = self.model(input_text, length)
            response = textgen_pb2.TextResponse(output=generated_text)
            yield response

def serve(model_path):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    textgen_pb2_grpc.add_TextGenServicer_to_server(TextGenServicer(model_path), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve('./model/fiction_gen.h5')