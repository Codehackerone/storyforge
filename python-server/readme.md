# Python gRPC Server
This is a gRPC server that generates text using a pre-trained distilgpt2 model as well as custom trained tensorflow model. It exposes a single GenerateText method that takes in a TextRequest object and returns a TextResponse object. Also, it has a streaming capability that allows the client to send multiple TextRequest objects and receive multiple TextResponse objects by the rust server.

# Prerequisites
Before running the server or client, make sure you have the following dependencies installed:

Python 3.9 or higher
gRPC
transformers
torch

# Install

`
make compile
make python-build
`

# To Run the server
`
make run
`

To test and use cli
`
make cli
`

or 

`
make test
`


# How to use
You can modify the prompt and length of the generated text by editing the prompt and length variables in the client.py file.

# Contributing
If you find any issues or have suggestions for improvement, feel free to open an issue or create a pull request.

# License
This project is licensed under the MIT License. See the LICENSE file for details.