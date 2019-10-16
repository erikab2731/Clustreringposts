import gensim
import tensorflow
import os
import nltk
from nltk import word_tokenize
import re
from nltk.corpus import stopwords

def tokenize(text):
    min_length = 3
    words = map(lambda word: word.lower(), word_tokenize(text))
    words = [word for word in words if word not in cachedStopWords]
    tokens = (list(map(lambda token: nltk.PorterStemmer().stem(token), words)))
    p = re.compile('[a-zA-Z]+')
    filtered_tokens = list (filter(lambda token: p.match(token) and len(token) >= min_length, tokens))
    return filtered_tokens



textos = []

for directory in os.listdir("Data"):
    for file in os.listdir("Data/" + directory):
        f = open("Data/" + directory + "/" + file, "r")

        for line in f:
            line2 = line.split("\\s")
            print(line2[0])




