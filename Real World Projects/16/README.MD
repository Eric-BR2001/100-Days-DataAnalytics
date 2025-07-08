# 📚 Word Frequency in *Moby Dick*

This project uses **web scraping** and **natural language processing (NLP)** techniques to identify the most frequent words in the classic novel *Moby Dick* by **Herman Melville**.

## 🧠 Objective

To answer the question:

> **What are the most frequent words in *Moby Dick*, and how often do they occur?**

By scraping a cached HTML version of the novel and processing the text, we uncover the top 10 most common non-stop words.

## 📥 Data Source

We use a cached HTML version of *Moby Dick* hosted on S3 (originally from [Project Gutenberg](https://www.gutenberg.org/)):

```
https://s3.amazonaws.com/assets.datacamp.com/production/project_147/datasets/2701-h.htm
```

## 🔧 Tools & Libraries

* `requests` – for HTTP requests
* `BeautifulSoup` – for HTML parsing
* `nltk` – for tokenization and stopword filtering
* `collections.Counter` – for word frequency counting
* `re` – for regex tokenization

## 🧪 Steps

1. **Request the HTML file**
   Use the `requests` library to retrieve the file and decode it as UTF-8.

2. **Parse the HTML content**
   Use `BeautifulSoup` with an HTML parser to extract the raw text from the HTML.

3. **Tokenize the text**
   Use `nltk.tokenize.RegexpTokenizer` to extract only alphanumeric words.

4. **Clean the text**

   * Convert all tokens to lowercase.
   * Remove English stop words using NLTK's stopword list.

5. **Analyze word frequency**
   Use Python’s `collections.Counter` to identify and print the top 10 most frequent words.