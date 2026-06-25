import joblib

MODEL_PATH = "models/model.pkl"

def load_model():

    data = joblib.load(MODEL_PATH)

    return (
        data["model"],
        data["columns"]
    )