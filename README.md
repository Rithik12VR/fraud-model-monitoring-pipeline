# Fraud Model Monitoring Pipeline

Built a PySpark-based data engineering pipeline to simulate real-world fraud monitoring and analytics workflows.

---

## Problem Statement

In fraud detection systems, it's critical to monitor model behavior continuously.  
Metrics like Transaction Review Rate (TRR), score distribution, and high-risk patterns help detect model drift and performance issues.

This project simulates that pipeline.

---

## What this pipeline does

- Reads transaction data
- Performs data quality validation
- Calculates TRR (Transaction Review Rate)
- Generates fraud score bucket distribution
- Identifies high-risk transaction patterns
- Writes processed outputs for reporting

---

## Tech Stack

- Python 3.10
- PySpark (Spark 3.5)
- Pandas
- SQL
- Git / GitHub

---

## Pipeline Flow

1. Data ingestion from CSV
2. Data quality checks
3. Aggregations (TRR, score buckets)
4. High-risk transaction analysis
5. Output generation

---

## Output Generated

- Data Quality Report
- TRR Metrics
- Score Bucket Distribution
- High Risk Summary

---

## Key Learning

- Built end-to-end ETL pipeline using PySpark
- Debugged Spark + Hadoop issues on Windows
- Implemented aggregation logic similar to production systems
- Handled environment-level failures and resolved them

---

## How to Run

bash
pip install -r requirements.txt
python -m src.pipeline
