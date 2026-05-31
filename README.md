# Spotify Music Streaming Analytics Platform

## Project Overview
This project demonstrates an end-to-end Azure Data Engineering pipeline using a public Spotify-style music dataset. The goal is to ingest raw music track data, process it through Bronze, Silver, and Gold layers, and create analytics-ready outputs for genre, artist, and track popularity analysis.

This project is designed for an Azure Data Engineer portfolio and interview explanation.

## Technology Stack
- Azure Data Factory
- Azure Data Lake Storage Gen2
- Azure Databricks
- PySpark
- Delta Lake
- SQL
- GitHub

## Dataset
Recommended public dataset:
- Kaggle: Spotify Tracks Dataset by Maharshi Pandya

For GitHub demo purposes, this repository also includes a small sample dataset:
`data/sample/spotify_tracks_sample.csv`

Use the sample data for testing the PySpark code locally or in Databricks. For a full project, download the Kaggle dataset and place it in the Bronze folder or `data/raw`.

## Architecture

```text
Spotify CSV Dataset / Source Files
        |
        v
Azure Data Factory
        |
        v
ADLS Gen2 - Bronze Layer
        |
        v
Azure Databricks - PySpark Transformations
        |
        v
ADLS Gen2 - Silver Delta Layer
        |
        v
Azure Databricks - Gold Aggregations
        |
        v
ADLS Gen2 - Gold Delta Layer
```

## Data Layers

### Bronze Layer
Stores raw source data as received.

### Silver Layer
Stores cleaned and standardized data after:
- removing duplicate tracks
- handling null values
- casting data types
- standardizing column names
- filtering invalid records

### Gold Layer
Stores analytics-ready outputs:
- genre popularity summary
- artist popularity summary
- top tracks by popularity

## Repository Structure

```text
spotify-music-streaming-analytics/
├── data/sample/
│   └── spotify_tracks_sample.csv
├── notebooks/
│   ├── 01_bronze_ingestion.py
│   ├── 02_silver_transformation.py
│   └── 03_gold_analytics.py
├── sql/
│   └── watermark_control.sql
├── adf/
│   └── adf_pipeline_design.md
├── architecture/
│   └── architecture_flow.md
├── docs/
│   ├── project_explanation.md
│   └── interview_questions.md
└── README.md
```

## How to Run in Azure Databricks

1. Create ADLS Gen2 folders:
   - bronze
   - silver
   - gold

2. Upload the Spotify CSV file into the Bronze layer.

3. Attach a Databricks cluster.

4. Run notebooks in this order:
   - `01_bronze_ingestion.py`
   - `02_silver_transformation.py`
   - `03_gold_analytics.py`

5. Validate Gold outputs:
   - genre summary
   - artist summary
   - top tracks


## Key Concepts Covered
- ADF ingestion design
- ADLS Gen2 folder structure
- Bronze, Silver, Gold architecture
- PySpark transformations
- Delta Lake storage
- Data validation
- Watermark-based incremental load concept
