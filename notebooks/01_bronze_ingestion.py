# Databricks Notebook: 01 Bronze Ingestion
# Purpose: Read raw Spotify CSV data and store it as Bronze Delta table.

from pyspark.sql.functions import current_timestamp

# Update these paths as per your ADLS mount or abfss path
source_path = "/mnt/bronze/spotify/spotify_tracks.csv"
bronze_delta_path = "/mnt/bronze/spotify_delta"

raw_df = (
    spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv(source_path)
)

bronze_df = raw_df.withColumn("ingestion_timestamp", current_timestamp())

bronze_df.write.format("delta").mode("overwrite").save(bronze_delta_path)

display(bronze_df.limit(10))
