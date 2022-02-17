import pandas as pd
import string
import numpy as np
import csv
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from bm25 import BM25
from preProcess import preProcess


def preProcess(s):
    ps = PorterStemmer()
    s = word_tokenize(s)
    s = [ps.stem(w) for w in s]
    s = ' '.join(s)
    return s

# lyrics_data = './Term_Project/assets/data.csv'
# lyric_df = pd.read_csv(lyrics_data)
# lyrics = lyric_df['Lyric']
# bm25 = BM25()
# bm25.fit(lyrics)
# pickle.dump(bm25, open(
#     'D:/Git/Repositories/IR-Term-Project-backend/Term_Project/assets/bm25_fit.pkl', 'wb'))

# lyrics_data = './Term_Project/assets/data.csv'
# lyric_df = pd.read_csv(lyrics_data)
# lyrics = lyric_df['Lyric']

# vectorizer = CountVectorizer(preprocessor=preProcess, ngram_range=(1, 3))
# X = vectorizer.fit_transform(lyrics)
# pickle.dump(vectorizer, open(
#     'D:/Git/Repositories/IR-Term-Project-backend/Term_Project/assets/vectorizer.pkl', 'wb'))
# pickle.dump(X, open(
#     'D:/Git/Repositories/IR-Term-Project-backend/Term_Project/assets/tf_fit.pkl', 'wb'))

# vectorizer2 = TfidfVectorizer(preprocessor=preProcess, ngram_range=(1, 3))
# X = vectorizer2.fit_transform(lyrics)
# pickle.dump(vectorizer2, open(
#     'D:/Git/Repositories/IR-Term-Project-backend/Term_Project/assets/vectorizer_tfidf.pkl', 'wb'))

# pickle.dump(X, open(
#     'D:/Git/Repositories/IR-Term-Project-backend/Term_Project/assets/ifidf_fit.pkl', 'wb'))
