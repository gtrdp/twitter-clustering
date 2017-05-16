from __future__ import print_function
import nltk
from sklearn.feature_extraction.text import CountVectorizer
import feedparser
import numpy as np
import scipy
import operator

# read from tempo.co rss
tempo_data = feedparser.parse('tempo.xml')

users = []
texts = []
for value in tempo_data['entries']:
	users.append(value['title'])
	texts.append(value['summary'])
# =============== end reading data =========================



# word counter
stopwords_english = nltk.corpus.stopwords.words('english')
with open("stopword_list_tala.txt", "r") as f:
	stopwords_indonesian = f.read().splitlines()

cv = CountVectorizer(min_df=0, stop_words=stopwords_english + stopwords_indonesian, max_features=200)
counts = cv.fit_transform(texts)
words = np.array(cv.get_feature_names())
# normalize
# counts = counts / float(counts.max())
print(words[0])

# summing it up together
# looping through the matrix to sum the word counts
cx = scipy.sparse.coo_matrix(counts)

words_dictionary = {}
for document_index, word_index, value in zip(cx.row, cx.col, cx.data):
	# print(type(str(words[word_index])))
	if words[word_index] in words_dictionary:
		# old entry, update
		words_dictionary.update({words[word_index]: words_dictionary[words[word_index]] + value})
	else:
		# new entry
		words_dictionary.update({words[word_index]: value})

words_dictionary = sorted(words_dictionary.items(), key = operator.itemgetter(1), reverse = True)
print(words_dictionary)
