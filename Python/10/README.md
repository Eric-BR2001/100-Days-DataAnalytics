# 💸 Dollar Value Bot (USD to BRL) with Selenium

This project uses **Python** and **Selenium** to automatically fetch the current exchange rate of the US Dollar (USD) to Brazilian Real (BRL) using **Google Search**.

## 🔍 What It Does

- Opens Google in a browser using Selenium
- Searches for "USD to BRL"
- Scrapes the current exchange rate from the search results
- Prints the value in the console

## 📦 Requirements

- Python 3.7+
- Google Chrome
- ChromeDriver (must match your Chrome version)

## 🧪 Installation

1. Install the required Python library:

```bash
pip install selenium
````

2. Download ChromeDriver from:
   [https://sites.google.com/chromium.org/driver/](https://sites.google.com/chromium.org/driver/)

3. Place the `chromedriver` in your system PATH or in the same directory as your script.

## 🚀 How to Run

```bash
python dollar_value_bot.py
```

You should see output like:

```
Current USD to BRL exchange rate: R$ 5.22
```

## 🛠️ Customization

To search for another currency pair (e.g., EUR to BRL or USD to ARS), simply change the text inside the `search_box.send_keys()` method:

```python
search_box.send_keys("EUR to BRL")
```

