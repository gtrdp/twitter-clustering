import json
import re
import unicodedata

emoticons_str = r"""
    (?:
        [:=;] # Eyes
        [oO\-]? # Nose (optional)
        [D\)\]\(\]/\\OpP] # Mouth
    )"""

regex_str = [
	emoticons_str,
	r'<[^>]+>',  # HTML tags
	r'(?:@[\w_]+)',  # @-mentions
	r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)",  # hash-tags
	r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+',  # URLs

	r'(?:(?:\d+,?)+(?:\.?\d+)?)',  # numbers
	r"(?:[a-z][a-z'\-_]+[a-z])",  # words with - and '
	r'(?:[\w_]+)',  # other words
	r'(?:\S)'  # anything else
]

tokens_re = re.compile(r'(' + '|'.join(regex_str) + ')', re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^' + emoticons_str + '$', re.VERBOSE | re.IGNORECASE)


def tokenize(s):
	return tokens_re.findall(s)


def preprocess(s, lowercase=False):
	tokens = tokenize(s)
	print(tokens)
	if lowercase:
		tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
	return tokens

if __name__ == '__main__':
	with open('data/stream_transjakarta_2017-08-18.json', 'r') as f:
		for line in f:
			tweet = json.loads(line)
			tweet_ascii = unicodedata.normalize('NFKD', tweet['text']).encode('ascii', 'ignore')
			tokens = preprocess(tweet_ascii)
			# print(tokens)