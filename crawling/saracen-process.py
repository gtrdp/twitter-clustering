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
	unique_id = []
	unique_text = []

	with open('saracen.json', 'r') as f:
		for line in f:
			tweet = json.loads(line)
			# tweet_ascii = unicodedata.normalize('NFKD', tweet['text']).encode('ascii', 'ignore')
			id_str = tweet['id_str']
			tweet_txt = tweet['text']
			# tokens = preprocess(tweet_ascii)
			# print(tokens)

			# check for duplicated tweet id
			if id_str not in unique_id:
				unique_id.append(id_str)
				with open('saracen-preprocessed.json', 'a') as file:
					file.write(json.dumps(tweet) + "\n")

			# check for duplicated tweet text
			if tweet_txt not in unique_text:
				unique_text.append(tweet_txt)
				with open('saracen-unique.json', 'a') as file:
					file.write(json.dumps(tweet) + "\n")

	unique_id = set(unique_id)
	print unique_id
	print len(unique_id)
