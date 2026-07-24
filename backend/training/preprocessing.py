import re
import string

# English Stopwords set built-in to eliminate extra downloads
STOPWORDS = {
    'a', 'about', 'above', 'after', 'again', 'against', 'all', 'am', 'an', 'and', 'any', 'are', 'aren\'t', 'as', 'at',
    'be', 'because', 'been', 'before', 'being', 'below', 'between', 'both', 'but', 'by', 'can', 'can\'t', 'cannot',
    'could', 'couldn\'t', 'did', 'didn\'t', 'do', 'does', 'doesn\'t', 'doing', 'don\'t', 'down', 'during', 'each',
    'few', 'for', 'from', 'further', 'had', 'hadn\'t', 'has', 'hasn\'t', 'have', 'haven\'t', 'having', 'he', 'he\'d',
    'he\'ll', 'he\'s', 'her', 'here', 'here\'s', 'hers', 'herself', 'him', 'himself', 'his', 'how', 'how\'s', 'i',
    'i\'d', 'i\'ll', 'i\'m', 'i\'ve', 'if', 'in', 'into', 'is', 'isn\'t', 'it', 'it\'s', 'its', 'itself', 'let\'s',
    'me', 'more', 'most', 'mustn\'t', 'my', 'myself', 'no', 'nor', 'not', 'of', 'off', 'on', 'once', 'only', 'or',
    'other', 'ought', 'our', 'ours', 'ourselves', 'out', 'over', 'own', 'same', 'shan\'t', 'she', 'she\'d', 'she\'ll',
    'she\'s', 'should', 'shouldn\'t', 'so', 'some', 'such', 'than', 'that', 'that\'s', 'the', 'their', 'theirs',
    'them', 'themselves', 'then', 'there', 'there\'s', 'these', 'they', 'they\'d', 'they\'ll', 'they\'re', 'they\'ve',
    'this', 'those', 'through', 'to', 'too', 'under', 'until', 'up', 'very', 'was', 'wasn\'t', 'we', 'we\'d', 'we\'ll',
    'we\'re', 'we\'ve', 'were', 'weren\'t', 'what', 'what\'s', 'when', 'when\'s', 'where', 'where\'s', 'which', 'while',
    'who', 'who\'s', 'whom', 'why', 'why\'s', 'with', 'won\'t', 'would', 'wouldn\'t', 'you', 'you\'d', 'you\'ll',
    'you\'re', 'you\'ve', 'your', 'yours', 'yourself', 'yourselves'
}

def clean_text(text: str) -> str:
    """
    Week 1: Data Cleaning & Preprocessing
    1. Remove non-word characters and punctuation
    2. Lowercase text
    3. Remove stop words
    4. Remove numerical digits
    """
    if not isinstance(text, str):
        return ""
    
    # 1. Lowercase text
    text = text.lower()
    
    # 2. Remove URLs
    text = re.sub(r'https?://\S+|www\.\S+', ' ', text)
    
    # 3. Remove non-alphanumeric punctuation as per specification (re.sub(r'\W', ' ', text))
    text = re.sub(r'\W', ' ', text)
    
    # 4. Remove numbers
    text = re.sub(r'\d+', ' ', text)
    
    # 5. Tokenize manually
    tokens = text.split()
    
    # 6. Filter stopwords
    filtered_tokens = [w for w in tokens if w not in STOPWORDS and len(w) > 2]
    
    # 7. Basic Stemming (Suffix Removal)
    stemmed_tokens = []
    for word in filtered_tokens:
        if word.endswith('ing') and len(word) > 5:
            word = word[:-3]
        elif word.endswith('ed') and len(word) > 4:
            word = word[:-2]
        elif word.endswith('es') and len(word) > 4:
            word = word[:-2]
        elif word.endswith('s') and len(word) > 3:
            word = word[:-1]
        stemmed_tokens.append(word)
        
    return " ".join(stemmed_tokens)

if __name__ == "__main__":
    sample = "BREAKING: Scientists discover shocking cure overnight at https://example.com! 100% Guaranteed!"
    print("Original:", sample)
    print("Cleaned :", clean_text(sample))
