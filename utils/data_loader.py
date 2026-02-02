from pyspark.sql import SparkSession


def load_csv(path: str):
    spark = SparkSession.builder.getOrCreate()

    return (
        spark.read
        .option("header", True)
        .option("inferSchema", True)
        .csv(path)
    )