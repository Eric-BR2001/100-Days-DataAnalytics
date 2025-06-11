# Day 2 – Prompt Engineering & Response Tuning

Welcome to **Day 2** of our LLM in Python series!  
Today’s focus is on understanding how to **improve and control LLM responses** using prompt engineering techniques and response parameters.

We’ll explore how changing things like **temperature**, **max tokens**, and **prompt phrasing** can produce dramatically different outputs.

---

## 🎯 Objectives

- Learn to craft better prompts for LLMs
- Experiment with `temperature` and `max_tokens`
- Compare multiple styles of asking the same question

---

## 📦 Requirements

```bash
pip install openai
````

---

## 🔐 API Setup

If you haven’t already, create a `.env` file:

```bash
# .env
OPENAI_API_KEY=your-api-key-here
```

And load it in your script:

```python
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
```

---

## 🧪 Examples

### ✅ Example 1: Varying Temperature

```python
response = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "Tell me a creative story about a robot that learns to paint."}],
    temperature=0.9,  # Higher = more creative
    max_tokens=150
)
print(response.choices[0].message.content)
```

Try this again with `temperature=0.3` and compare the results.

---

### ✅ Example 2: Different Prompt Styles

```python
prompts = [
    "What is recursion?",
    "Explain recursion with a simple code example.",
    "Explain recursion like I'm five."
]

for prompt in prompts:
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    print(f"Prompt: {prompt}\nResponse: {response.choices[0].message.content}\n{'-'*50}")
```

---

