import joblib
import pandas as pd

def test_model_load():
    model = joblib.load("models/xgboost_final_model.joblib")
    assert model is not None

def test_prediction_shape():
    model = joblib.load("models/xgboost_final_model.joblib")
    sample = pd.DataFrame({
        "Age": [30],
        "Income": [500000],
        "Gender": ["Male"]
    })
    pred = model.predict(sample)
    assert len(pred) == 1
