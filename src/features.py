import os
import pandas as pd
from tqdm import tqdm

INPUT_PATH = "data/processed/"
OUTPUT_PATH = "data/features/"

def add_features(df):
    # Extract time features
    df["hour"] = df["tpep_pickup_datetime"].dt.hour
    df["day_of_week"] = df["tpep_pickup_datetime"].dt.dayofweek

    # Create congestion level based on speed
    def congestion_label(speed):
        if speed < 10:
            return "HIGH"
        elif speed < 25:
            return "MEDIUM"
        else:
            return "LOW"

    df["congestion_level"] = df["avg_speed"].apply(congestion_label)

    return df


def run_feature_engineering():
    os.makedirs(OUTPUT_PATH, exist_ok=True)

    files = [f for f in os.listdir(INPUT_PATH) if f.endswith(".parquet")]

    print("Starting feature engineering...")

    for i, file in enumerate(tqdm(files)):
        file_path = os.path.join(INPUT_PATH, file)

        df = pd.read_parquet(file_path)

        df_features = add_features(df)

        output_file = os.path.join(OUTPUT_PATH, f"features_{i}.parquet")
        df_features.to_parquet(output_file, index=False)

    print("Feature engineering complete.")


if __name__ == "__main__":
    run_feature_engineering()