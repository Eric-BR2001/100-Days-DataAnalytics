# Detecting Anomalous Transactions

Dive into the world of banking transactions to uncover hidden anomalies and protect customer confidence. Ready to take on the challenge?

## Objective

Explore the `transactions.csv` dataset and use data analysis techniques to discover the potential for fraud by focusing on anomalies.

## Tasks

1. **Compute Anomaly Scores**  
   Calculate an anomaly score for each transaction.  
   - Add a new column to the `transactions` DataFrame named `Anomaly_Score`.

2. **Flag Anomalies**  
   Identify which transactions are anomalous.  
   - Add a boolean column named `Anomaly` where `True` indicates an anomalous transaction.

3. **Create Anomalies Summary**  
   Generate a summary DataFrame named `anomalies_summary` containing:
   - `TransactionID`
   - `TransactionAmount`
   - `TransactionDuration`
   - `AccountBalance`

4. **Visualize Anomaly Distribution**  
   Analyze the distribution of transaction amounts for both normal and anomalous transactions.  
   - Generate and save a histogram as `anomalies_histogram.png`
   - Visualize both groups using distinct colors to highlight any differences.

## Deliverables

- A modified `transactions` DataFrame with `Anomaly_Score` and `Anomaly` columns.
- A `pandas` DataFrame named `anomalies_summary`.
- A histogram saved as `anomalies_histogram.png` comparing `TransactionAmount` for anomalous vs. normal transactions.

