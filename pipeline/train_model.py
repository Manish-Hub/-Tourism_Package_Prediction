from xgboost import XGBClassifier
import joblib

def train_model(X_train, y_train):
    model = XGBClassifier()
    model.fit(X_train, y_train)
    return model

def save_model(model, path):
    joblib.dump(model, path)
