# Fraud Model Monitoring Data Pipeline

A practical data engineering project that simulates fraud model monitoring for payment transactions.

The pipeline reads transaction-level fraud scoring data, computes Transaction Review Rate (TRR), detects population drift using PSI, runs data quality checks, and produces monitoring outputs that can be used by dashboards or alerting systems.

This project is intentionally built around real data engineering concepts used in enterprise fraud and risk systems:

- Batch processing with PySpark
- SQL-based validation queries
- Data quality checks
- Model monitoring metrics
- Partitioned output design
- Clean project structure
- GitHub-ready documentation

---

## Business Problem

Fraud models score payment transactions in real time. Over time, model behavior can change because of new transaction patterns, model refreshes, data quality issues, or upstream pipeline failures.

This pipeline helps monitor whether fraud model output is stable by calculating:

- Transaction Review Rate (TRR): percentage of transactions flagged for review
- Population Stability Index (PSI): detects drift between baseline and current score distributions
- Data quality results: null checks, duplicate checks, and invalid score checks

---

## Tech Stack

- Python 3.10+
- PySpark 3.x
- SQL
- Parquet-style output design
- Git / GitHub
- Optional dashboard layer: Splunk, Qlik, Power BI

---

## Project Structure

```text
fraud-model-monitoring-pipeline/
├── data/
│   ├── input/
│   │   └── transactions.csv
│   └── output/
├── docs/
│   └── linkedin_post.md
├── sql/
│   └── validation_queries.sql
├── src/
│   ├── config.py
│   ├── data_quality.py
│   ├── pipeline.py
│   └── psi.py
├── tests/
│   └── test_psi.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Input Data

Sample input table: `transactions.csv`

| column | description |
|---|---|
| transaction_id | unique payment transaction id |
| transaction_date | transaction date |
| customer_id | customer identifier |
| merchant_id | merchant identifier |
| amount | transaction amount |
| fraud_score | model score between 0 and 1 |
| review_flag | 1 if transaction is sent for review, else 0 |
| model_version | fraud model version |
| region | transaction region |

---

## Metrics Produced

### 1. Transaction Review Rate

```text
TRR = reviewed transactions / total transactions
```

Example output:

| transaction_date | model_version | total_transactions | reviewed_transactions | trr |
|---|---:|---:|---:|---:|
| 2026-05-01 | model_v1 | 5 | 2 | 0.40 |

---

### 2. PSI

PSI compares current fraud score distribution with baseline distribution.

High PSI means the model input or score distribution has shifted.

General interpretation:

| PSI value | meaning |
|---:|---|
| < 0.10 | stable |
| 0.10 - 0.25 | moderate drift |
| > 0.25 | significant drift |

---

### 3. Data Quality Checks

The pipeline checks for:

- null transaction ids
- duplicate transaction ids
- fraud scores outside 0 to 1
- missing model versions
- missing transaction dates

---

## How to Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Run pipeline

```bash
spark-submit src/pipeline.py
```

For local development:

```bash
python src/pipeline.py
```

---

## SQL Validation

Sample validation queries are available in:

```text
sql/validation_queries.sql
```

These queries can be used to validate row counts, TRR, duplicates, and score quality.

---

## Why This Project Matters

This project demonstrates practical data engineering skills beyond basic ETL:

- Building reliable data pipelines
- Monitoring fraud model behavior
- Writing reusable PySpark code
- Validating data quality
- Producing business-facing metrics
- Creating outputs suitable for dashboards and alerts

---

## Future Improvements

- Add Kafka streaming input
- Write outputs to Delta Lake or Iceberg
- Add Airflow orchestration
- Add Docker support
- Add dashboard screenshots
- Add CI/CD pipeline using GitHub Actions
