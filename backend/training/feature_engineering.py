from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer

def build_vectorizer(method="tfidf", max_features=5000, ngram_range=(1, 2)):
    """
    Week 2: Feature Engineering
    Builds either Bag-of-Words (CountVectorizer) or TF-IDF Vectorizer.
    """
    if method == "bow":
        vectorizer = CountVectorizer(max_features=max_features, ngram_range=ngram_range)
    else:
        vectorizer = TfidfVectorizer(max_features=max_features, ngram_range=ngram_range, sublinear_tf=True)
    return vectorizer

def extract_features(texts, vectorizer=None, fit=True, max_features=5000):
    if vectorizer is None:
        vectorizer = build_vectorizer(method="tfidf", max_features=max_features)
        
    if fit:
        X_vec = vectorizer.fit_transform(texts)
    else:
        X_vec = vectorizer.transform(texts)
        
    return X_vec, vectorizer
