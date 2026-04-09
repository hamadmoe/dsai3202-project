import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
import joblib

DATA_PATH = "data/features/"
MODEL_PATH = "models/"

def load_data():
    files = [f for f in os.listdir(DATA_PATH) if f.endswith(".parquet")]
    df_list = [pd.read_parquet(os.path.join(DATA_PATH, f)) for f in files[:10]]
    df = pd.concat(df_list, ignore_index=True)
    return df

def preprocess(df):
    X = df[["trip_distance", "hour", "day_of_week"]]
    y = df["congestion_level"]
    return X, y

def train():
    os.makedirs(MODEL_PATH, exist_ok=True)

    print("Loading data...")
    df = load_data()

    X, y = preprocess(df)

    print("Splitting data...")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    print("Training baseline model (Logistic Regression)...")
    baseline = LogisticRegression(
        max_iter=500,
        C=1.0,
        solver="lbfgs",
        multi_class="auto"
    )
    baseline.fit(X_train, y_train)
    print("\nBaseline Model (Logistic Regression):")
    y_pred_base = baseline.predict(X_test)
    print(classification_report(y_test, y_pred_base))

    print("Training main model (Random Forest)...")
    model = RandomForestClassifier(
        n_estimators=200,
        max_depth=None,
        min_samples_split=2,
        random_state=42,
        n_jobs=-1
    )
    model.fit(X_train, y_train)

    print("\nMain Model (Random Forest):")
    y_pred_rf = model.predict(X_test)
    print(classification_report(y_test, y_pred_rf))

    # Save model
    joblib.dump(model, os.path.join(MODEL_PATH, "model.pkl"))

    print("Model saved.")

if __name__ == "__main__":
    train()