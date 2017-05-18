from __future__ import print_function
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import feedparser
import pandas as pd
from sklearn.cluster import DBSCAN
from sklearn import metrics
import numpy as np

if __name__ == "__main__":
	# read the data, preprocessing involves:
	# - removing URLS, special characters
	# - all to small letters
	# read from precrawled twitter tweets
	print("reading the files, stemming, and stopwords removal")
	raw_data = pd.read_csv('output.csv')
	# replace URL
	raw_data = raw_data.replace(
		['http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', "&amp;", "\[pic\]"],
		['', '', ''], regex=True)
	users_long = raw_data['user'].tolist()
	texts_long = [x.lower() for x in raw_data['text'].tolist()]
	users = users_long
	texts = texts_long

	# # read from tempo.co rss
	# tempo_data = feedparser.parse('tempo.xml')
	#
	# users = []
	# texts = []
	# for value in tempo_data['entries']:
	# 	users.append(value['title'])
	# 	texts.append(value['summary'])

	# =============== end reading data =========================


	# tfidf
	# define vectorizer parameters (tuning parameters)
	stopwords_english = nltk.corpus.stopwords.words('english')
	with open("stopword_list_tala.txt", "r") as f:
		stopwords_indonesian = f.read().splitlines()
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
	dist = 1 - cosine_similarity(tfidf_matrix)
	# print(len(terms))
	print(tfidf_matrix.shape)
	# print(len(dist[0]))

	print("beginning clustering...")
	db = DBSCAN(eps=0.7, min_samples=10).fit(tfidf_matrix)
	core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
	core_samples_mask[db.core_sample_indices_] = True
	labels = db.labels_

	# Number of clusters in labels, ignoring noise if present.
	n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)

	print('Estimated number of clusters: %d' % n_clusters_)
	print("Silhouette Coefficient: %0.3f"
		  % metrics.silhouette_score(tfidf_matrix, labels))

