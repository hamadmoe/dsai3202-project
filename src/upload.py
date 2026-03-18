from azure.storage.blob import BlobServiceClient
import os

CONNECT_STR = "PRIVATE"
CONTAINER_NAME = "traffic-data"
LOCAL_FOLDER = "data/features/"

def upload_files():
    blob_service_client = BlobServiceClient.from_connection_string(CONNECT_STR)

    for file_name in os.listdir(LOCAL_FOLDER):
        file_path = os.path.join(LOCAL_FOLDER, file_name)

        blob_client = blob_service_client.get_blob_client(
            container=CONTAINER_NAME,
            blob=file_name
        )

        with open(file_path, "rb") as data:
            blob_client.upload_blob(data, overwrite=True)

        print(f"Uploaded {file_name}")

if __name__ == "__main__":
    upload_files()