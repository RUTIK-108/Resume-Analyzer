import spacy
import re
from nltk.corpus import stopwords

nlp = spacy.load("en_core_web_sm")

def clean_text(text):
    text = re.sub(r'\W+', ' ', text)
    text = text.lower()
    text = ' '.join([word for word in text.split() if word not in stopwords.words('english')])
    return text

def extract_keywords(text):
    doc = nlp(text)
    return [token.lemma_ for token in doc if token.is_alpha and not token.is_stop]