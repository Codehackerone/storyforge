# Rust gRPC Server Interacting with Python gRPC Server
This repository contains an implementation of a Rust gRPC server that interacts with a Python gRPC server

The Rust server forwards incoming gRPC requests to the Python server and converts the Python responses to Rust responses.

# Prerequisites
To run this example, you need to have the following installed on your machine:

- Rust 
- Python >= 3.9 
- pip package manager for Python

# Installation

` cargo build`

## Running the server

` cargo run --bin cli`
