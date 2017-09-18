LogBook
=======
- [April](https://github.com/gtrdp/twitter-clustering/blob/master/LogBook/00-april.md)
- [May](https://github.com/gtrdp/twitter-clustering/blob/master/LogBook/01-may.md)
- [June](https://github.com/gtrdp/twitter-clustering/blob/master/LogBook/02-june.md)
- [July](https://github.com/gtrdp/twitter-clustering/blob/master/LogBook/03-july.md)

August #1
---------
- **Mon Jul 31 16:02:53 WIB 2017**
	- Pak Is Public Defense.
- **Thu Aug  1 11:04:05 WIB 2017**
	- I-Sys Web.
- **Thu Aug  2 11:04:05 WIB 2017**
	- I-Sys Web.
- **Thu Aug  3 11:04:05 WIB 2017**
	- Weekly Meeting.
	- BTM implementation:
		- https://github.com/xiaohuiyan/BTM
		- https://github.com/xiaohuiyan/OnlineBTM
	- Visualization library: Plot.ly

August #2
---------
- **Mon Aug  7 14:35:52 WIB 2017**
	- Lunch with Jarkom.
	- Got the recommendation letter.
- **Tue Aug  8 14:35:52 WIB 2017**
	- Worked at DSSDI.
	- Visualization options:
		- pie chart -> sentiment 
		- scatter plot -> cluster
		- bar chart -> number of tweets about transjakarta over a period of time, with corresponding sentiments
			- bar chart per day (hours).
		- word cloud
		- a frame containing corresponding tweets, when s/o clicks over a bar, the contents change. p.s. thus save also the tweet number
		- text about statistics (total tweets a week, percent positive, percent negative, and neutral)
		- Tree Maps (Foam Tree), hierarchical result
		- tweet location heatmap.
	- Installing Jupyter notebook
- **Wed Aug  9 11:12:23 WIB 2017**
	- None.
- **Thu Aug 10 11:21:21 WIB 2017**
	- Starting to create an automated crawling data.
	- Geobox: http://boundingbox.klokantech.com
	- Designing the mockup.
- **Fri Aug 11 09:58:36 WIB 2017**
	- Installing spark standalone with ubuntu vm.
		- https://roshansanthosh.wordpress.com/2016/02/23/apache-spark-pyspark-standalone-installation-on-ubuntu-14-04/
	- Interesting to learn notebook
		- http://jadianes.me/spark-py-notebooks/
		- https://blog.sicara.com/get-started-pyspark-jupyter-guide-tutorial-ae2fe84f594f

August #3
---------
- **Mon Aug 14 14:15:40 WIB 2017**
	- Configuring remote jupyter notebook [FAILED].
	- Local pyspark installation completed.
	- https://spark.apache.org/docs/latest/rdd-programming-guide.html
	- Double check if the path is correct or the file exists as there is no error message if file does not exist.
		- http://www.learn4master.com/big-data/pyspark/pyspark-check-if-file-exists
- **Tue Aug 15 14:03:58 WIB 2017**
	- Meeting Yuk app.
		- Fixing bugs.
- **Wed Aug 16 15:31:14 WIB 2017**
	- Learn Spark and LDA.
- **Thu Aug 17 09:11:09 WIB 2017**
	- Indonesian Independence Day.
- **Fri Aug 18 09:11:09 WIB 2017**
	- Meeting Yuk app.

August #4
---------
- **Mon Aug 21 14:00:10 WIB 2017**
	- Creating cronjobs for data acquisition.
- **Wed Aug 23 14:01:12 WIB 2017**
	- Meet Pak Widyawan, some insights:
		- http://www.trackur.com
		- http://www.ebdesk.com
		- http://keyhole.co -> very nice for visualization
		- https://gephi.org
		- https://nodexl.codeplex.com
- **Wed Aug 23 14:01:12 WIB 2017**
	- Work together for thursday's jakarta demo (Hanura OSO).
- **Thu Aug 24 10:46:20 WIB 2017**
	- Save location (text) as text cloud or rank.
	- Got this error:

```
requests.exceptions.SSLError: HTTPSConnectionPool(host='stream.twitter.com', port=443): Max retries exceeded with url: /1.1/statuses/filter.json?delimited=length (Caused by SSLError(SSLError(1, u'[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:765)'),))
```
- **Fri Aug 25 18:20:29 WIB 2017**
	- an example of Twitter's JSON
		- https://gist.github.com/hrp/900964
		- https://twitter.com/statuses/ID to retrieve original tweet
	- Twitter's enterprise API
		- https://gnip.com
	- LDA in Spark
		- https://github.com/apache/spark/blob/master/examples/src/main/python/mllib/latent_dirichlet_allocation_example.py

August #5
---------
- **Mon Aug 28 22:19:00 WIB 2017**
	- Starting cronjobs to crawl the data.
	- Working on the saracen JSON.
		- It turns out that it does not contain duplicated data.
		- It contains 10082 lines of unique tweed id.
		- Apparently, it contains lots of retweets as it only contains of unique 3505 lines of tweet text.
- **Tue Aug 29 09:21:41 WIB 2017**
	- Try to run multiple data collection streamer.
	- Crontab formula is now working, but be aware of (possible) duplicated id.
	- Double crawlers (indonesian and general) are now running.
- **Wed Aug 30 11:18:34 WIB 2017**
	- Figure out how to handle exceptions and keep the program up and running.