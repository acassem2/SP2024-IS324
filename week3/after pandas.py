import pandas as pd 
from nltk.tokenize import word_tokenize
from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords
from nltk.util import ngrams

data = pd.read_csv("C:\Users\adamr\OneDrive\Documents\Github\SP2024-IS324\week3\Political-media-DFE.csv", encoding='latin1')
data.columns
