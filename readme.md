# StoryForge
StoryForge is a fictional text-generation project that uses a custom-made GRU architecture to generate fictional stories. The project has two main components: a Python backend server and a Rust server. The Python backend server uses a manually-curated dataset of fictional stories to generate text, while the Rust server displays the generated text to the user.

# Python Backend Server
The Python backend server is responsible for generating the text using the GRU architecture. It uses a dataset of fictional stories to train the model and generate new text. The generated text is returned as a gRPC response to the Rust server. The server is implemented using the gRPC Python library and communicates with the Rust server using the textgen.proto file.

Go to the python-server directory

# Rust Server
The Rust server is responsible for displaying the generated text to the user. It acts as a client to the Python backend server and sends requests for generated text. When it receives a response from the Python server, it displays the generated text to the user. The server is implemented using the gRPC Rust library and communicates with the Python server using the textgen.proto file.

Go to the rust-server directory

# Installation

To run and install python server,
`make python-dev`

To run and install rust server,
`make rust-dev`