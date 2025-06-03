# 🌍 Daily Top 5 World News Logger

This Python project automatically fetches and logs the top 5 world news headlines from **Reuters** using their free RSS feed. Each time you run the script, it adds the latest headlines to this file with timestamps, helping you build a historical log of major world events.

---

## 📰 Features

- ✅ No API key required (uses public RSS feed)
- 🌐 Global news from Reuters
- 🕒 Automatically timestamps each entry
- 📁 Logs stored directly in this `README.md`
- ⚙️ Easy to automate via cron (Linux/macOS) or Task Scheduler (Windows)

---

## 📂 Project Structure

```

top\_news/
├── top\_news.py       # Python script to fetch and log news
└── README.md         # This file – stores instructions and logged headlines

````

---

## 🚀 Getting Started

### 1. Clone or Download the Repo

```bash
git clone https://github.com/your-username/top-news-logger.git
cd top-news-logger
````

### 2. Install Required Package

We use [`feedparser`](https://pypi.org/project/feedparser/) to handle RSS:

```bash
pip install feedparser
```

### 3. Run the Script

```bash
python top_news.py
```

> This will append the latest 5 world news headlines from Reuters into `README.md`.

---

## 🔄 Automate Daily Execution

### On Linux/macOS (Using `cron`)

1. Open your crontab:

   ```bash
   crontab -e
   ```

2. Add this line to run the script every day at 9 AM:

   ```
   0 9 * * * /usr/bin/python3 /absolute/path/to/top_news.py
   ```

✅ Replace `/usr/bin/python3` and `/absolute/path/to/top_news.py` with your actual Python and script paths. You can find your Python path with:

```bash
which python3
```

---

### On Windows (Using Task Scheduler)

1. Open **Task Scheduler**.
2. Click **Create Basic Task**.
3. Name it e.g. `TopNewsDaily`.
4. Trigger: **Daily**, set time.
5. Action: **Start a program**

   * Program: `python`
   * Arguments: `"C:\full\path\to\top_news.py"`
6. Finish setup.

---

## ✅ Sample Output

```
## 🗓️ 2025-06-02 09:00:00 - Top 5 World News from Reuters

1. [G7 leaders agree on AI rules for military use](https://www.reuters.com/some-link)
2. [UN calls for ceasefire in Gaza after new bombings](https://www.reuters.com/some-link)
3. [China, Russia hold joint drills in Pacific](https://www.reuters.com/some-link)
4. [France moves to dissolve National Assembly](https://www.reuters.com/some-link)
5. [Brazil faces new wave of Amazon deforestation](https://www.reuters.com/some-link)

---
```
