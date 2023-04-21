// Importing the io and Write modules from the std library.
use std::io::{self, Write};

// Importing the Channel and other necessary modules from tonic transport and textgen crate.
use tonic::transport::Channel;
use textgen::text_generator_client::TextGeneratorClient;
use textgen::TextRequest;

// importing the module textgen from the textgen.rs file in the same directory.
mod textgen {
    include!("textgen.rs");
}

#[tokio::main] // The tokio runtime is used to run this async function
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    // Creating a channel to communicate with the server from the given endpoint.
    let channel = Channel::from_static("http://localhost:50051").connect().await?;

    // Creating a client for the TextGenerator service using the created channel.
    let mut client = TextGeneratorClient::new(channel);

    // Receiving input from user until option q is entered to quit the program.
    loop {
        print!("Enter a prompt(q to quit): ");
        io::stdout().flush()?; // Flushing any buffered output to ensure that it's displayed on screen immediately.
        let mut prompt = String::new(); // Initializing an empty string.

        // Reading user input from stdin.
        io::stdin().read_line(&mut prompt)?;

        if prompt.trim() == "q" { // Quitting the program if input is q.
            break;
        }

        print!("Enter length of text to generate: ");
        io::stdout().flush()?;
        let mut length_input = String::new();
        io::stdin().read_line(&mut length_input)?;
        let length = length_input.trim().parse::<u32>().unwrap_or(50); // Parsing user input as unsigned integer, or assigning 50 as default.

        // Creating a request to the server with given prompt and length.
        let request = tonic::Request::new(TextRequest { prompt, length: length as i32 });

        // Sending the request to the server through the client object and storing the result in response variable.
        let response = client.generate_text(request).await?.into_inner();

        // Displaying the generated text on console.
        println!("Response from server: {:?}", response.text);
    }

    // Return an empty Ok() type result since there were no errors during execution.
    Ok(())
}
