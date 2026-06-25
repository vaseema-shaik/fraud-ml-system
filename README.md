# 🏦 AI-Powered Fraud Detection & Risk Intelligence Platform

🚀 An enterprise-style Machine Learning system for detecting fraudulent financial transactions using real-world credit card transaction data. Built with FastAPI, Streamlit, MLflow, Docker, and MLOps practices for real-time fraud prediction and monitoring.

---

## 🌟 Key Features

* 🤖 Machine Learning Fraud Detection Model
* ⚡ FastAPI Real-Time Prediction API
* 📊 Interactive Streamlit Dashboard
* 📈 MLflow Experiment Tracking
* 🐳 Docker Containerization
* 🔄 CI/CD with GitHub Actions
* 📉 Model Performance Monitoring
* 🧠 Risk Scoring Engine
* 🔍 Fraud Probability Prediction
* 💾 Model Persistence with Joblib

---

## 🏗️ Project Structure

```text
fraud-ml-system/
│
├── train.py
├── main.py
├── predictor.py
├── model_loader.py
├── streamlit_app.py
│
├── models/
│   └── model.pkl
│
├── mlruns/
│
├── requirements.txt
├── deployment.yaml
├── ci.yml
├── README.md
└── .gitignore
```

---

## 🧠 How It Works

1. Train model using credit card transaction dataset
2. Save trained model as model.pkl
3. Load model through FastAPI service
4. User submits transaction details
5. Model predicts fraud probability
6. Dashboard displays risk score and prediction

---

## 🚀 Installation & Setup

```bash
git clone https://github.com/vaseema-shaik/fraud-ml-system.git

cd fraud-ml-system

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt
```

---

## 🎯 Train Model

```bash
python train.py
```

Expected Output:

```text
AUC Score: 0.9780
```

---

## ⚡ Start FastAPI Server

```bash
uvicorn main:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

---

## 📊 Start Streamlit Dashboard

Open a new terminal:

```bash
streamlit run streamlit_app.py
```

Open:

```text
http://localhost:8501
```

---

## 📈 Model Performance

* Dataset: Kaggle Credit Card Fraud Detection
* Algorithm: Random Forest Classifier
* AUC Score: 0.9780
* Real-Time Prediction API
* Enterprise Dashboard

---

## 🛠️ Technology Stack

* Python
* Scikit-Learn
* FastAPI
* Streamlit
* MLflow
* Pandas
* NumPy
* Docker
* GitHub Actions
* Kubernetes (Deployment Ready)

---

## 💼 Resume Highlights

* Built an end-to-end fraud detection platform using Machine Learning and MLOps principles.
* Developed REST APIs for real-time fraud prediction using FastAPI.
* Designed an interactive dashboard using Streamlit.
* Implemented experiment tracking using MLflow.
* Containerized application using Docker and prepared deployment workflows.

---

## 👤 Author

Shaik Vaseema

GitHub:
https://github.com/vaseema-shaik

LinkedIn:
https://linkedin.com/in/shaik-vaseema-81977a37b

---

## ⭐ Support

If you found this project useful, please give it a Star ⭐ on GitHub.

