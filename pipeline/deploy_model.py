# pipeline/deploy_model.py

from huggingface_hub import HfApi, HfFolder, upload_file
import os

# Replace with your actual repo name
REPO_ID = "Manish-Hub/Tourism_Package_Prediction"
MODEL_PATH = "models/xgboost_final_model.joblib"

# Authenticate using token stored in environment variable
token = os.getenv("HF_TOKEN")
api = HfApi()
HfFolder.save_token(token)

# Upload the model file
upload_file(
    path_or_fileobj=MODEL_PATH,
    path_in_repo="xgboost_final_model.joblib",
    repo_id=REPO_ID,
    repo_type="model"
)

print(f"✅ Model pushed to {REPO_ID}")
