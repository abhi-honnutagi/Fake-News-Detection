import numpy as np
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, classification_report, roc_curve, auc
)

def evaluate_model(model, X_test, y_test, model_name="Model"):
    """
    Week 4: Model Evaluation
    Calculates Accuracy, Precision, Recall, F1-Score, Confusion Matrix, ROC-AUC.
    """
    y_pred = model.predict(X_test)
    
    # Predict probabilities if supported
    if hasattr(model, "predict_proba"):
        y_prob = model.predict_proba(X_test)[:, 1]
    elif hasattr(model, "decision_function"):
        df = model.decision_function(X_test)
        y_prob = (df - df.min()) / (df.max() - df.min() + 1e-9)
    else:
        y_prob = y_pred.astype(float)
        
    acc = float(accuracy_score(y_test, y_pred))
    prec = float(precision_score(y_test, y_pred, average='binary', zero_division=0))
    rec = float(recall_score(y_test, y_pred, average='binary', zero_division=0))
    f1 = float(f1_score(y_test, y_pred, average='binary', zero_division=0))
    
    cm = confusion_matrix(y_test, y_pred).tolist()
    
    fpr, tpr, thresholds = roc_curve(y_test, y_prob)
    roc_auc = float(auc(fpr, tpr))
    
    report_dict = classification_report(y_test, y_pred, output_dict=True, zero_division=0)
    
    return {
        "model_name": model_name,
        "accuracy": round(acc, 4),
        "precision": round(prec, 4),
        "recall": round(rec, 4),
        "f1_score": round(f1, 4),
        "auc_roc": round(roc_auc, 4),
        "confusion_matrix": cm,
        "roc_curve": {
            "fpr": [round(val, 4) for val in fpr.tolist()],
            "tpr": [round(val, 4) for val in tpr.tolist()]
        },
        "classification_report": report_dict
    }
