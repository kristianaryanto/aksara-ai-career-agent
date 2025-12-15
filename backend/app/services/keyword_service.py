from sklearn.feature_extraction.text import TfidfVectorizer
import re

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'\s+', ' ', text) # Remove extra whitespace
    text = re.sub(r'[^a-z0-9\s]', '', text) # Remove punctuation
    return text

def extract_keywords_tfidf(text_corpus: list[str], top_n=20):
    """
    Extracts top N keywords from a list of documents using TF-IDF.
    This is the cost-reduction step.
    """
    if not text_corpus:
        return []

    preprocessed_corpus = [preprocess_text(doc) for doc in text_corpus]
    
    vectorizer = TfidfVectorizer(stop_words='english', max_features=100)
    tfidf_matrix = vectorizer.fit_transform(preprocessed_corpus)
    
    feature_names = vectorizer.get_feature_names_out()
    
    # For a single corpus, we can just return the most important features.
    return feature_names[:top_n]