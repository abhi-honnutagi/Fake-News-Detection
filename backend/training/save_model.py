import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

import joblib
import json

def save_artifacts(model, vectorizer, metrics, model_dir=None):
    if model_dir is None:
        model_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "model")
    os.makedirs(model_dir, exist_ok=True)
    
    model_path = os.path.join(model_dir, "model.pkl")
    vectorizer_path = os.path.join(model_dir, "vectorizer.pkl")
    metrics_path = os.path.join(model_dir, "metrics.json")
    
    joblib.dump(model, model_path)
    joblib.dump(vectorizer, vectorizer_path)
    
    with open(metrics_path, "w") as f:
        json.dump(metrics, f, indent=2)
        
    print(f"[OK] Saved model to {model_path}")
    print(f"[OK] Saved vectorizer to {vectorizer_path}")
    print(f"[OK] Saved metrics to {metrics_path}")

def load_artifacts(model_dir=None):
    if model_dir is None:
        model_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "model")
    model_path = os.path.join(model_dir, "model.pkl")
    vectorizer_path = os.path.join(model_dir, "vectorizer.pkl")
    metrics_path = os.path.join(model_dir, "metrics.json")
    
    if not (os.path.exists(model_path) and os.path.exists(vectorizer_path)):
        raise FileNotFoundError(f"Model artifacts not found in {model_dir}. Please run training first.")
        
    model = joblib.load(model_path)
    vectorizer = joblib.load(vectorizer_path)
    
    metrics = {}
    if os.path.exists(metrics_path):
        with open(metrics_path, "r") as f:
            metrics = json.load(f)
            
    return model, vectorizer, metrics
