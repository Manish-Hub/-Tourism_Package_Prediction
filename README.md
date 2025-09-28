# 🧠 Tourism Package Interest Predictor
> This project predicts whether a customer is likely to respond positively to a tourism package offer, using demographic, behavioral, and engagement features. It demonstrates a full-stack machine learning pipeline—from preprocessing and model comparison to deployment and interpretability.<
---

## 🔍 Problem Statement
> Tourism companies often struggle to identify which customers are likely to respond to promotional packages. This model helps predict interest levels based on user profiles, enabling targeted outreach and personalized marketing strategies.<
---

## 🧭 Tech specs
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
- Colab: Reproducible notebook interface
- Hugging Face Spaces: [Live App](https://huggingface.co/spaces/ManishManu44/TourismPackagePrediction)

  The app accepts user inputs and returns predictions with confidence scores and interpretability-enhancing messages:
- 🟢 High interest → personalize the pitch
- 🔴 Low interest → reconsider strateg
---

## 🧠 Interpretability & UX
- Dynamic input fields
- Conditional color feedback
- Confidence scores
- Insight boxes for actionable messaging
---

📜 License
- MIT License. See LICENSE file for details
---

## 🌐 Live Demo
- 👉 Try the app on Hugging Face Spaces: [Tourism Package Predictor](https://huggingface.co/spaces/ManishManu44/TourismPackagePrediction)
---

## 🛠️ Setup Instructions
```
bash
pip install -r requirements.txt
python deployment/app.py
