import tweepy,sys,jsonpickle

consumer_key = '5al1l35t3IOaw8tLYSfbVicun'
consumer_secret = 'Utu7s83k8JMBqMuh9cnsd6RQY3l1Eio6oBht0xdcKfWGWmz30z' 
OAUTH_TOKEN = '282111686-OJG5ioJomj199EXDqHIPf1gwU1VTBwTm2bbDdyPo'
OAUTH_TOKEN_SECRET = 'wBI1jpq68bKh96CYyPAAbpC5nQBoQvBO3lAGSIFKOnIyP'

#qry='transjakarta OR TransJakarta OR busway'
qry='saracen OR Saracen'
maxTweets = 10000 # Isi sembarang nilai sesuai kebutuhan anda
tweetsPerQry = 100  # Jangan isi lebih dari 100, ndak boleh oleh Twitter
fName='saracen.json' # Nama File hasil Crawling


#auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
#auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)


auth = tweepy.AppAuthHandler(consumer_key,consumer_secret)


api = tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
print api

if (not api):
    sys.exit('Autentikasi gagal, mohon cek "Consumer Key" & "Consumer Secret" Twitter anda')



sinceId=None;max_id=-1;tweetCount=0
print("Mulai crawling {0} tweets".format(maxTweets))
with open(fName,'w') as f:
    while tweetCount < maxTweets:
        try:
            if (max_id <= 0):
                if (not sinceId):
                    new_tweets=api.search(q=qry,count=tweetsPerQry)
                else:
                    new_tweets=api.search(q=qry,count=tweetsPerQry,since_id=sinceId)
            else:
                if (not sinceId):
                    new_tweets=api.search(q=qry,count=tweetsPerQry,max_id=str(max_id - 1))
                else:
                    new_tweets=api.search(q=qry,count=tweetsPerQry,max_id=str(max_id - 1),since_id=sinceId)
            if not new_tweets:
                print('Tidak ada lagi Tweet ditemukan dengan Query="{0}"'.format(qry));break
            for tweet in new_tweets:
                f.write(jsonpickle.encode(tweet._json,unpicklable=False)+'\n')
            tweetCount+=len(new_tweets)
            sys.stdout.write("\r");sys.stdout.write("Jumlah Tweets telah tersimpan: %.0f" %tweetCount);sys.stdout.flush()
            max_id=new_tweets[-1].id
        except tweepy.TweepError as e:
            print("some error : " + str(e));break 
print ('\nSelesai! {0} tweets tersimpan di "{1}"'.format(tweetCount,fName))
