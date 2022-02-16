from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

def preProcess(s):
    ps = PorterStemmer()
    s = word_tokenize(s)
    s = [ps.stem(w) for w in s]
    s = ' '.join(s)
    return s
