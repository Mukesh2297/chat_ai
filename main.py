from dotenv import load_dotenv
from gradio.monitoring_dashboard import demo
from openai import OpenAI
import os
import gradio as gr

load_dotenv(override=True)

MODEL = "gpt-4o-mini"
LOCAL_MODEL = "llama3.1"


def chat(message, history):
    client = OpenAI(api_key="not applicable", base_url="http://localhost:11434/v1")

    response = client.chat.completions.create(model=LOCAL_MODEL, messages=[
        {"role": "user", "content": message}])
    print("Client initialized with API key.")

    resp = response.choices[0].message.content;

    print(response.choices[0].message.content)
    return resp


def main():
    demo = gr.ChatInterface(fn=chat)
    demo.launch()

if __name__ == "__main__":
    main()

