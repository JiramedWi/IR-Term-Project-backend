import pickle
import string

import nltk
import numpy as np
import pandas as pd
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from bm25 import BM25
from openfile import preProcess


tf_open = open('./Term_Project/assets/tf_fit.pkl', 'rb')
tf_fit = pickle.load(tf_open)
vectorizer_tf = pickle.load(open('./Term_Project/assets/vectorizer.pkl', 'rb'
    ))
tfidf_fit = pickle.load(open('./Term_Project/assets/ifidf_fit.pkl', 'rb'
    ))
vectorizer_tfidf = pickle.load(open('./Term_Project/assets/vectorizer_tfidf.pkl', 'rb'
    ))
bm25_fit = pickle.load(open('./Term_Project/assets/bm25_fit.pkl', 'rb'
    ))
lyrics_data = './Term_Project/assets/data.csv'


def tf_ranking(query):
    lyric_df = pd.read_csv(lyrics_data)
    query_vec = vectorizer_tf.transform(query)

    tf_fit.data = np.log10(tf_fit.data + 1)
    cos_sim = cosine_similarity(tf_fit, query_vec).reshape((-1), )
    tf = pd.DataFrame({'tf': list(cos_sim), 
    'lyric': list(lyric_df['Lyric']), 
    'song': list(lyric_df['Song']), 
    'artist': list(lyric_df['Artist'])}).nlargest(columns='tf', n=10)

    tf['rank'] = tf['tf'].rank(ascending=False)
    tf = tf.drop(columns='tf', axis=1)
    tf = tf.to_dict('record')
    return tf

def tf_idf_ranking(query):
    lyric_df = pd.read_csv(lyrics_data)
    query_vec = vectorizer_tfidf.transform(query)
    cos_sim = cosine_similarity(tfidf_fit, query_vec).reshape((-1), )
    tf = pd.DataFrame({'tfidf': list(cos_sim), 
    'lyric': list(lyric_df['Lyric']), 
    'song': list(lyric_df['Song']), 
    'artist': list(lyric_df['Artist'])}).nlargest(columns='tfidf', n=10)

    tf['rank'] = tf['tfidf'].rank(ascending=False)
    tf = tf.drop(columns='tfidf', axis=1)
    tf = tf.to_dict('record')
    return tf

def bm25_ranking(query):
    lyric_df = pd.read_csv(lyrics_data)
    score = bm25_fit.transform(query)
    tf = pd.DataFrame(
        {'bm25': list(score),
    'lyric': list(lyric_df['Lyric']), 
    'song': list(lyric_df['Song']), 
    'artist': list(lyric_df['Artist'])}).nlargest(columns='bm25', n=10)

    tf['rank'] = tf['bm25'].rank(ascending=False)
    tf = tf.drop(columns='bm25', axis=1)
    tf = tf.to_dict('record')
    return tf

def searchExactSong(query):
    df = pd.read_csv(lyrics_data)
    # find song title
    rs = df[df['Song'].str.contains(query)]
    # split the word of song title and find the exact word
    rs = rs[rs['Song'].apply(lambda s: s.split()[0]==query.split()[0])]
    rs = rs.to_dict('record')
    return rs