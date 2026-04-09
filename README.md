# Cloud-Based Traffic Congestion Prediction System

## Project Overview
This project implements a cloud-based data pipeline and machine learning system for predicting traffic congestion using large-scale NYC Yellow Taxi trip data. The system covers the full AI lifecycle: data ingestion, ETL, feature engineering, model training, validation, and cloud deployment on Microsoft Azure.

---

## Tech Stack
- Python (pandas, numpy, scikit-learn)
- VS Code
- Microsoft Azure Blob Storage
- Parquet data format

---

## Data Source
- NYC Yellow Taxi Trip Data (Kaggle)
- Dataset size: ~1.7GB
- Batch ingestion strategy used

---

## Pipeline Architecture

Raw Data (CSV)  
↓  
Ingestion (Chunk Processing)  
↓  
Bronze Layer (Parquet) → Azure Container: `raw`  
↓  
ETL Pipeline  
↓  
Silver Layer (Clean Data) → Azure Container: `processed`  
↓  
Feature Engineering  
↓  
Gold Layer (ML-ready Data) → Azure Container: `curated`  
↓  
Model Training & Validation  
↓  
Batch Prediction Pipeline  
↓  
Predictions stored in Azure Container: `predictions`

---

## 1. Data Ingestion
- Implemented batch ingestion using chunk processing
- Converted CSV into partitioned Parquet files
- Ensured scalability for large datasets
- Raw data preserved in Bronze layer

---

## 2. ETL Process
- Cleaned missing and invalid data
- Converted timestamp fields
- Removed unrealistic trips (duration, distance, speed)
- Created derived features:
  - Trip duration
  - Average speed

---

## 3. Data Organization & Governance
- Implemented a multi-layer Azure storage architecture:
  - `raw` (Bronze)
  - `processed` (Silver)
  - `curated` (Gold)
- Ensured clear data lineage and separation of concerns
- All transformations are reproducible

---

## 4. Exploratory Data Analysis
- Analyzed distributions of key variables:
  - Trip duration
  - Average speed
- Evaluated congestion patterns over time
- Verified data quality and readiness for modeling

---

## 5. Feature Engineering
- Extracted time-based features:
  - Hour of day
  - Day of week
- Defined congestion levels based on speed:
  - High (<10 mph)
  - Medium (10–25 mph)
  - Low (>25 mph)
- Avoided data leakage by excluding derived features (avg_speed, trip_duration) from training
- Created ML-ready dataset

---

## 6. Model Development

### Baseline Model:
- Logistic Regression

### Main Model:
- Random Forest Classifier

- Features used:
  - `trip_distance`
  - `hour`
  - `day_of_week`

- Reproducibility ensured through fixed random seeds and consistent preprocessing

---

## 7. Model Evaluation

- Final Random Forest performance:
  - Accuracy: ~74%

### Key Observations:
- High congestion detected with strong recall (~0.85)
- Medium congestion moderately predicted
- Low congestion harder to detect due to overlapping patterns

### Important Insight:
- Initial models showed unrealistically high performance due to data leakage
- This was resolved by removing features used to derive the target variable

---

## 8. Model Optimization

- Hyperparameter tuning was explored for Random Forest and Logistic Regression
- More complex configurations did not improve performance significantly
- Demonstrated that:
  - Simpler models can outperform over-tuned configurations
  - Feature quality is more impactful than aggressive tuning

---

## 9. Model Versioning

- Model saved as:
  - `models/model.pkl`

- Metadata stored:
  - Model type
  - Features used
  - Performance metrics
  - Notes on design decisions

---

## 10. Azure Deployment

- Data stored across containers:
  - `raw` (Bronze)
  - `processed` (Silver)
  - `curated` (Gold)

- Model deployed using batch inference approach

---

## 11. Batch Prediction Pipeline

A batch pipeline was implemented:

1. Retrieve data from Azure `curated` container  
2. Apply trained model  
3. Generate predictions  
4. Upload results to Azure `predictions` container  

---

## 12. Deployment Validation

- Predictions were successfully generated using cloud data
- Outputs were validated through sanity checks
- Model behavior aligned with real-world expectations
- Consistency confirmed between offline and deployed predictions

---

## Project Structure

dsai3202-project/  
│  
├── data/  
│   ├── raw/  
│   ├── processed/  
│   └── features/  
│  
├── src/  
│   ├── ingestion.py  
│   ├── etl.py  
│   ├── features.py  
│   ├── train.py  
│   ├── evaluate.py  
│   ├── predict.py  
│   ├── predict_from_azure.py  
│   ├── batch_pipeline.py  
│  
├── models/  
│   ├── model.pkl  
│   └── metadata/  
│  
├── notebooks/  
│   └── eda.ipynb  
│  
├── config/  
│   └── schema.json  
│  
├── README.md  
└── requirements.txt  

---

## Important Notes
- Due to dataset size (~1.7GB), raw data is not stored in GitHub
- Data is handled locally and through Azure Blob Storage
- All pipelines are reproducible via provided scripts

---