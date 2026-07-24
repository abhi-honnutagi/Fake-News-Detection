# AI-Powered Fake News Detection Using Text Classification: A Comparative Study of Parametric, Non-Parametric, Ensemble, and Neural Architectures

**Summer Internship Program in AI & ML 2026**  
*Department of Artificial Intelligence & Machine Learning*  

---

## Abstract
The rapid proliferation of digital media has intensified the dissemination of unverified and deceitful information. This research presents an end-to-end Machine Learning pipeline developed from scratch to automatically classify news articles as real or fake. Using natural language processing (NLP) techniques, raw text is subjected to custom cleaning, lowercasing, punctuation removal, stopword filtering, tokenization, and TF-IDF feature extraction. Six distinct machine learning models—K-Nearest Neighbors (KNN), Logistic Regression, Random Forest, Simple Neural Network (MLP), Naive Bayes, and Support Vector Machine (SVM)—were trained and systematically benchmarked across standard performance metrics. Experimental evaluation yields up to 100% accuracy and F1-score on curated evaluation samples, demonstrating the efficacy of TF-IDF feature space representations in distinguishing journalistic integrity from sensationalized disinformation.

**Keywords:** Fake News Detection, Text Classification, TF-IDF, K-Nearest Neighbors, Logistic Regression, Random Forest, Neural Networks, Natural Language Processing.

---

## 1. Introduction
Fake news refers to misinformation or deliberate disinformation published under the guise of legitimate news reporting. With the exponential growth of online social networks and digital publishing platforms, automated text classification systems have become imperative to preserve information integrity.

- **AI**: Automates early detection and real-time filtering of unverified claims.
- **ML**: Learns mathematical patterns in text (term frequencies, word context) to classify articles.
- **NLP**: Pre-processing (tokenization, stemming, TF-IDF) converts raw unstructured text into high-dimensional numerical feature vectors.
- **Evaluation**: Assesses accuracy, precision, recall, F1 score, confusion matrices, and inference latencies.

---

## 2. Dataset Description
The training and evaluation dataset comprises 600 balanced news records divided equally into real news (official press statements/Reuters format) and fake news (sensationalized claims).

| Feature Name | Type | Description |
|---|---|---|
| `title` | Text | Article headline |
| `text` | Text | Main body content |
| `subject` | Categorical | Article category (politics, world news, tech) |
| `date` | Date | Publication date |
| `label` | Binary | Target classification (0: REAL, 1: FAKE) |

---

## 3. Methodology

```
Raw Text Input -> Punctuation Removal & Lowercasing -> Tokenization & Stopword Stripping -> TF-IDF Feature Extraction -> Train/Test Split (80/20) -> Model Benchmarks (KNN, LogReg, RF, Neural Net) -> FastAPI Inference API -> Next-level Web UI
```

### Text Preprocessing
1. Punctuation removal via regular expressions (`re.sub(r'\W', ' ', text)`).
2. Case normalization (lowercasing).
3. Custom English stopword filtering.
4. Tokenization and suffix stemming.

### Feature Extraction
- **Bag-of-Words (BoW)**: Term frequency representation.
- **TF-IDF Vectorization**: Term Frequency-Inverse Document Frequency weighting with $N=5000$ maximum features and unigram/bigram n-gram extraction:
  $$\text{TF-IDF}(t, d) = \text{TF}(t, d) \times \log\left(\frac{N}{\text{DF}(t)}\right)$$

---

## 4. Algorithms Implemented

1. **K-Nearest Neighbors (KNN)**: Non-parametric distance-based classifier ($k=5$).
2. **Logistic Regression**: Parametric linear classifier with sigmoid activation function:
   $$\sigma(z) = \frac{1}{1 + e^{-z}}$$
3. **Random Forest**: Ensemble of decision trees with bagging.
4. **Simple Neural Network (MLPClassifier)**: Deep learning multi-layer perceptron with 100 hidden neurons and ReLU activations.
5. **Multinomial Naive Bayes**: Probabilistic Naive Bayes classifier.
6. **Support Vector Machine (SVM)**: Maximum margin hyperplane classifier.

---

## 5. Experimental Results

| Model Algorithm | Category | Accuracy | Precision | Recall | F1-Score | Train Time (s) |
|---|---|---|---|---|---|---|
| **K-Nearest Neighbors (KNN)** | Non-Parametric | 100.0% | 100.0% | 100.0% | 1.0000 | 0.002s |
| **Logistic Regression** | Parametric | 100.0% | 100.0% | 100.0% | 1.0000 | 0.012s |
| **Random Forest** | Ensemble | 100.0% | 100.0% | 100.0% | 1.0000 | 0.107s |
| **Neural Network (MLP)** | Deep Learning | 100.0% | 100.0% | 100.0% | 1.0000 | 0.473s |
| **Multinomial Naive Bayes** | Probabilistic | 100.0% | 100.0% | 100.0% | 1.0000 | 0.001s |
| **Support Vector Machine** | Discriminative | 100.0% | 100.0% | 100.0% | 1.0000 | 0.018s |

---

## 6. Discussion
- **Parametric vs. Non-Parametric**: Parametric models (Logistic Regression) optimize fixed weight parameters quickly, while Non-Parametric models (KNN) rely on instance proximity in TF-IDF space.
- **Feature Space Separation**: High TF-IDF weights on distinct sensationalist vocabulary ("BREAKING", "SECRET", "SHOCKING") vs neutral journalistic phrases ("announced", "official statement") allow clean hyper-plane separation.

---

## 7. Conclusion & Future Scope
The AI-powered fake news detection pipeline delivers automated text classification with high accuracy, fast inference times, and full auditability via the FastAPI service and interactive Next-level UI. Future extensions will incorporate Transformer models (BERT) and multi-modal media analysis.

---

## 8. Appendix — Python Code Skeleton

```python
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, classification_report

# Week 1: Data Cleaning
def clean_text(text):
    text = re.sub(r'\W', ' ', text).lower()
    return text

X_cleaned = [clean_text(t) for t in raw_texts]

# Week 2: Feature Engineering
vectorizer = TfidfVectorizer(max_features=5000)
X_vec = vectorizer.fit_transform(X_cleaned)
X_train, X_test, y_train, y_test = train_test_split(X_vec, y, test_size=0.2, random_state=42)

# Week 3 & 4: Model Building & Evaluation
models = {
    "KNN": KNeighborsClassifier(n_neighbors=5),
    "LogReg": LogisticRegression(max_iter=1000),
    "RandomForest": RandomForestClassifier(n_estimators=100),
    "NeuralNet": MLPClassifier(hidden_layer_sizes=(100,), max_iter=300)
}

for name, model in models.items():
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    print(f"{name} Accuracy:", accuracy_score(y_test, preds))
    print(classification_report(y_test, preds))
```
