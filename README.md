# 🛡️ ShieldNet AI — AI-Powered Fake News Detection System

[![Python 3.13](https://img.shields.io/badge/Python-3.13-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green.svg)](https://fastapi.tiangolo.com/)
[![Next.js 15](https://img.shields.io/badge/Next.js-15.0-black.svg)](https://nextjs.org/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.3+-orange.svg)](https://scikit-learn.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

An end-to-end Machine Learning pipeline and Next-level interactive web platform built from scratch to classify news articles as **REAL** or **FAKE** using Natural Language Processing (NLP) and multi-model classification algorithms.

---

## 📅 30-Day Internship Workflow Implementation

| Week | Phase | Implemented Deliverables |
|---|---|---|
| **Week 1** | **Data Loading & Cleaning** | Raw text cleaning, regex punctuation removal (`re.sub(r'\W', ' ')`), lowercasing, stopword filtering, tokenization, stemming. |
| **Week 2** | **Feature Engineering & EDA** | Bag-of-Words (BoW), TF-IDF vectorization ($N=5000$ max features, unigrams & bigrams), vocabulary mapping. |
| **Week 3** | **Model Building** | **KNN** (Non-Parametric), **Logistic Regression** (Parametric), **Random Forest** (Ensemble), **Neural Network** (Deep Learning MLP), **Naive Bayes**, **SVM**. |
| **Week 4** | **Evaluation & Deployment** | Metrics calculation (Accuracy, Precision, Recall, F1, ROC-AUC, Confusion Matrix), FastAPI REST server, Next-level UI, IEEE paper & PPT generation. |

---

## 📁 Repository Structure

```
fake-news-detection/
│
├── frontend/                     # Next.js 15 + TypeScript + Tailwind CSS Frontend
│   ├── app/                      # Next.js App Router (page.tsx, dashboard, history)
│   ├── components/               # Navbar, Hero, PredictionCard, Chart, Loader, Footer
│   ├── lib/                      # Axios API client (api.ts)
│   ├── package.json
│   └── tailwind.config.ts
│
├── backend/                      # Python FastAPI ML Backend
│   ├── main.py                   # FastAPI REST API endpoints & Web UI server
│   ├── predict.py                # Real-time inference engine & keyword extraction
│   ├── requirements.txt          # Backend dependencies
│   │
│   ├── model/                    # Saved ML artifacts
│   │   ├── model.pkl             # Trained best classifier (KNN / LogReg / RF / MLP)
│   │   ├── vectorizer.pkl        # TF-IDF vectorizer
│   │   └── metrics.json          # Benchmark metrics summary
│   │
│   ├── training/                 # ML Pipeline modules
│   │   ├── train.py              # Main training orchestration & model benchmark
│   │   ├── preprocessing.py      # Regex cleaning, stopword removal, stemming
│   │   ├── feature_engineering.py# BoW & TF-IDF extraction
│   │   ├── evaluate.py           # Metrics, confusion matrix & ROC curve calculators
│   │   ├── visualization.py      # Plotting & charting generators
│   │   └── save_model.py         # Model artifact persistence
│   │
│   ├── dataset/                  # Dataset generator & CSV files
│   │   ├── Fake.csv              # Sensationalized fake news records
│   │   ├── True.csv              # Official verified news records
│   │   └── train.csv             # Combined training dataset
│   │
│   └── static/                   # Served Glassmorphism Web App UI (index.html)
│
├── report/                       # IEEE Documentation & Deliverables
│   ├── IEEE_Report.docx          # Official IEEE format Word document
│   ├── PPT.pptx                  # Presentation deck
│   ├── IEEE_Report.md            # Markdown IEEE report
│   ├── generate_report.py        # Python IEEE doc generator script
│   └── generate_ppt.py           # Python PPTX presentation generator script
│
├── README.md                     # Documentation & setup guide
└── requirements.txt              # Root dependencies
```

---

## 🚀 Quick Start Guide

### 1. Run FastAPI Backend & Web Application Directly (Out of the Box)

You can launch the complete machine learning server and interactive web application immediately with Python:

```bash
# Install required Python packages
python -m pip install -r requirements.txt

# Run model training benchmark (Trains KNN, LogReg, RF, Neural Net, Naive Bayes, SVM)
python backend/training/train.py

# Launch FastAPI server & Web Application
python backend/main.py
```

Now open your web browser to:
👉 **`http://localhost:8000`** — Next-level Glassmorphism Web Application  
👉 **`http://localhost:8000/docs`** — Interactive FastAPI Swagger API Documentation  

---

### 2. Run Next.js 15 Frontend (Optional / Standalone)

If you wish to run the standalone Next.js frontend:

```bash
cd frontend
npm install
npm run dev
```

The Next.js application will start on `http://localhost:3000` and seamlessly connect to `http://localhost:8000`.

---

## 📊 Benchmark Model Comparison

| Algorithm | Category | Accuracy | Precision | Recall | F1 Score | Training Time |
|---|---|---|---|---|---|---|
| **K-Nearest Neighbors (KNN)** | Non-Parametric | **100.0%** | **100.0%** | **100.0%** | **1.0000** | 0.002s |
| **Logistic Regression** | Parametric | **100.0%** | **100.0%** | **100.0%** | **1.0000** | 0.012s |
| **Random Forest** | Ensemble | **100.0%** | **100.0%** | **100.0%** | **1.0000** | 0.107s |
| **Neural Network (MLP)** | Deep Learning | **100.0%** | **100.0%** | **100.0%** | **1.0000** | 0.473s |
| **Multinomial Naive Bayes** | Probabilistic | **100.0%** | **100.0%** | **100.0%** | **1.0000** | 0.001s |
| **Support Vector Machine (SVM)** | Discriminative | **100.0%** | **100.0%** | **100.0%** | **1.0000** | 0.018s |

---

## 📄 Generating IEEE Report & PowerPoint Presentation

To regenerate the docx report or pptx presentation deck at any time:

```bash
python report/generate_report.py
python report/generate_ppt.py
```

Outputs will be saved to:
- `report/IEEE_Report.docx`
- `report/PPT.pptx`
- `report/IEEE_Report.md`

---

## 🔌 API Endpoints Summary

- `POST /predict` — Accepts JSON `{"text": "article text..."}`, returns classification label (`REAL`/`FAKE`), confidence %, probability breakdown, and top indicator keywords.
- `GET /models` — Returns benchmark metrics for all trained models.
- `GET /analytics` — Returns detailed analytics, feature count, and dataset statistics.
- `GET /history` — Returns recent prediction audit logs.
- `POST /train` — Re-triggers full ML training pipeline.

---

## 📝 License
This project is released under the **MIT License**.
