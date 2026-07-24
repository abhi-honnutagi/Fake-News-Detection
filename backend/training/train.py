import os
import sys
import csv
import time
import numpy as np

# Ensure UTF-8 output encoding for Windows PowerShell console
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC

# Add backend directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from training.preprocessing import clean_text
from training.feature_engineering import extract_features
from training.evaluate import evaluate_model
from training.save_model import save_artifacts
from dataset.generate_dataset import generate_sample_dataset

def load_data(dataset_path):
    if not os.path.exists(dataset_path):
        print("[!] Dataset not found. Generating dataset...")
        generate_sample_dataset()
        
    texts = []
    labels = []
    with open(dataset_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            texts.append(row["text"])
            labels.append(int(row["label"]))
    return texts, np.array(labels)

def train_all_models(dataset_path="c:/CSEN/project/fake-news-detection/backend/dataset/train.csv"):
    texts, y = load_data(dataset_path)
    print(f"[*] Loaded {len(texts)} samples from {dataset_path}")
    
    print("[*] Cleaning text & applying NLP preprocessing...")
    cleaned_texts = [clean_text(t) for t in texts]
    
    print("[*] Extracting TF-IDF features (max_features=5000)...")
    X_vec, vectorizer = extract_features(cleaned_texts, fit=True, max_features=5000)
    
    X_train, X_test, y_train, y_test = train_test_split(X_vec, y, test_size=0.2, random_state=42, stratify=y)
    print(f"[*] Training set: {X_train.shape[0]} | Testing set: {X_test.shape[0]}")
    
    # Week 3: Model Building (KNN, LogReg, RandomForest, NeuralNet + NaiveBayes, SVM)
    models = {
        "KNN": KNeighborsClassifier(n_neighbors=5),
        "LogisticRegression": LogisticRegression(max_iter=1000, C=1.0),
        "RandomForest": RandomForestClassifier(n_estimators=100, random_state=42),
        "NeuralNetwork": MLPClassifier(hidden_layer_sizes=(100,), max_iter=300, random_state=42),
        "NaiveBayes": MultinomialNB(alpha=1.0),
        "SVM": SVC(kernel='linear', probability=True, random_state=42)
    }
    
    results = {}
    trained_models = {}
    best_model_name = None
    best_f1 = -1.0
    
    print("\n[+] Training & Evaluating Models...\n")
    for name, model in models.items():
        t0 = time.time()
        model.fit(X_train, y_train)
        train_time = round(time.time() - t0, 3)
        
        t1 = time.time()
        metrics = evaluate_model(model, X_test, y_test, model_name=name)
        infer_time = round(time.time() - t1, 3)
        
        metrics["training_time_sec"] = train_time
        metrics["inference_time_sec"] = infer_time
        
        results[name] = metrics
        trained_models[name] = model
        
        print(f"[OK] [{name:<18}] Accuracy: {metrics['accuracy']:.4f} | F1-Score: {metrics['f1_score']:.4f} | Train Time: {train_time}s")
        
        if metrics['f1_score'] > best_f1:
            best_f1 = metrics['f1_score']
            best_model_name = name
            
    print(f"\n[BEST MODEL] {best_model_name} with F1-Score: {best_f1:.4f}")
    
    summary = {
        "best_model": best_model_name,
        "models": results,
        "total_samples": len(texts),
        "train_samples": X_train.shape[0],
        "test_samples": X_test.shape[0],
        "feature_count": X_vec.shape[1]
    }
    
    save_artifacts(trained_models[best_model_name], vectorizer, summary)
    return summary

if __name__ == "__main__":
    train_all_models()
