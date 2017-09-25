import re

def processTweet(tweet):
    # lower case: mengubah menjadi huruf kecil semua
    tweet = tweet.lower()
    # mengubah www.* atau https?://* menjadi 'URL'
    tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))','',tweet)
    # mengubah @username menjadi AT_USER
    tweet = re.sub('@[^\s]+','',tweet)
    # cleansing: hapus semua spasi tambahan
    tweet = re.sub('[\s]+', ' ', tweet)
    # mengubah hashtag #word menjadi word
    tweet = re.sub('#[^\s]+', '', tweet)
    return tweet

def replaceTwoOrMore(s):
    pattern = re.compile(r"(.)\1{1,}", re.DOTALL)
    return pattern.sub(r"\1\1", s)

def tokenize(text):
	text = text.lower()
	text = re.compile(u"[^\w\n ]|\xe2",re.UNICODE).sub(" ", text)
	text = text.split()
	return text