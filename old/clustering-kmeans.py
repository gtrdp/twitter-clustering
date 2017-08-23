#!/usr/bin/env python

"""clustering-kmeans.py: Tweet clustering using kmeans. Inspired from http://brandonrose.org/clustering#K-means-clustering"""
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


# read the data, preprocessing involves:
# - removing URLS, special characters
# - all to small letters
# read from precrawled twitter tweets
# raw_data = pd.read_csv('data.csv')
# # replace URL
# raw_data = raw_data.replace(['http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', "&amp;", "\[pic\]"], ['','',''], regex=True)
# users_long = raw_data['user'].tolist()
# texts_long = [x.lower() for x in raw_data['text'].tolist()]
# users = users_long[:2000]
# texts = texts_long[:2000]

# read from tempo.co rss
tempo_data = feedparser.parse('tempo.xml')

users = []
texts = []
for value in tempo_data['entries']:
	users.append(value['title'])
	texts.append(value['summary'])

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

totalvocab_stemmed = []
totalvocab_tokenized = []
for i in texts:
	allwords_stemmed = tokenize_and_stem(i)  # for each item in 'synopses', tokenize/stem
	totalvocab_stemmed.extend(allwords_stemmed)  # extend the 'totalvocab_stemmed' list

	allwords_tokenized = tokenize_only(i)
	totalvocab_tokenized.extend(allwords_tokenized)

vocab_frame = pd.DataFrame({'words': totalvocab_tokenized}, index = totalvocab_stemmed)
print('there are ' + str(vocab_frame.shape[0]) + ' items in vocab_frame')
# vocab_frame.to_csv('vocab_frame.csv')



# tfidf
# define vectorizer parameters (tuning parameters)
tfidf_vectorizer = TfidfVectorizer(max_df=0.5, max_features=200000,
								   min_df=2, stop_words=stopwords_english + stopwords_indonesian,
								   use_idf=True, ngram_range=(1, 2))

tfidf_matrix = tfidf_vectorizer.fit_transform(texts)  # fit the vectorizer
terms = tfidf_vectorizer.get_feature_names()
dist = 1 - cosine_similarity(tfidf_matrix)
print(len(terms))
print(tfidf_matrix.shape)
print(len(dist[0]))

# k-means clustering
num_clusters = 5
km = KMeans(n_clusters=num_clusters)
km.fit(tfidf_matrix)
clusters = km.labels_.tolist()

# store the clustering result
# joblib.dump(km,  'doc_cluster.pkl')
# load the clustering result
# km = joblib.load('doc_cluster.pkl')
# clusters = km.labels_.tolist()

# creating data frame to store the files
tweets = {'user': users, 'text': texts, 'cluster': clusters}
clustered_data = pd.DataFrame(tweets, index = [clusters] , columns = ['user', 'text', 'cluster'])
print(clustered_data['cluster'].value_counts())



# finding the top n words of each cluster
print("Top terms per cluster:")
print()
# sort cluster centers by proximity to centroid
order_centroids = km.cluster_centers_.argsort()[:, ::-1]

cluster_names = {}
for i in range(num_clusters):
	print("Cluster %d words:" % i)

	foo = ''
	for ind in order_centroids[i, :7]:
		# print(' %s' % vocab_frame.ix[terms[ind].split(' ')].values.tolist()[0][0].encode('utf-8', 'ignore'), end=',')
		print(' %s' % terms[ind], end=',')
		foo = foo + terms[ind] + ', '
	print()  # add whitespace
	print()  # add whitespace
	cluster_names[i] = foo

	# print("Cluster %d titles:" % i, end='')
	# for title in clustered_data.ix[i]['text'].values.tolist():
	# 	print(' %s,' % title, end='')
	# print()  # add whitespace
	# print()  # add whitespace

print()
print()


# visualize the result
# multi dimensional scaling
MDS()

# convert two components as we're plotting points in a two-dimensional plane
# "precomputed" because we provide a distance matrix
# we will also specify `random_state` so the plot is reproducible.
mds = MDS(n_components=2, dissimilarity="precomputed", random_state=1)

pos = mds.fit_transform(dist)  # shape (n_components, n_samples)

xs, ys = pos[:, 0], pos[:, 1]
print()
print()


# set up colors per clusters using a dict
cluster_colors = {0: '#1b9e77', 1: '#d95f02', 2: '#7570b3', 3: '#e7298a', 4: '#66a61e'}

# define custom toolbar location
class TopToolbar(mpld3.plugins.PluginBase):
	"""Plugin for moving toolbar to top of figure"""

	JAVASCRIPT = """
    mpld3.register_plugin("toptoolbar", TopToolbar);
    TopToolbar.prototype = Object.create(mpld3.Plugin.prototype);
    TopToolbar.prototype.constructor = TopToolbar;
    function TopToolbar(fig, props){
        mpld3.Plugin.call(this, fig, props);
    };

    TopToolbar.prototype.draw = function(){
      // the toolbar svg doesn't exist
      // yet, so first draw it
      this.fig.toolbar.draw();

      // then change the y position to be
      // at the top of the figure
      this.fig.toolbar.toolbar.attr("x", 150);
      this.fig.toolbar.toolbar.attr("y", 400);

      // then remove the draw function,
      // so that it is not called again
      this.fig.toolbar.draw = function() {}
    }
    """

	def __init__(self):
		self.dict_ = {"type": "toptoolbar"}


# create data frame that has the result of the MDS plus the cluster numbers and titles
df = pd.DataFrame(dict(x=xs, y=ys, label=clusters, tweet=users))

# group by cluster
groups = df.groupby('label')

# define custom css to format the font and to remove the axis labeling
css = """
text.mpld3-text, div.mpld3-tooltip {
  font-family:Arial, Helvetica, sans-serif;
}

g.mpld3-xaxis, g.mpld3-yaxis {
display: none; }
"""

# Plot
fig, ax = plt.subplots(figsize=(14, 6))  # set plot size
ax.margins(0.03)  # Optional, just adds 5% padding to the autoscaling

# iterate through groups to layer the plot
# note that I use the cluster_name and cluster_color dicts with the 'name' lookup to return the appropriate color/label
for name, group in groups:
	points = ax.plot(group.x, group.y, marker='o', linestyle='', ms=18, label=cluster_names[name], mec='none',
					 color=cluster_colors[name])
	ax.set_aspect('auto')
	labels = [i for i in group.tweet]

	# set tooltip using points, labels and the already defined 'css'
	tooltip = mpld3.plugins.PointHTMLTooltip(points[0], labels,
											 voffset=10, hoffset=10, css=css)
	# connect tooltip to fig
	mpld3.plugins.connect(fig, tooltip, TopToolbar())

	# set tick marks as blank
	ax.axes.get_xaxis().set_ticks([])
	ax.axes.get_yaxis().set_ticks([])

	# set axis as blank
	ax.axes.get_xaxis().set_visible(False)
	ax.axes.get_yaxis().set_visible(False)

ax.legend(numpoints=1)  # show legend with only one dot

mpld3.display()  # show the plot

# uncomment the below to export to html
html = mpld3.fig_to_html(fig)
# print(html)
with open("result.html", "w") as html_file:
	html_file.write(html)
