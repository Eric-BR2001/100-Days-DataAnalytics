# 🗼 Planning a Trip to Paris with the OpenAI API

This project uses OpenAI's powerful API to build a simple chatbot that answers common tourist questions about Paris. It demonstrates how to format a conversation for the API, set up the model's behavior, and generate accurate, concise responses.

## ✨ Project Overview

You'll create a chatbot capable of responding to the following questions:

1. **How far away is the Louvre from the Eiffel Tower (in miles) if you are driving?**
2. **Where is the Arc de Triomphe?**
3. **What are the must-see artworks at the Louvre Museum?**

## 🛠️ How It Works

- The conversation is structured as a list of dictionaries with two main keys:
  - `"role"`: defines the speaker (`system`, `user`, or `assistant`)
  - `"content"`: the message content

- The conversation begins with a **system message** to guide the assistant's behavior.

- The API parameters are:
  - `temperature`: `0.0` (for deterministic responses)
  - `max_tokens`: `100` (to limit response length)

## 🧠 Example Conversation Structure

```python
conversation = [
  {"role": "system", "content": "You are a helpful travel assistant knowledgeable about Paris tourist attractions."},
  {"role": "user", "content": "How far away is the Louvre from the Eiffel Tower (in miles) if you are driving?"},
  {"role": "assistant", "content": "The Louvre Museum is about 2.4 miles away from the Eiffel Tower by car, depending on traffic."},
  {"role": "user", "content": "Where is the Arc de Triomphe?"},
  {"role": "assistant", "content": "The Arc de Triomphe is located at the western end of the Champs-Élysées, at Place Charles de Gaulle, Paris."},
  {"role": "user", "content": "What are the must-see artworks at the Louvre Museum?"},
  {"role": "assistant", "content": "Must-see artworks at the Louvre include the Mona Lisa, Venus de Milo, Winged Victory of Samothrace, Liberty Leading the People, and The Coronation of Napoleon."}
]
````

## 🔧 Requirements

* Python 3.7+
* OpenAI Python SDK (`openai`)

## 🚀 Getting Started

1. Install the OpenAI SDK:

   ```bash
   pip install openai
   ```

2. Set your API key:

   ```python
   import openai
   openai.api_key = "your-api-key"
   ```

3. Run the script using the conversation structure provided.

