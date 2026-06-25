from fastapi import FastAPI
from pydantic import BaseModel

from predictor import predict

app = FastAPI(
    title="Fraud Detection API"
)

class Transaction(BaseModel):
    data: dict

@app.get("/")
def home():
    return {
        "status": "running"
    }

@app.post("/predict")
def predict_api(txn: Transaction):

    try:
        return predict(txn.data)

    except Exception as e:
        return {
            "error": str(e)
        }