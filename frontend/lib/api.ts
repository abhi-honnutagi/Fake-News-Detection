import axios from 'axios';

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://127.0.0.1:8000';

export const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export interface PredictionRequest {
  text: string;
  model_name?: string;
}

export interface PredictionResponse {
  label: string;
  is_fake: boolean;
  confidence: number;
  probabilities: {
    REAL: number;
    FAKE: number;
  };
  model_used: string;
  key_indicators: Array<{ word: string; weight: number }>;
  cleaned_text: string;
  timestamp: string;
}

export interface ModelMetrics {
  accuracy: number;
  precision: number;
  recall: number;
  f1_score: number;
  auc_roc: number;
  training_time_sec: number;
  inference_time_sec: number;
  confusion_matrix: number[][];
}

export interface AnalyticsResponse {
  best_model: string;
  total_samples: number;
  train_samples: number;
  test_samples: number;
  feature_count: number;
  models: Record<string, ModelMetrics>;
}

export const classifyNews = async (text: string): Promise<PredictionResponse> => {
  const res = await api.post<PredictionResponse>('/predict', { text });
  return res.data;
};

export const getModelsSummary = async (): Promise<AnalyticsResponse> => {
  const res = await api.get<AnalyticsResponse>('/models');
  return res.data;
};

export const getPredictionHistory = async () => {
  const res = await api.get('/history');
  return res.data;
};

export const triggerRetraining = async () => {
  const res = await api.post('/train');
  return res.data;
};
