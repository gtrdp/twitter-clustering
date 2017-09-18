#!/usr/bin/env python
import json

DEBUG = False

import sys
import tweepy
import time

#consumer_key = 'HcMP89vDDumRhHeQBYbE3Asnp'
#consumer_secret = 'kcXfsNyBl7tan1u2DgV7E10MpsVxhbwTjmbjp3YL9XfDdMJiYt'
#access_key = '67882386-IXbLKaQEtTbZF9yotuLTjgitqjwBkouIstmlW4ecG'
#access_secret = 'SyVrXlIDkidYr3JlNiTQ8tjZ973gIKy5mfpEwFpQWN3Gy'

consumer_key = 'Mcof8aJtJVDqQwz4OMDn2AyZu'
consumer_secret = 'mjsHber2Gj79uc2unbzSRdwGyNyZGjEPBEn4ZHXQZW8FeGeSkv'
access_key = '833745600743079936-hK2K3umAtnfYYuLGLDwD7uzj9ssPCDU'
access_secret = '2Odz7Cky2gb3dZJsO1E65zNL8i84ZnoxLrM9uihSEDb6M'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)



class CustomStreamListener(tweepy.StreamListener):

    def __init__(self, data_dir):
        # query_fname = format_filename(query)
        time_now = time.strftime("%Y-%m-%d_%H.%M.%S")
        self.outfile = "%s/stream_%s.json" % (data_dir, time_now)

    def on_data(self, data):
        try:
            with open(self.outfile, 'a') as f:
                f.write(data)
                print(data)
                return True

        except BaseException as e:
            print("Error on_data: %s" % str(e))
            time.sleep(5)
        return True

    def on_error(self, status_code):
        print >> sys.stderr, 'Encountered error with status code:', status_code
        return True # Don't kill the stream

    def on_timeout(self):
        print >> sys.stderr, 'Timeout...'
        return True # Don't kill the stream

# run the code with try to handle the exception
try:
    sapi = tweepy.streaming.Stream(auth, CustomStreamListener('twitter-data'))
    sapi.filter(track=["transjakarta", "trans jakarta", "bus way", "busway"], languages=["in"])
except:
    pass
