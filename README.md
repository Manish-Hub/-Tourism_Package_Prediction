# 🧭 Tourism Package Prediction

This project predicts user interest in tourism packages using machine learning. It includes data cleaning, model comparison, and deployment-ready artifacts.

---

## 📁 Repository Structure

- `data/`: Cleaned dataset
- `models/`: Final model artifacts
- `notebooks/`: Full pipeline notebook
- `pipeline/`: Modular training and evaluation scripts
- `deployment/`: App/API code for deployment
- `utils/`: Helper functions
- `tests/`: Unit tests (optional)

---

## 🧠 Final Model Metadata

**Model**: XGBoostClassifier  
**Saved As**: `models/xgboost_final_model.joblib`  
**Performance**:  
- Accuracy: 92%  
- Class 1 Precision: 0.83  
- Class 1 Recall: 0.74  
- Class 1 F1-score: 0.78  

**Intended Use**: Predicting tourism package interest based on user features  
**Limitations**: Sensitive to class imbalance  
**Interpretability Tools**: SHAP-compatible

---

## 🚀 Deployment Plan

- GitHub: Version control and documentation  
- Hugging Face Spaces: Interactive app  
- Colab: Reproducible notebook interface
- Hugging Face Spaces: [Live App](https://huggingface.co/spaces/ManishManu44/TourismPackagePrediction)
---

## 🌐 Live Demo

👉 Try the app on Hugging Face Spaces: [Tourism Package Predictor](https://huggingface.co/spaces/ManishManu44/TourismPackagePrediction)
---

## 🛠️ Setup Instructions

```bash
pip install -r requirements.txt
python deployment/app.py
