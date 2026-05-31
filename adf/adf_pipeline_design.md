# ADF Pipeline Design

## Pipeline Name
PL_SPOTIFY_TRACKS_INGESTION

## Purpose
To ingest Spotify track data from source storage into the ADLS Gen2 Bronze layer and trigger Databricks notebooks for transformation.

## Activities Used

### 1. Get Metadata Activity
Used to check whether the source file is available.

### 2. Copy Activity
Used to copy the raw Spotify CSV file into the ADLS Bronze layer.

### 3. Databricks Notebook Activity
Used to trigger the Bronze, Silver, and Gold transformation notebooks.

### 4. Failure Path
Used to capture failure details and support troubleshooting.

## Pipeline Flow

```text
Get Metadata
    |
    v
Copy Activity
    |
    v
Databricks Bronze Notebook
    |
    v
Databricks Silver Notebook
    |
    v
Databricks Gold Notebook
```

## Source
Public Spotify CSV dataset.

## Sink
ADLS Gen2 Bronze folder.

## Notes
In a real production scenario, this pipeline can be parameterized to process multiple files or datasets dynamically.
