import os
import sys
import json
import csv
import io
from datetime import datetime
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, FileResponse, StreamingResponse
from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any

# Ensure backend root is on path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from predict import FakeNewsPredictor
from training.train import train_all_models

# Import report generators
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "report")))
try:
    from generate_report import create_ieee_report
    from generate_ppt import create_presentation
except Exception as e:
    print(f"Report import note: {e}")

app = FastAPI(
    title="AI-Powered Fake News Detection API",
    description="Machine Learning Text Classification Pipeline with FastAPI Backend",
    version="1.0.0"
)

# CORS middleware for Next.js frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize predictor & history log
predictor = None
try:
    predictor = FakeNewsPredictor()
except Exception as e:
    print(f"⚠️ Initial load warning: {e}. Will train model on startup.")

prediction_history: List[Dict[str, Any]] = []

class NewsRequest(BaseModel):
    text: str = Field(..., example="BREAKING: Secret Alien Technology Discovered in Underground Bunker!")
    model_name: Optional[str] = "Best Model"

class PredictionResponse(BaseModel):
    label: str
    is_fake: bool
    confidence: float
    probabilities: Dict[str, float]
    model_used: str
    key_indicators: List[Dict[str, Any]]
    cleaned_text: str
    timestamp: str

@app.on_event("startup")
def startup_event():
    global predictor
    model_dir = "c:/CSEN/project/fake-news-detection/backend/model"
    if not os.path.exists(os.path.join(model_dir, "model.pkl")):
        train_all_models()
    predictor = FakeNewsPredictor()

@app.get("/health")
def health_check():
    return {"status": "online", "model_loaded": predictor is not None, "timestamp": datetime.now().isoformat()}

@app.post("/predict", response_model=PredictionResponse)
def predict_news(request: NewsRequest):
    if not predictor:
        raise HTTPException(status_code=500, detail="ML model is not loaded.")
        
    if not request.text or len(request.text.strip()) < 10:
        raise HTTPException(status_code=400, detail="Input text must be at least 10 characters long.")
        
    res = predictor.predict(request.text)
    res["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Keep last 50 predictions in memory log
    prediction_history.insert(0, {
        "text": request.text[:120] + ("..." if len(request.text) > 120 else ""),
        "label": res["label"],
        "confidence": res["confidence"],
        "model_used": res["model_used"],
        "timestamp": res["timestamp"]
    })
    if len(prediction_history) > 50:
        prediction_history.pop()
        
    return res

@app.get("/models")
def get_models_summary():
    if not predictor or not predictor.metrics:
        raise HTTPException(status_code=404, detail="Metrics not found.")
    return predictor.metrics

@app.get("/analytics")
def get_analytics():
    if not predictor or not predictor.metrics:
        raise HTTPException(status_code=404, detail="Metrics not found.")
        
    metrics = predictor.metrics
    models_data = metrics.get("models", {})
    
    return {
        "best_model": metrics.get("best_model"),
        "total_samples": metrics.get("total_samples"),
        "train_samples": metrics.get("train_samples"),
        "test_samples": metrics.get("test_samples"),
        "feature_count": metrics.get("feature_count"),
        "models": models_data
    }

@app.get("/history")
def get_prediction_history():
    return {"history": prediction_history}

@app.get("/download-report")
def download_ieee_report():
    report_path = "c:/CSEN/project/fake-news-detection/report/IEEE_Report.docx"
    if not os.path.exists(report_path):
        create_ieee_report(report_path)
    return FileResponse(
        path=report_path,
        filename="IEEE_Fake_News_Detection_Report.docx",
        media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )

@app.get("/download-ppt")
def download_ppt():
    ppt_path = "c:/CSEN/project/fake-news-detection/report/PPT.pptx"
    if not os.path.exists(ppt_path):
        create_presentation(ppt_path)
    return FileResponse(
        path=ppt_path,
        filename="Fake_News_Detection_Presentation.pptx",
        media_type="application/vnd.openxmlformats-officedocument.presentationml.presentation"
    )

@app.get("/export-csv")
def export_csv_history():
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["Timestamp", "Text", "Verdict", "Confidence", "Model Engine"])
    for item in prediction_history:
        writer.writerow([item["timestamp"], item["text"], item["label"], f"{item['confidence']*100:.1f}%", item["model_used"]])
    output.seek(0)
    return StreamingResponse(
        io.BytesIO(output.getvalue().encode('utf-8')),
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=Prediction_Audit_Log.csv"}
    )

@app.post("/train")
def trigger_training():
    summary = train_all_models()
    global predictor
    predictor = FakeNewsPredictor()
    return {"message": "Training completed successfully!", "summary": summary}

# Static file serving for FastAPI Web Application UI
static_dir = os.path.join(os.path.dirname(__file__), "static")
os.makedirs(static_dir, exist_ok=True)
app.mount("/static", StaticFiles(directory=static_dir), name="static")

@app.get("/", response_class=HTMLResponse)
def read_root():
    index_file = os.path.join(static_dir, "index.html")
    if os.path.exists(index_file):
        return FileResponse(index_file)
    return HTMLResponse("<h2>AI-Powered Fake News Detection API is running! Access /docs for Swagger UI.</h2>")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
