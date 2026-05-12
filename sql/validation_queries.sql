-- Validation 1: total row count
SELECT COUNT(*) AS total_transactions
FROM transactions;

-- Validation 2: duplicate transaction ids
SELECT transaction_id, COUNT(*) AS duplicate_count
FROM transactions
GROUP BY transaction_id
HAVING COUNT(*) > 1;

-- Validation 3: invalid fraud scores
SELECT *
FROM transactions
WHERE fraud_score < 0 OR fraud_score > 1;

-- Validation 4: transaction review rate by date and model
SELECT
    transaction_date,
    model_version,
    COUNT(*) AS total_transactions,
    SUM(review_flag) AS reviewed_transactions,
    ROUND(SUM(review_flag) * 1.0 / COUNT(*), 4) AS trr
FROM transactions
GROUP BY transaction_date, model_version
ORDER BY transaction_date, model_version;

-- Validation 5: high-risk transactions by region
SELECT
    region,
    COUNT(*) AS total_transactions,
    SUM(CASE WHEN fraud_score >= 0.70 THEN 1 ELSE 0 END) AS high_risk_transactions
FROM transactions
GROUP BY region
ORDER BY high_risk_transactions DESC;
