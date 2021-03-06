# Author: Olivier Grisel <olivier.grisel@ensta.org>
#         Lars Buitinck
#         Chyi-Kwei Yau <chyikwei.yau@gmail.com>
# License: BSD 3 clause

from __future__ import print_function
from time import time

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.datasets import fetch_20newsgroups
import nltk
from sklearn.feature_extraction.text import CountVectorizer
import feedparser
import pandas as pd
import numpy as np
import scipy
import operator
import csv
import unicodedata
import json
import re

# from mas arham
import Kamus
import spellCheck
import pre

n_samples = 2000
n_features = 1000
n_topics = 5
n_top_words = 3


def print_top_words(model, feature_names, n_top_words):
    for topic_idx, topic in enumerate(model.components_):
        print("Topic #%d:" % topic_idx)
        print(" ".join([feature_names[i]
                        for i in topic.argsort()[:-n_top_words - 1:-1]]))
    print()


# read data from transjakarta pre-crawled data
users = []
texts = []
kamus_dt = Kamus.Kamus()
with open('data/transjakarta.json', 'r') as f:
	for line in f:
		all_tweet = json.loads(line)
		tweet = unicodedata.normalize('NFKD', all_tweet['text']).encode('ascii', 'ignore') # convert to ascii
		tweet = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', tweet) # remove url
		tweet = re.sub(r'\&amp\;', '', tweet)  # remove &
		tweet = re.sub(r'\[pic\]', '', tweet)  # remove pic
		tweet = re.sub(r'RT', '', tweet)  # remove RT
		# print(tweet)

		# preprocess
		tweet = pre.processTweet(tweet)
		tweet = kamus_dt.analize(tweet)
		# print(tweet)
		# print()

		users.append(all_tweet['user'])
		texts.append(tweet)
# =============== end reading data =========================

# Use tf-idf features
stopwords_english = nltk.corpus.stopwords.words('english')
with open("stopword_list_tala.txt", "r") as f:
	stopwords_indonesian = f.read().splitlines()

print("Extracting tf-idf features...")
tfidf_vectorizer = TfidfVectorizer(max_df=0.95, min_df=2,
                                   max_features=n_features,
								   stop_words= stopwords_english + stopwords_indonesian)
t0 = time()
tfidf = tfidf_vectorizer.fit_transform(texts)
print("done in %0.3fs." % (time() - t0))



# Doing LDA
print("Fitting LDA models with tfidf features, "
      "n_samples=%d and n_features=%d..."
      % (n_samples, n_features))
lda = LatentDirichletAllocation(n_topics=n_topics, max_iter=10,
                                learning_method='online',
                                learning_offset=50.,
                                random_state=0)
t0 = time()
lda.fit(tfidf)
print("done in %0.3fs." % (time() - t0))

print("\nTopics in LDA model:")
tf_feature_names = tfidf_vectorizer.get_feature_names()
print_top_words(lda, tf_feature_names, n_top_words)
