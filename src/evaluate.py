import os
import pandas as pd
import joblib
from sklearn.metrics import confusion_matrix, classification_report
import matplotlib.pyplot as plt
import seaborn as sns

DATA_PATH = "data/features/"
MODEL_PATH = "models/model.pkl"

def load_data():
    files = [f for f in os.listdir(DATA_PATH) if f.endswith(".parquet")]
    df_list = [pd.read_parquet(os.path.join(DATA_PATH, f)) for f in files[:10]]
    df = pd.concat(df_list, ignore_index=True)
    return df

def preprocess(df):
    X = df[["trip_distance", "hour", "day_of_week"]]
    y = df["congestion_level"]
    return X, y

def evaluate():
    print("Loading model...")
    model = joblib.load(MODEL_PATH)

    print("Loading data...")
    df = load_data()
    X, y = preprocess(df)

    print("Predicting...")
    y_pred = model.predict(X)

    print("\nClassification Report:")
    print(classification_report(y, y_pred))

    # Confusion Matrix
    cm = confusion_matrix(y, y_pred)
    
    plt.figure(figsize=(6,5))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues",
                xticklabels=["HIGH", "LOW", "MEDIUM"],
                yticklabels=["HIGH", "LOW", "MEDIUM"])
    
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.title("Confusion Matrix")
    plt.show()

if __name__ == "__main__":
    evaluate()