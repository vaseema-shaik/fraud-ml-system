import pandas as pd

from model_loader import load_model

model, columns = load_model()

def predict(payload):

    sample = pd.DataFrame([payload])

    sample = sample.reindex(
        columns=columns,
        fill_value=0
    )

    probability = model.predict_proba(sample)[0][1]

    risk = (
        "HIGH"
        if probability > 0.7
        else "LOW"
    )

    return {
        "fraud_probability": float(probability),
        "risk": risk
    }