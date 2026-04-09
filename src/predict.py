from azure.storage.blob import BlobServiceClient
import pandas as pd
import joblib
import os

CONNECT_STR = "connection_string_of_traffic1project"

CONTAINER_NAME = "curated"
MODEL_PATH = "models/model.pkl"
DOWNLOAD_PATH = "temp_data/"

def download_data():
    os.makedirs(DOWNLOAD_PATH, exist_ok=True)

    blob_service_client = BlobServiceClient.from_connection_string(CONNECT_STR)
    container_client = blob_service_client.get_container_client(CONTAINER_NAME)

    print("Downloading files from Azure...")

    blobs = container_client.list_blobs()

    files = []
    for blob in blobs:
        if blob.name.endswith(".parquet"):
            file_path = os.path.join(DOWNLOAD_PATH, blob.name)

            with open(file_path, "wb") as f:
                f.write(container_client.download_blob(blob.name).readall())

            files.append(file_path)

            # limit for speed
            if len(files) >= 5:
                break

    return files


def load_data(files):
    df_list = [pd.read_parquet(f) for f in files]
    return pd.concat(df_list, ignore_index=True)


def run_prediction():
    print("Loading model...")
    model = joblib.load(MODEL_PATH)

    files = download_data()

    print("Loading data...")
    df = load_data(files)

    X = df[["trip_distance", "hour", "day_of_week"]]

    print("Running predictions...")
    preds = model.predict(X)

    df["predicted_congestion"] = preds

    print(df[["trip_distance", "hour", "predicted_congestion"]].head(10))

    upload_predictions(df)

def upload_predictions(df):
    blob_service_client = BlobServiceClient.from_connection_string(CONNECT_STR)
    container_client = blob_service_client.get_container_client("predictions")

    output_file = "predictions.parquet"
    df.to_parquet(output_file, index=False)

    with open(output_file, "rb") as data:
        container_client.upload_blob(name=output_file, data=data, overwrite=True)

    print("Predictions uploaded to Azure.")

if __name__ == "__main__":
    run_prediction()