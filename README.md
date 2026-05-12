# Fraud Model Monitoring Pipeline

A PySpark-based data pipeline built to mimic how fraud monitoring systems track model behavior in real-world payment platforms.

This project focuses on computing key monitoring metrics like TRR (Transaction Review Rate), score distribution, and high-risk patterns, outputs typically consumed by fraud analytics and risk teams.

---

## Why this project

In production fraud systems, models don’t just run, they are continuously monitored.

Small shifts in score distribution or review rates can indicate:

* model drift
* data quality issues
* unexpected traffic patterns

This pipeline represents a simplified version of that monitoring layer.

---

## What the pipeline does

* Reads transaction-level data from CSV
* Runs data quality checks
* Computes TRR (Transaction Review Rate)
* Builds fraud score bucket distributions
* Generates high-risk transaction summaries
* Writes outputs as report-ready datasets

---

## Tech Stack

* Python 3.10
* PySpark (Spark 3.5)
* Pandas (for local output handling)
* SQL (validation queries)
* Git / GitHub

---

## Data Schema (Sample)

| Column           | Description                    |
| ---------------- | ------------------------------ |
| transaction_id   | Unique transaction identifier  |
| transaction_date | Date of transaction            |
| model_version    | Fraud model version            |
| fraud_score      | Model score (0–1)              |
| review_flag      | 1 if flagged for manual review |
| region           | Transaction region             |

---

## Pipeline Flow

```
Raw CSV Data
     ↓
Data Quality Checks
     ↓
Transformations (TRR, Score Buckets)
     ↓
Aggregations (High Risk Summary)
     ↓
Output Reports (CSV)
---

## Sample Output

### TRR Results

| transaction_date | model_version | total_transactions | reviewed_transactions | trr  |
| ---------------- | ------------- | ------------------ | --------------------- | ---- |
| 2024-01-01       | v1            | 1000               | 120                   | 0.12 |

### High Risk Summary

| transaction_date | region | high_risk_rate |
| ---------------- | ------ | -------------- |
| 2024-01-01       | US     | 0.08           |

---

## What I focused on

This project goes beyond basic transformations.

Key areas I worked through:

* Setting up Spark locally on Windows
* Debugging Spark session and worker issues
* Handling Hadoop / winutils dependency problems
* Fixing Python environment conflicts with PySpark
* Designing aggregation logic for monitoring metrics

These are the kinds of issues that typically show up in real-world data engineering environments.
---
## How to run
```
pip install -r requirements.txt
python -m src.pipeline
```
Outputs will be generated in:
data/output/
```
## Author

Rithik V
Senior Data Engineer
