# Architecture Flow

```text
Public Spotify Dataset
        |
        v
Azure Data Factory
        |
        v
ADLS Gen2 Bronze
        |
        v
Azure Databricks PySpark
        |
        v
ADLS Gen2 Silver Delta
        |
        v
Azure Databricks Aggregations
        |
        v
ADLS Gen2 Gold Delta
```

## Bronze
Raw Spotify track data.

## Silver
Cleaned and standardized music metadata.

## Gold
Analytics-ready datasets:
- Genre popularity summary
- Artist popularity summary
- Top tracks analysis
