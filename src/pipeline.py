from pyspark.sql import SparkSession
from pyspark.sql import functions as F

from src.config import INPUT_PATH, OUTPUT_DIR, REVIEW_THRESHOLD
from src.data_quality import run_data_quality_checks


def create_spark_session() -> SparkSession:
    return (
        SparkSession.builder
        .appName("Fraud Monitoring Pipeline")
        .master("local[*]")
        .config("spark.driver.host", "127.0.0.1")
        .config("spark.driver.bindAddress", "127.0.0.1")
        .config("spark.ui.enabled", "false")
        .getOrCreate()
    )


def read_transactions(spark: SparkSession):
    return (
        spark.read
        .option("header", True)
        .option("inferSchema", True)
        .csv(str(INPUT_PATH))
    )


def calculate_trr(df):
    return (
        df.groupBy("transaction_date", "model_version")
        .agg(
            F.count("*").alias("total_transactions"),
            F.sum("review_flag").alias("reviewed_transactions"),
            F.avg("fraud_score").alias("avg_fraud_score"),
        )
        .withColumn(
            "trr",
            F.round(F.col("reviewed_transactions") / F.col("total_transactions"), 4),
        )
        .orderBy("transaction_date", "model_version")
    )


def calculate_score_buckets(df):
    return (
        df.withColumn(
            "score_bucket",
            F.when(F.col("fraud_score") < 0.2, "0.0-0.2")
            .when(F.col("fraud_score") < 0.4, "0.2-0.4")
            .when(F.col("fraud_score") < 0.6, "0.4-0.6")
            .when(F.col("fraud_score") < 0.8, "0.6-0.8")
            .otherwise("0.8-1.0"),
        )
        .groupBy("model_version", "score_bucket")
        .agg(F.count("*").alias("transaction_count"))
        .orderBy("model_version", "score_bucket")
    )


def calculate_high_risk_summary(df):
    return (
        df.withColumn("is_high_risk", F.when(F.col("fraud_score") >= REVIEW_THRESHOLD, 1).otherwise(0))
        .groupBy("transaction_date", "region")
        .agg(
            F.count("*").alias("total_transactions"),
            F.sum("is_high_risk").alias("high_risk_transactions"),
        )
        .withColumn(
            "high_risk_rate",
            F.round(F.col("high_risk_transactions") / F.col("total_transactions"), 4),
        )
        .orderBy("transaction_date", "region")
    )


def write_output(df, name: str):
    output_path = OUTPUT_DIR / name

    # convert to pandas to avoid Hadoop native dependency
    pdf = df.toPandas()

    output_path.mkdir(parents=True, exist_ok=True)

    file_path = output_path / f"{name}.csv"
    pdf.to_csv(file_path, index=False)

    print(f"{name} written to {file_path}")


def main():
    spark = create_spark_session()

    transactions = read_transactions(spark)

    dq_results = run_data_quality_checks(transactions)
    trr_results = calculate_trr(transactions)
    score_buckets = calculate_score_buckets(transactions)
    high_risk_summary = calculate_high_risk_summary(transactions)

    write_output(dq_results, "data_quality_results")
    write_output(trr_results, "trr_results")
    write_output(score_buckets, "score_bucket_distribution")
    write_output(high_risk_summary, "high_risk_summary")

    print("Pipeline completed successfully")
    print(f"Output written to: {OUTPUT_DIR}")

    spark.stop()


if __name__ == "__main__":
    main()
