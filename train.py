import pandas as pd
import joblib
import mlflow
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score

MODEL_PATH = "models/model.pkl"

def train():

    df = pd.read_csv("creditcard.csv")

    X = df.drop("Class", axis=1)
    y = df["Class"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        stratify=y,
        random_state=42
    )

    model = RandomForestClassifier(
        n_estimators=300,
        max_depth=12,
        n_jobs=-1,
        random_state=42
    )

    model.fit(X_train, y_train)

    preds = model.predict_proba(X_test)[:, 1]

    auc = roc_auc_score(y_test, preds)

    with mlflow.start_run():
        mlflow.log_metric("AUC", auc)

    joblib.dump(
        {
            "model": model,
            "columns": X.columns.tolist()
        },
        MODEL_PATH
    )

    print(f"AUC Score: {auc:.4f}")

if __name__ == "__main__":
    train()