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

def cluster(num_clusters):
	# === k-means clustering
	print("clustering with N=%d" % num_clusters)
	km = KMeans(n_clusters=num_clusters, random_state=10)
	# km.fit(tfidf_matrix)
	km.fit(reduced_data)
	clusters = km.labels_.tolist()

	# store the clustering result
	# joblib.dump(km,  'doc_cluster.pkl')
	# load the clustering result
	# km = joblib.load('doc_cluster.pkl')
	# clusters = km.labels_.tolist()


	# creating data frame to store the files
	# tweets = {'user': users, 'text': texts, 'cluster': clusters}
	# clustered_data = pd.DataFrame(tweets, index = [clusters] , columns = ['user', 'text', 'cluster'])
	# print(clustered_data['cluster'].value_counts())

	# if num_clusters == 3:
	# 	# plotting the result
	# 	print("plotting the result to scatter plot")
	# 	for index, val in enumerate(clusters):
	# 		if val == 0:
	# 			c1 = plt.scatter(reduced_data[index, 0], reduced_data[index, 1], c='r', marker='+')
	# 		elif val == 1:
	# 			c2 = plt.scatter(reduced_data[index, 0], reduced_data[index, 1], c='g', marker='o')
	# 		elif val == 2:
	# 			c3 = plt.scatter(reduced_data[index, 0], reduced_data[index, 1], c='b', marker='*')
	#
	# 	plt.show()


	# # finding the top n words of each cluster
	# print("Top terms per cluster:")
	# print()
	# # sort cluster centers by proximity to centroid
	# order_centroids = km.cluster_centers_.argsort()[:, ::-1]
	#
	# cluster_names = {}
	#
	# for i in range(num_clusters):
	# 	print("Cluster %d words:" % i)
	#
	# 	foo = ''
	# 	for ind in order_centroids[i, :10]:
	# 		# print(' %s' % vocab_frame.ix[terms[ind].split(' ')].values.tolist()[0][0].encode('utf-8', 'ignore'), end=',')
	# 		print(' %s' % terms[ind], end=',')
	# 		foo = foo + terms[ind] + ', '
	# 	print()  # add whitespace
	# 	print()  # add whitespace
	# 	cluster_names[i] = foo
	#
	# 	# print("Cluster %d titles:" % i, end='')
	# 	# for title in clustered_data.ix[i]['text'].values.tolist():
	# 	# 	print(' %s,' % title, end='')
	# 	# print()  # add whitespace
	# 	# print()  # add whitespace

	silhouette_avg = silhouette_score(reduced_data, clusters)
	# silhouette_avg = silhouette_score(tfidf_matrix, clusters)
	print("For n_clusters =", num_clusters,
		  "The average silhouette_score is :", silhouette_avg)
	silhouette_index.append(silhouette_avg)
	print()
	print()

	if num_clusters == 14:
		print("Save the result to csv file")
		# convert unicode to ascii
		for idx, val in enumerate(texts):
			if isinstance(val, unicode):
				texts[idx] = unicodedata.normalize('NFKD', val).encode('ascii', 'ignore')

		my_dict = {"cluster": clusters, "text": texts}

		with open('mycsvfile_'+str(num_clusters)+'.csv', 'wb') as f:  # Just use 'w' mode in 3.x
			writer = csv.writer(f)
			writer.writerow(my_dict.keys())
			writer.writerows(zip(*my_dict.values()))

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
	reduced_data = PCA(n_components=3).fit_transform(tfidf_matrix.toarray())
	# # draw the plot
	# plt.scatter(reduced_data[:,0], reduced_data[:,1])
	# plt.show()


	print("beginning clustering...")
	n_clusters = range(2,30)
	silhouette_index = []
	for foo in n_clusters:
		cluster(foo)

	# draw the plot
	print("max:",n_clusters[silhouette_index.index(max(silhouette_index))],"(",max(silhouette_index),")")
	print(len(n_clusters), len(silhouette_index))
	plt.plot(n_clusters, silhouette_index, 'ro', linestyle="-", color='b')
	# plt.axis([0, 6, 0, 20])
	plt.xlabel('n cluster')
	plt.ylabel('Silhouette')
	plt.title('Silhouette index on Tempo.co dataset; 3 dimensions')
	# plt.title('Silhouette index on Twitter dataset (with sentiment)')
	plt.show()
