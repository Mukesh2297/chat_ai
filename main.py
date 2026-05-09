from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv(override=True)

def main():
    client = OpenAI(
        api_key="not-needed",
        base_url="http://localhost:11434/v1"
    )

    response = client.chat.completions.create(model="llama3.1", messages=[{"role": "user", "content": "Hi"}])

    print("Client initialized with API key.")
    print(response.choices[0].message)

if __name__ == "__main__":
    main()
