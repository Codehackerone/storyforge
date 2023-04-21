use tonic::transport::Channel;
use textgen::text_generator_client::TextGeneratorClient;
use textgen::TextRequest;

mod textgen {
    include!("textgen.rs");
}

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let channel = Channel::from_static("http://localhost:50051").connect().await?;
    let mut client = TextGeneratorClient::new(channel);

    let mut prompt = String::new();
    prompt.push_str("Once upon a time, there was a ");
    let request = tonic::Request::new(TextRequest { prompt: prompt, length: 50});
    let response = client.generate_text(request).await?.into_inner();

    println!("Response from server: {:?}", response.text);

    Ok(())
}
