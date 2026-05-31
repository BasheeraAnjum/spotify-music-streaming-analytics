# Interview Questions and Answers

## 1. Explain this project end to end.
This project processes Spotify track data using Azure services. ADF ingests raw CSV data into ADLS Bronze layer. Databricks PySpark notebooks clean and standardize the data into Silver layer. Gold layer datasets are created for genre popularity, artist summaries, and top track analysis.

## 2. What is the Bronze layer?
Bronze layer stores raw data as received from source without business transformations.

## 3. What is the Silver layer?
Silver layer stores cleaned and standardized data after handling duplicates, null values, data types, and invalid records.

## 4. What is the Gold layer?
Gold layer stores curated analytics-ready datasets used for reporting and analysis.

## 5. Why did you use PySpark?
PySpark is useful for distributed data processing and transformations such as cleansing, deduplication, filtering, and aggregations.

## 6. What transformations did you perform?
I removed duplicates, handled nulls, standardized text columns, casted data types, filtered invalid records, and created summary datasets.

## 7. What is incremental loading?
Incremental loading means processing only new or updated records instead of loading the complete dataset every time.

## 8. How did you validate data?
I performed duplicate checks, null checks, valid popularity range checks, and row count validations between layers.

## 9. Why did you use Delta Lake?
Delta Lake provides reliable storage and supports structured data processing on ADLS.

## 10. How would you enhance this project?
I would add automated ADF scheduling, parameterized pipelines, more data quality checks, and GitHub documentation with screenshots.
