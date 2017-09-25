LogBook
=======
- [April](https://github.com/gtrdp/twitter-clustering/blob/master/LogBook/00-april.md)
- [May](https://github.com/gtrdp/twitter-clustering/blob/master/LogBook/01-may.md)
- [June](https://github.com/gtrdp/twitter-clustering/blob/master/LogBook/02-june.md)
- [July](https://github.com/gtrdp/twitter-clustering/blob/master/LogBook/03-july.md)

September #1
------------
- **Wed Sep  6 10:12:27 WIB 2017**
	- Making the dataset available.

September #2
------------
- **Mon Sep 11 10:47:22 WIB 2017**
	- Meet pak Selo.
- **Tue Sep 12 09:33:08 WIB 2017**
	- Meet Pak Widyawan.
- **Thu Sep 14 09:33:08 WIB 2017**
	- BigData Meeting.
		- event based NLP analysis.
		- Big Data Team:
		- https://docs.google.com/document/d/1Lmzdtaj0M3spP5YpYSLAKjE9BBv10mrMBrkBqtfPiAQ/edit
- **Thu Sep 14 09:33:08 WIB 2017**
	- -
- **Fri Sep 15 09:33:08 WIB 2017**
	- Dinner with Taiki.

September #3
------------
- **Mon Sep 18 09:46:10 WIB 2017**
	- Starting using LDA in spark. By reading the already coded source code.
		- https://databricks-prod-cloudfront.cloud.databricks.com/public/4027ec902e239c93eaaa8714f173bcfc/3741049972324885/3783546674231782/4413065072037724/latest.html
		- https://medium.com/zero-gravity-labs/lda-topic-modeling-in-spark-mllib-febe84b9432

- **Tue Sep 19 09:46:10 WIB 2017**
	- https://researchers.mq.edu.au/en/persons/josef-pieprzyk/network/

September #4
------------
- **Mon Sep 25 14:31:33 WIB 2017**
	- Some specs:
		- **NEWS**
			- Dampak ipoleksosbud media opini (topics) (pie)
			- Dampak ipoleksosbud kabinet kinerja (topics) (pie)
			- sentimen kabinet kerja (pie)
			- sentimen portal opini (pie)
			- Dampak ipoleksosbud kabinet kinerja (topics, per hour) (barchart)
			- histogram for news counts (bar)
			- tag cloud:
				- entitas lokasi
				- entitas person
				- entitas organisasi
			- statistics in text
			- news list (judul, url, sentiment, date, date crawled)
			- not realtime, batched, search feature available
		- **FACEBOOK**
			- sentiment in line chart
			- sentiment in bar chart
			- word cloud
			- possibly from facebook pages or open groups
			- fb metrics
		- **TWITTER ANALYSIS**
			- realtime clock
			- tweet frequency (line or bar chart)
			- top 20 hashtags (stacked bar chart)
			- top 20 hashtags in hourly barchart 
			- top 10 active twitter user (tweet count, in time window, barchart)
			- follower segmentation (pie chart)
			- hashtag tree by user
			- estimated reach
			- impression
			- account ontology, graph (who tweet what) 
		- **NETWORKS**
			- Index pattern + field
			- structured data.
	- Install Elastic Search and Kibana in Mac:
		- https://gist.github.com/djonsson/6e06de4e28a6148b7a1e
	- Hadoop+Spark vs ES+Kibana:
		- https://www.quora.com/Why-do-people-use-Hadoop-or-Spark-when-there-is-ElasticSearch-Why-shouldnt-ElasticSearch-be-used-as-a-data-warehouse
	- Some links about ES:
		- https://www.elastic.co/guide/en/kibana/current/getting-started.html
		- https://www.digitalocean.com/community/tutorials/how-to-use-kibana-dashboards-and-visualizations
		- https://www.youtube.com/watch?v=mMhnGjp8oOI
		- https://www.youtube.com/watch?v=Kqs7UcCJquM
		- https://logz.io/blog/kibana-visualizations/
		- https://www.linkedin.com/pulse/creating-custom-kibana-visualizations-rittik-banik