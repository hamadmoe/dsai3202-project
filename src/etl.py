import os
import pandas as pd
from tqdm import tqdm

INPUT_PATH = "data/raw/partitioned/"
OUTPUT_PATH = "data/processed/"

def clean_chunk(df):
    # Convert datetime columns
    df["tpep_pickup_datetime"] = pd.to_datetime(df["tpep_pickup_datetime"], errors="coerce")
    df["tpep_dropoff_datetime"] = pd.to_datetime(df["tpep_dropoff_datetime"], errors="coerce")

    # Drop rows with invalid timestamps
    df = df.dropna(subset=["tpep_pickup_datetime", "tpep_dropoff_datetime"])

    # Create trip duration (minutes)
    df["trip_duration"] = (
        (df["tpep_dropoff_datetime"] - df["tpep_pickup_datetime"])
        .dt.total_seconds() / 60
    )

    # Remove unrealistic durations
    df = df[(df["trip_duration"] > 1) & (df["trip_duration"] < 180)]

    # Remove invalid distances
    df = df[(df["trip_distance"] > 0) & (df["trip_distance"] < 100)]

    # Create average speed (mph)
    df["avg_speed"] = df["trip_distance"] / (df["trip_duration"] / 60)

    # Remove unrealistic speeds
    df = df[(df["avg_speed"] > 1) & (df["avg_speed"] < 100)]

    df = df.dropna(subset=[
    "pickup_longitude",
    "pickup_latitude",
    "dropoff_longitude",
    "dropoff_latitude"
    ])

    # Keep only relevant columns
    columns_to_keep = [
        "tpep_pickup_datetime",
        "tpep_dropoff_datetime",
        "trip_distance",
        "trip_duration",
        "avg_speed",
        "pickup_longitude",
        "pickup_latitude",
        "dropoff_longitude",
        "dropoff_latitude"
    ]

    df = df[columns_to_keep]

    return df


def run_etl():
    os.makedirs(OUTPUT_PATH, exist_ok=True)

    files = [f for f in os.listdir(INPUT_PATH) if f.endswith(".parquet")]

    print("Starting ETL process...")

    for i, file in enumerate(tqdm(files)):
        file_path = os.path.join(INPUT_PATH, file)

        df = pd.read_parquet(file_path)

        df_clean = clean_chunk(df)

        output_file = os.path.join(OUTPUT_PATH, f"clean_{i}.parquet")
        df_clean.to_parquet(output_file, index=False)

    print("ETL complete. Clean data saved.")


if __name__ == "__main__":
    run_etl()