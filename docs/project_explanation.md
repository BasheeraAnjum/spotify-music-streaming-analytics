# Project Explanation for Interview

## Short Explanation
This project is a Spotify Music Streaming Analytics pipeline built using Azure Data Factory, ADLS Gen2, Azure Databricks, PySpark, and Delta Lake. The project processes public Spotify track data and prepares curated datasets for music analytics.

## End-to-End Flow
1. Source data is available as a Spotify CSV dataset.
2. ADF ingests the CSV into the ADLS Bronze layer.
3. Databricks reads Bronze data and performs cleansing and standardization.
4. Clean data is stored in the Silver Delta layer.
5. Gold datasets are created for genre popularity, artist summaries, and top tracks.
6. Data quality checks are performed to validate duplicate, null, and invalid records.

## Why Bronze, Silver, Gold?
Bronze stores raw data, Silver stores cleaned data, and Gold stores business-ready analytical datasets.

## Why Databricks?
Databricks is used for scalable PySpark transformations such as cleansing, deduplication, filtering, joins, and aggregations.

## Why Delta Lake?
Delta Lake provides reliable storage, schema handling, and efficient data processing on top of ADLS.
