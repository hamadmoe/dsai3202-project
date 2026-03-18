import os
import pandas as pd
from tqdm import tqdm

RAW_DATA_PATH = "data/raw/yellow_tripdata.csv"
OUTPUT_PATH = "data/raw/partitioned/"

CHUNK_SIZE = 100_000

def ingest_data():
    os.makedirs(OUTPUT_PATH, exist_ok=True)

    print("Starting data ingestion...")

    chunk_iter = pd.read_csv(RAW_DATA_PATH, chunksize=CHUNK_SIZE)

    for i, chunk in enumerate(tqdm(chunk_iter)):
        chunk.drop_duplicates(inplace=True)

        output_file = os.path.join(OUTPUT_PATH, f"chunk_{i}.parquet")
        chunk.to_parquet(output_file, index=False)

    print("Ingestion complete.")

if __name__ == "__main__":
    ingest_data()