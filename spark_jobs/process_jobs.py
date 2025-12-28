from pyspark.sql import SparkSession

def main():
    """
    Process job postings data using Spark
    """
    spark = SparkSession.builder.appName("Job Market Intelligence").getOrCreate()
    print("Spark session created")

    raw_jobs_path = "data/raw/jobs/"

    df = spark.read.option("header", "true").csv(raw_jobs_path)
    df.printSchema()
    print(f"Raw jobs data loaded with {df.count()} rows")

    spark.stop()
    print("Spark session stopped")
    print("Job completed successfully")

if __name__ == "__main__":
    main()