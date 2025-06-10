# Day 1 – Introduction to LLMs in Python

Welcome to **Day 1** of our hands-on LLM in Python series!  
Today’s focus is on understanding and experimenting with **Large Language Models** using Python through two major tools:

- 🔹 [OpenAI API](https://platform.openai.com/docs/)
- 🔹 [Hugging Face Transformers](https://huggingface.co/docs/transformers)

---

## 🧠 Objectives

- Set up your Python environment
- Make basic text generation requests to LLMs
- Compare outputs between OpenAI and Hugging Face models

---

## 📦 Requirements

```bash
pip install openai transformers
````

---

## 🔐 API Setup

If using OpenAI, get your API key from [https://platform.openai.com/account/api-keys](https://platform.openai.com/account/api-keys)

### Option 1: Use `.env` file

```bash
# .env
OPENAI_API_KEY=your-api-key-here
```

Load it in Python:

```python
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
```

### Option 2: Hardcode (not recommended)

```python
client = OpenAI(api_key="your-api-key")
```

---

## 🧪 Examples

### ✅ Example 1: OpenAI GPT (Chat Completion)

```python
from openai import OpenAI

client = OpenAI(api_key="your-api-key")

response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "user", "content": "Explain what a Large Language Model is."}
    ]
)

print(response.choices[0].message.content)
```

---

### ✅ Example 2: Hugging Face Transformers (GPT-2)

```python
from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")

response = generator("Once upon a time, there was a developer who", max_length=50)
print(response[0]['generated_text'])
```

---

