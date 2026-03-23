# Cloud-Based Traffic Congestion Prediction System

##  Project Overview
This project implements a cloud-based data pipeline for predicting traffic congestion using large-scale NYC Yellow Taxi trip data. The system processes raw trip data, performs ETL operations, extracts meaningful features, and prepares the dataset for machine learning applications.

---

## Tech Stack
- Python (pandas, numpy)
- VS Code
- Microsoft Azure Blob Storage
- Parquet data format

---

##  Data Source
- NYC Yellow Taxi Trip Data (Kaggle)
- Dataset size: ~1.7GB
- Batch ingestion strategy used

---

## Pipeline Architecture

Raw Data (CSV)--> Ingestion (Chunk Processing) --> Bronze Layer (Parquet) --> ETL Pipeline --> Silver Layer (Clean Data) --> Feature Engineering --> Gold Layer (ML-ready Data) --> Azure Blob Storage

---

##  1. Data Ingestion
- Implemented batch ingestion using chunk processing
- Converted CSV into partitioned Parquet files
- Ensured scalability for large datasets
- Raw data preserved locally (Bronze layer)

---

##  2. ETL Process
- Cleaned missing and invalid data
- Converted timestamp fields
- Removed unrealistic trips (duration, distance, speed)
- Created derived features:
  - Trip duration
  - Average speed

---

##  3. Data Organization & Governance
- Data structured into:
  - `data/raw/` (Bronze)
  - `data/processed/` (Silver)
  - `data/features/` (Gold)
- Schema consistency maintained across pipeline
- Transformations are fully reproducible

---

##  4. Exploratory Data Analysis
- Analyzed distributions of key variables:
  - Trip duration
  - Average speed
- Evaluated congestion patterns over time
- Verified data quality and readiness

---

##  5. Feature Engineering
- Extracted time-based features:
  - Hour of day
  - Day of week
- Defined congestion levels based on speed:
  - High (<10 mph)
  - Medium (10–25 mph)
  - Low (>25 mph)
- Created ML-ready dataset

---

##  Azure Deployment
- Uploaded raw, processed, and curated data to Azure Blob Storage
- Implemented cloud-based storage architecture
- Ensured separation of code and data



## IMPORTANT NOTE!
- Because of the huge size of the dataset, raw data was not uploaded to the repo
- Data is handled locally and thorugh the cloud blob storage
