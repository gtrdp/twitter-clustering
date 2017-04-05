#!/usr/bin/env python

"""clustering-kmeans.py: Tweet clustering using kmeans."""
from __future__ import print_function
__author__ = "Guntur DP"
__email__ = "guntur.dharma@gmail.com"
__status__ = "Development"


import pandas as pd
import numpy as np
import pandas as pd
import nltk
import re
import os
import codecs
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.cluster import KMeans
from sklearn.externals import joblib
from nltk.stem.snowball import SnowballStemmer



# read the data, preprocessing involves:
# - removing URLS, special characters
# - all to small letters
raw_data = pd.read_csv('data.csv')
# replace URL
raw_data = raw_data.replace(['http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '[pic]'], ['',''], regex=True)
users = raw_data['user'].tolist()
texts = [x.lower() for x in raw_data['text'].tolist()]

# Stopwords, stemming, and tokenizing
stopwords_english = nltk.corpus.stopwords.words('english')
with open("stopword_list_tala.txt", "r") as f:
	stopwords_indonesian = f.read().splitlines()
stemmer = SnowballStemmer("english")

def tokenize_and_stem(text):
    # first tokenize by sentence, then by word to ensure that punctuation is caught as it's own token
    tokens = [word for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
    filtered_tokens = []
    # filter out any tokens not containing letters (e.g., numeric tokens, raw punctuation)
    for token in tokens:
        if re.search('[a-zA-Z]', token):
            filtered_tokens.append(token)
    stems = [stemmer.stem(t) for t in filtered_tokens]
    return stems


def tokenize_only(text):
    # first tokenize by sentence, then by word to ensure that punctuation is caught as it's own token
    tokens = [word.lower() for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
    filtered_tokens = []
    # filter out any tokens not containing letters (e.g., numeric tokens, raw punctuation)
    for token in tokens:
        if re.search('[a-zA-Z]', token):
            filtered_tokens.append(token)
    return filtered_tokens

# not super pythonic, no, not at all.
# use extend so it's a big flat list of vocab
totalvocab_stemmed = []
totalvocab_tokenized = []
for i in texts:
	allwords_stemmed = tokenize_and_stem(i)  # for each item in 'synopses', tokenize/stem
	totalvocab_stemmed.extend(allwords_stemmed)  # extend the 'totalvocab_stemmed' list

	allwords_tokenized = tokenize_only(i)
	totalvocab_tokenized.extend(allwords_tokenized)

vocab_frame = pd.DataFrame({'words': totalvocab_tokenized}, index = totalvocab_stemmed)
print('there are ' + str(vocab_frame.shape[0]) + ' items in vocab_frame')
vocab_frame.to_csv('vocab_frame.csv')
#
#
#
# # tfidf
# # define vectorizer parameters (tuning parameters)
# tfidf_vectorizer = TfidfVectorizer(max_df=0.8, max_features=200000,
# 								   min_df=10, stop_words=stopwords_english + stopwords_indonesian,
# 								   use_idf=True, ngram_range=(1, 2))
#
# tfidf_matrix = tfidf_vectorizer.fit_transform(texts)  # fit the vectorizer
# # print(tfidf_matrix.shape)
# terms = tfidf_vectorizer.get_feature_names()
# dist = 1 - cosine_similarity(tfidf_matrix)
#
# # print(tfidf_matrix)
#
#
# # k-means clustering
# num_clusters = 5
# km = KMeans(n_clusters=num_clusters)
# km.fit(tfidf_matrix)
# clusters = km.labels_.tolist()
#
# # store the clustering result
# # joblib.dump(km,  'doc_cluster.pkl')
# # load the clustering result
# # km = joblib.load('doc_cluster.pkl')
# # clusters = km.labels_.tolist()
#
# # creating data frame to store the files
# tweets = {'user': users, 'text': texts, 'cluster': clusters}
# clustered_data = pd.DataFrame(tweets, index = [clusters] , columns = ['user', 'text', 'cluster'])
# print(clustered_data['cluster'].value_counts())
#
#
#
# # finding the top n words of each cluster
# print("Top terms per cluster:")
# print()
# # sort cluster centers by proximity to centroid
# order_centroids = km.cluster_centers_.argsort()[:, ::-1]
#
#
# for i in range(num_clusters):
# 	print("Cluster %d words:" % i)
#
# 	for ind in order_centroids[i, :7]:
# 		print(' %s' % vocab_frame.ix[terms[ind].split(' ')].values.tolist()[0][0], end=',')
# 	print()  # add whitespace
# 	print()  # add whitespace
#
# 	# print("Cluster %d titles:" % i, end='')
# 	# for title in clustered_data.ix[i]['text'].values.tolist():
# 	# 	print(' %s,' % title, end='')
# 	# print()  # add whitespace
# 	# print()  # add whitespace
#
# print()
# print()
