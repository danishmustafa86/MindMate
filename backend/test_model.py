import os
from openai import OpenAI

# Initialize the OpenAI client
client = OpenAI(
    base_url="https://api.aimlapi.com/v1",  # AIML API URL
    api_key="<45b240cf29474d64a2f9bea01d7b892c>",               # Replace with your API key
)

# Send a message to the AI model and get the response
response = client.chat.completions.create(
    model="deepseek/deepseek-chat",
    messages=[
        {"role": "system", "content": "You are an AI assistant who knows everything."},
        {"role": "user", "content": "Tell me, why is the sky blue?"}
    ]
)

# Extract and print the response from the assistant
message = response.choices[0].message.content
print(f"Assistant: {message}")
