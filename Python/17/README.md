# 💬 Day 3 – Build a Chatbot Using a Large Language Model (LLM)

Welcome to **Day 3** of the LLM in Python mini-project!  
Today you'll build a simple but powerful chatbot that uses an LLM to chat with the user in real time from the terminal.

You’ll use either the **OpenAI API** or a **Hugging Face model** (like DialoGPT or Mistral) to simulate conversational AI.

---

## 🎯 Objectives

- Build a terminal-based chatbot using Python
- Use LLMs to handle user input and return natural responses
- Maintain conversation history for better context

---

## 📦 Requirements

```bash
pip install openai transformers
````

---

## 🔐 API Setup (for OpenAI)

```bash
# .env
OPENAI_API_KEY=your-api-key-here
```

Load it in your script:

```python
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
```

---

## ▶️ How to Run

```bash
python PythonExercises.py
```

Type `exit` or `quit` to end the conversation.

---

## 🧪 Example Conversation

```
You: How does photosynthesis work?
Bot: Photosynthesis is the process by which green plants use sunlight to convert water and carbon dioxide into food (glucose) and oxygen...
```

---

## 🧠 Features in This Bot

* Chat history maintained between turns (OpenAI version)
* User can type freely, exit anytime
* Hugging Face option works offline (good for experimentation)

---

