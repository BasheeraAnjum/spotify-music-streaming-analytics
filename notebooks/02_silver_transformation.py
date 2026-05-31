# Databricks Notebook: 02 Silver Transformation
# Purpose: Clean and standardize Spotify track data.

from pyspark.sql.functions import col, trim, lower, current_timestamp

bronze_delta_path = "/mnt/bronze/spotify_delta"
silver_delta_path = "/mnt/silver/spotify_tracks"

bronze_df = spark.read.format("delta").load(bronze_delta_path)

silver_df = (
    bronze_df
    .withColumn("track_name", trim(col("track_name")))
    .withColumn("artist_name", trim(col("artist_name")))
    .withColumn("album_name", trim(col("album_name")))
    .withColumn("genre", lower(trim(col("genre"))))
    .withColumn("popularity", col("popularity").cast("int"))
    .withColumn("duration_ms", col("duration_ms").cast("int"))
    .withColumn("danceability", col("danceability").cast("double"))
    .withColumn("energy", col("energy").cast("double"))
    .dropDuplicates(["track_id"])
    .filter(col("track_id").isNotNull())
    .filter(col("track_name").isNotNull())
    .filter(col("artist_name").isNotNull())
    .filter(col("popularity").between(0, 100))
    .filter(col("duration_ms") > 0)
    .withColumn("silver_updated_timestamp", current_timestamp())
)

silver_df.write.format("delta").mode("overwrite").save(silver_delta_path)

display(silver_df.limit(10))
