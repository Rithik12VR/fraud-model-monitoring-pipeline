from pyspark.sql import DataFrame
from pyspark.sql import functions as F


def run_data_quality_checks(df: DataFrame) -> DataFrame:
    total_rows = df.count()
    null_transaction_ids = df.filter(F.col("transaction_id").isNull()).count()
    null_dates = df.filter(F.col("transaction_date").isNull()).count()
    null_model_versions = df.filter(F.col("model_version").isNull()).count()
    invalid_scores = df.filter((F.col("fraud_score") < 0) | (F.col("fraud_score") > 1)).count()

    duplicate_transaction_ids = (
        df.groupBy("transaction_id")
        .count()
        .filter(F.col("count") > 1)
        .count()
    )

    results = [
        ("total_rows", total_rows),
        ("null_transaction_ids", null_transaction_ids),
        ("null_dates", null_dates),
        ("null_model_versions", null_model_versions),
        ("invalid_scores", invalid_scores),
        ("duplicate_transaction_ids", duplicate_transaction_ids),
    ]

    return df.sparkSession.createDataFrame(results, ["check_name", "check_value"])
