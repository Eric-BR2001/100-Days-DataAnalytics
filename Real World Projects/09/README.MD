# 📈 Finding Exchange Rates for International Sales

This project demonstrates how to integrate real-time exchange rate data into an existing sales dataset using the [VATComply API](https://www.vatcomply.com/). The goal is to convert all sales to USD based on exchange rates from a specific date.

## 🧾 Project Overview

We use the VAT Comply Exchange Rates API to gather currency conversion data and apply it to an existing sales orders DataFrame. This allows for consistent reporting of international sales in a single base currency (USD).

## 🛠️ Features

* Queries exchange rates for a base currency of **USD** on the date **2024-01-21**.
* Reads an existing orders dataset containing multiple currencies.
* Converts all order totals to **USD** using real-time exchange rates.
* Calculates and stores the **total USD sales**.
* Ensures the final orders DataFrame matches predefined requirements (as per provided workbook).

## 🔗 API Information

* **Endpoint**: `https://api.vatcomply.com/rates`
* **Parameters**:

  * `base=USD`
  * `date=2024-01-21`
* **Authentication**: None required
* **Documentation**: [https://www.vatcomply.com/](https://www.vatcomply.com/)