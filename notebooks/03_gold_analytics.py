# Databricks Notebook: 03 Gold Analytics
# Purpose: Create analytics-ready Gold datasets.

from pyspark.sql.functions import col, avg, count, round

silver_delta_path = "/mnt/silver/spotify_tracks"

gold_genre_path = "/mnt/gold/genre_popularity_summary"
gold_artist_path = "/mnt/gold/artist_popularity_summary"
gold_top_tracks_path = "/mnt/gold/top_tracks"

silver_df = spark.read.format("delta").load(silver_delta_path)

genre_summary_df = (
    silver_df
    .groupBy("genre")
    .agg(
        count("track_id").alias("total_tracks"),
        round(avg("popularity"), 2).alias("avg_popularity"),
        round(avg("danceability"), 2).alias("avg_danceability"),
        round(avg("energy"), 2).alias("avg_energy")
    )
    .orderBy(col("avg_popularity").desc())
)

genre_summary_df.write.format("delta").mode("overwrite").save(gold_genre_path)

artist_summary_df = (
    silver_df
    .groupBy("artist_name")
    .agg(
        count("track_id").alias("total_tracks"),
        round(avg("popularity"), 2).alias("avg_popularity")
    )
    .orderBy(col("avg_popularity").desc())
)

artist_summary_df.write.format("delta").mode("overwrite").save(gold_artist_path)

top_tracks_df = (
    silver_df
    .select("track_id", "track_name", "artist_name", "genre", "popularity", "duration_ms")
    .orderBy(col("popularity").desc())
)

top_tracks_df.write.format("delta").mode("overwrite").save(gold_top_tracks_path)

display(genre_summary_df)
display(artist_summary_df.limit(20))
display(top_tracks_df.limit(20))
