from xgboost import XGBClassifier
import joblib

def train_model(X_train, y_train):
    """
    Train XGBoost model on provided training data.
    """
    model = XGBClassifier(use_label_encoder=False, eval_metric='logloss')
    model.fit(X_train, y_train)
    return model

def save_model(model, path="models/xgboost_final_model.joblib"):
    """
    Save trained model to disk using joblib.
    Default path saves to models/ folder.
    """
    joblib.dump(model, path)
