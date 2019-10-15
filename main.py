# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 14:42:06 2019

@author: erika
"""

import nltk
from nltk import word_tokenize
print (nltk.__version__)
f = open('49960.txt')
raw = f.read()
tokens = word_tokenize(raw)
type(tokens)