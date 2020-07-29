#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: ankuraggarwal
"""
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

text = ["What is your name","Can you tell me your name"]
count = CountVectorizer().fit_transform(text)
Similarity = cosine_similarity(count)
print (Similarity)


