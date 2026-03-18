# Cloud-Based Traffic Congestion Prediction System

## Project Overview
This project aims to build a cloud-based data pipeline for predicting traffic congestion using large-scale NYC taxi trip data.

## Tech Stack
- Python (pandas, numpy)
- VS Code
- Microsoft Azure (planned)

## Data Source
NYC Yellow Taxi Trip Data (Kaggle)

## Pipeline Overview
1. Data Ingestion (Batch processing, CSV → Parquet)
2. ETL (Data cleaning and transformation)
3. Feature Engineering (Extracted time-based features (hour, day of week), Created congestion level target variable based on average speed)
4. EDA:
- Analyzed feature distributions (speed, duration)
- Checked congestion level balance
- Validated relationships between variables
- Confirmed dataset readiness for modeling
5. Deployment on Azure (Upcoming)

## Current Progress
- [x] Project setup
- [x] Data ingestion pipeline
- [x] ETL pipeline
- [x] Feature engineering
- [x] EDA
- [ ] Azure deployment