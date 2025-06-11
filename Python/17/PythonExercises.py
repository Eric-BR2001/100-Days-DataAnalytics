import os
from dotenv import load_dotenv
from openai import OpenAI

# Load API key from .env
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI client
client = OpenAI(api_key=api_key)

chat_history = []

print("🤖 Chatbot is running. Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("👋 Goodbye!")
        break

    chat_history.append({"role": "user", "content": user_input})

    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=chat_history,
            temperature=0.7
        )

        reply = response.choices[0].message.content.strip()
        print(f"Bot: {reply}\n")
        chat_history.append({"role": "assistant", "content": reply})

    except Exception as e:
        print("⚠️ Error:", str(e))
        break
