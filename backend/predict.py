import os
import sys
import numpy as np

# Add parent directory to sys.path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from training.preprocessing import clean_text
from training.save_model import load_artifacts

class FakeNewsPredictor:
    def __init__(self, model_dir="c:/CSEN/project/fake-news-detection/backend/model"):
        self.model_dir = model_dir
        self.model, self.vectorizer, self.metrics = load_artifacts(model_dir)
        self.feature_names = np.array(self.vectorizer.get_feature_names_out())
        
    def predict(self, text: str):
        cleaned = clean_text(text)
        if not cleaned.strip():
            return {
                "label": "UNKNOWN",
                "is_fake": False,
                "confidence": 0.0,
                "probabilities": {"REAL": 0.5, "FAKE": 0.5},
                "key_indicators": [],
                "cleaned_text": cleaned
            }
            
        X_vec = self.vectorizer.transform([cleaned])
        
        # Binary prediction (1: FAKE, 0: REAL)
        pred_class = int(self.model.predict(X_vec)[0])
        
        if hasattr(self.model, "predict_proba"):
            probs = self.model.predict_proba(X_vec)[0]
            real_prob = float(probs[0])
            fake_prob = float(probs[1])
        elif hasattr(self.model, "decision_function"):
            score = float(self.model.decision_function(X_vec)[0])
            fake_prob = 1.0 / (1.0 + np.exp(-score))
            real_prob = 1.0 - fake_prob
        else:
            fake_prob = 1.0 if pred_class == 1 else 0.0
            real_prob = 1.0 - fake_prob
            
        confidence = fake_prob if pred_class == 1 else real_prob
        
        # Extract top active feature keywords from input text
        active_indices = X_vec.nonzero()[1]
        active_weights = X_vec.data
        
        word_importance = []
        for idx, weight in zip(active_indices, active_weights):
            word = self.feature_names[idx]
            word_importance.append({"word": word, "weight": round(float(weight), 4)})
            
        word_importance.sort(key=lambda x: x["weight"], reverse=True)
        top_indicators = word_importance[:10]
        
        label_str = "FAKE" if pred_class == 1 else "REAL"
        
        return {
            "label": label_str,
            "is_fake": (pred_class == 1),
            "confidence": round(float(confidence), 4),
            "probabilities": {
                "REAL": round(real_prob, 4),
                "FAKE": round(fake_prob, 4)
            },
            "model_used": self.metrics.get("best_model", "Selected Model"),
            "key_indicators": top_indicators,
            "cleaned_text": cleaned
        }

if __name__ == "__main__":
    predictor = FakeNewsPredictor()
    sample_fake = "BREAKING: Secret Alien Technology Discovered in Underground Bunker! Scientists Shocked!"
    print("Sample Fake Prediction:")
    print(predictor.predict(sample_fake))
