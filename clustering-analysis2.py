#!/usr/bin/env python

"""clustering-analysis.py: """
from __future__ import print_function
__author__ = "Guntur DP"
__email__ = "guntur.dharma@gmail.com"
__status__ = "Development"

import pandas as pd
import nltk
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.cluster import KMeans
from sklearn.externals import joblib
from nltk.stem.snowball import SnowballStemmer
import mpld3
import matplotlib.pyplot as plt
from sklearn.manifold import MDS
import feedparser
from sklearn.metrics import silhouette_samples, silhouette_score
import Similarity
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import csv
import unicodedata
import json
from sklearn.datasets import fetch_20newsgroups
from sklearn.cluster import DBSCAN
import numpy as np

def cluster(epsilon, minsample):
	db = DBSCAN(eps=epsilon_value[epsilon], min_samples=minsample).fit(reduced_data)
	core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
	core_samples_mask[db.core_sample_indices_] = True
	labels = db.labels_

	# Number of clusters in labels, ignoring noise if present.
	n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)

	print("epsilon:", epsilon_value[epsilon],"min sample:",minsample)
	print('Estimated number of clusters: %d' % n_clusters_)
	# print("Silhouette Coefficient: %0.3f"
	# 	  % silhouette_score(reduced_data, labels))
	# silhouette_avg = silhouette_score(reduced_data, labels)
	print()

if __name__ == "__main__":
	# read the data, preprocessing involves:
	# - removing URLS, special characters
	# - all to small letters
	# read from precrawled twitter tweets
	print("reading the files, stemming, and stopwords removal")
	# raw_data = pd.read_csv('output.csv')
	# # replace URL
	# raw_data = raw_data.replace(
	# 	['http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', "&amp;", "\[pic\]"],
	# 	['', '', ''], regex=True)
	# users_long = raw_data['user'].tolist()
	# texts_long = [x.lower() for x in raw_data['text'].tolist()]
	# users = users_long
	# texts = texts_long

	# # read data from transjakarta pre-crawled data
	# users = []
	# texts = []
	# with open('data/Hasil.json', 'r') as f:
	# 	for line in f:
	# 		all_tweet = json.loads(line)
	# 		tweet = unicodedata.normalize('NFKD', all_tweet['text']).encode('ascii', 'ignore')  # convert to ascii
	# 		tweet = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '',
	# 					   tweet)  # remove url
	# 		tweet = re.sub(r'\&amp\;', '', tweet)  # remove &
	# 		tweet = re.sub(r'\[pic\]', '', tweet)  # remove pic
	#
	# 		users.append(all_tweet['user'])
	# 		texts.append(tweet)

	# read from tempo.co rss
	tempo_data = feedparser.parse('tempo.xml')

	users = []
	texts = []
	for value in tempo_data['entries']:
		users.append(value['title'])
		texts.append(value['summary'])

	# # print("Loading 20 newsgroups dataset for categories:")
	# categories = [
	# 	'alt.atheism',
	# 	'talk.religion.misc',
	# 	'comp.graphics',
	# 	'sci.space',
	# ]
	#
	# texts = fetch_20newsgroups(subset='all', categories=categories,
	# 							 shuffle=True, random_state=42)
	# texts = texts.data
	#
	# print("%d documents" % len(texts))
	# print()

	# =============== end reading data =========================

	# Stopwords, stemming, and tokenizing
	stopwords_english = nltk.corpus.stopwords.words('english')
	with open("stopword_list_tala.txt", "r") as f:
		stopwords_indonesian = f.read().splitlines()

	# tfidf
	# define vectorizer parameters (tuning parameters)
	print("TFIDF Vectorizer")
	tfidf_vectorizer = TfidfVectorizer(max_df=0.5, max_features=10000,
									   min_df=2, stop_words=stopwords_english + stopwords_indonesian,
									   use_idf=True)
	# uni-gram bi-gram tri-gram: separated and compare the result
	# kcm and fcm clustering
	# using dbi
	# jaccard and cosine similarity

	tfidf_matrix = tfidf_vectorizer.fit_transform(texts)  # fit the vectorizer
	terms = tfidf_vectorizer.get_feature_names()
	# dist = 1 - cosine_similarity(tfidf_matrix)
	# print(len(terms))
	print(tfidf_matrix.shape)
	# print(len(dist[0]))

	# doing PCA
	print("performing PCA...")
	reduced_data = PCA(n_components=10).fit_transform(tfidf_matrix.toarray())
	# # draw the plot
	# plt.scatter(reduced_data[:,0], reduced_data[:,1])
	# plt.show()


	print("beginning clustering...")
	epsilon_value = range(5,10)
	epsilon = range(0,5)
	minsample = range(4,10)
	silhouette_index = []

	for foo in epsilon:
		for bar in minsample:
			cluster(foo, bar)

	# # draw the plot
	# print("max:",n_clusters[silhouette_index.index(max(silhouette_index))],"(",max(silhouette_index),")")
	# print(len(n_clusters), len(silhouette_index))
	# plt.plot(n_clusters, silhouette_index, 'ro', linestyle="-", color='b')
	# # plt.axis([0, 6, 0, 20])
	# plt.xlabel('n cluster')
	# plt.ylabel('Silhouette')
	# plt.title('Silhouette index on Tempo.co dataset; 3 dimensions')
	# # plt.title('Silhouette index on Twitter dataset (with sentiment)')
	# plt.show()
