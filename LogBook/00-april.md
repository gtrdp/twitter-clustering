LogBook
-------
- [April](https://github.com/gtrdp/masters-thesis-guntur/blob/master/LogBook/00-august.md)

**To-Do**

- Learn DBI
- TF IDF
- Learn how to visualize the data from Google Trends

April #1
---------
- **Sun Apr  2 21:41:15 WIB 2017**
	- Preparing the git repository.
	- Mining twitter using python:
		- https://marcobonzanini.com/2015/03/02/mining-twitter-data-with-python-part-1/
	- Limits in Twitter APIs:
		- https://dev.twitter.com/overview/terms/agreement-and-policy
		- https://dev.twitter.com/rest/public/rate-limiting
	- Google trends might help: https://trends.google.nl/trends/
	- Library for twitter mining: http://tweepy.readthedocs.io/en/v3.5.0/
	- Resources for learning twitter mining:
		- https://github.com/bonzanini/Book-SocialMediaMiningPython
	- Got the minimal working example (not yet pre-processed).

- **Mon Apr  3 11:59:22 WIB 2017**
	- Learn about twitter clustering.
	- Might be interesting: https://github.com/JamesPHoughton/twitter-cluster
	- Downloaded some papers.
	- Nice tools to create geobox
		- http://boundingbox.klokantech.com
		- geobox whole world: ```GEOBOX_WORLD = [-180,-90,180,90]```
		- Jogja and surroundings: ```JOGJA = [109.4763,-8.4557,111.3928,-7.2811]```
	- The streaming API doesn't allow to filter by location AND keyword simultaneously (http://stackoverflow.com/questions/22889122/how-to-add-a-location-filter-to-tweepy-module).
		- https://dev.twitter.com/streaming/overview/request-parameters#locations
	
		> Bounding boxes do not act as filters for other filter parameters. For example track=twitter&locations=-122.75,36.8,-121.75,37.8 would match any tweets containing the term Twitter (even non-geo tweets) OR coming from the San Francisco area.
	
	