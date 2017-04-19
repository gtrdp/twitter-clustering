LogBook
-------
- [April](https://github.com/gtrdp/masters-thesis-guntur/blob/master/LogBook/00-august.md)

**To-Do**

- How to visualize: voronoi tree map, cartesian plot
- Different clustering algorithms: hierarchical clustering (top-down, bottom-up), partitional clustering (centroid-based, density-based)

April #1
---------
Target this week:

- Working code with visualization
	- Using preprocessed data from Mas Arham
	- Using mainstream online media
- DBI is also counted (as discussed in the meeting).

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
	
- **Tue Apr  4 09:42:00 WIB 2017**
	- 	Preprocessing: remove RT, via, URL, unicode characters (convert to string if possible), remove hastags (or separate hashtags and regular term)?.
	-  From python to web based graph: https://github.com/wrobstory/vincent
	-  Discussion about text (document) clustering:
		-  https://www.researchgate.net/post/What_is_the_best_algorithm_for_Text_Clustering
		-  http://datascience.stackexchange.com/questions/979/algorithms-for-text-clustering
		-  Latent Dirichlet Allocation (LDA)
		-  k-Means
		-  Latent Semantic Analysis
		-  Ontology based clustering
		-  Hierarchical clustering
	- DBI implementation in Python (and also other index in text clustering):
		- http://www.turingfinance.com/clustering-countries-real-gdp-growth-part2/
	- Visualization options:
		- No text are presented, possibly only the keywords. When the pointer hovers on a particular point, the full text (tweet) appears.
	- Interesting bookmarks:
		- http://scikit-learn.org/stable/auto_examples/text/document_clustering.html
		- http://blog.echen.me/2011/08/22/introduction-to-latent-dirichlet-allocation/
		- https://tedunderwood.com/2012/04/07/topic-modeling-made-just-simple-enough/
		- **Simply comprehensive** http://brandonrose.org/clustering
		- http://brandonrose.org/top100
		- http://www.cs.duke.edu/courses/spring14/compsci290/assignments/lab02.html
		- http://nlpforhackers.io/recipe-text-clustering/
		- http://datascience.stackexchange.com/questions/979/algorithms-for-text-clustering
		- http://harrywang.github.io/document_clustering/
		- Several indices in clustering: http://www.turingfinance.com/clustering-countries-real-gdp-growth-part2/
	- Visualize the performance of the clustering as well.

- **Wed Apr  5 10:30:58 WIB 2017**
	- Location based crawling of Twitter data using native Twitter's Python library requires a point and radius.
	- Tutorial on using data frame in Python (pandas)
		- https://www.datacamp.com/community/tutorials/pandas-tutorial-dataframe-python#gs.6Yqsa1k
	- Trying to make http://brandonrose.org/clustering works (took most of the time).
		- The program ran until clustering, got a problem on visualization.
		- The MDS process took hours of running time. Very long list length might cause the problem.

- **Thu Apr  6 08:48:57 WIB 2017**
	- Continue making the brandon's code works.
		- Tested using 1000 samples: works fine.
		- Tested using 2000 samples: works fine, took a couple of minutes.
	- Indonesian popular online news RSS:
		- http://monosbit.blogspot.co.id/2015/08/daftar-rss-feed-website-populer.html
	- **Question:** clustering result always changes?
	- Got the first working clustering with visualization. Problems:
		- Some words appear more than once.
		- The legend of the graph overlaps the main cluster image.
	- Progress report meeting.

- **Fri Apr  7 15:58:47 WIB 2017**
	- Writing PPTI proposal.
		- Kerjasama skema konsorsium ABG (Lembaga Akademik/ Perguruan Tinggi/ Lembaga Litbang, Business dan Government). Diutamakan adanya kerjasama terkait pengadaan pemerintah (produk/ komponen).
		- Road Map 3 Tahun	
	- Output:
		- Prototipe laik industri
		- Dokumen Detail Engineering Design dari prototype laik industri yang dibuat
		- Dokumen hasil uji simulasi prototipe laik industri di laboratorium dengan kondisi sesungguhnya
		- Dokumen hasil uji Prototype laik industri yang sudah mengalami pengujian dalam lingkungan yang sesungguhnya.
	- Outcome:
		- Peningkatan TKDN
		- Peningkatan daya kompetisi industri
		- Adanya produk hasil pengembangan industri
		- Mengurangi ketergantungan teknologi dari luar
		- Penghematan devisa dan peningkatan devisa

April #2
--------
- **Mon Apr 10 08:44:49 WIB 2017**
	- Writing proposal.
	- To do:
		- BAB 2: Komparasi Sebutkan software analisis yang sudah tersedia: elastic search, kibana, dll Bandingkan dengan komparasi komparasi produk lain, sebutkan keunggulan (berikan chapter khusus dengan poin poin). Bandingkan dengan paten juga https://www.nodeflux.io/about
		- BAB 6: Seperti yang ada pada proposal SUVI, dengan pembagian seperti di buku panduan
WBS: Analisis Sentimen, Clustering, Visualisasi, Integrasi
WP: menyesuaikan
		- BAB 8: 3 tahun, samakan dengan suvi
		- Sharing pembiayaan: Dijabarkan dalam tabel per tahun
	- Keywords for transjakarta research (with PT Aino): lokasi, orang, ketidak nyamanan transjakarta

- **Tue Apr 11 09:43:04 WIB 2017**
	- Revising proposal.

- **Wed Apr 12 08:56:50 WIB 2017**
	- Nice tool for text clustering (including visualization):
		- https://carrotsearch.com
	- Voronoi treemap visualization: good way to visualize the result.

- **Thu Apr 13 11:30:38 WIB 2017**
	- Teknologi peranti lunak yang memungkinkan para pemangku jabatan di pemerintahan untuk mengetahui isu-isu terkini dari sosial media dan sentimennya, guna bahan pertimbangan obyektif dalam mengambil kebijakan strategis.
	- Informasi teknis proposal:
		- NIDN: 0020096904
		- No TKT PPTI: 3029967576
		- No Reg Proposal: 277466
	
- **Fri Apr 14 07:49:52 WIB 2017**
	- Good Friday.

April #3
--------
- **Mon Apr 17 07:49:52 WIB 2017**
	- Visualizing document clustering using scatter plot:
		- http://stats.stackexchange.com/questions/49313/r-visualizing-document-clustering-results
		- if you are trying to validate your results in some way, consider graphing cluster metrics such as cohesion and separation, or a silhouette plot
	- Silhouette plot to see the cluster performance.
		- https://en.wikipedia.org/wiki/Silhouette_(clustering)
		- https://de.wikipedia.org/wiki/Silhouettenkoeffizient
	- Find out what do these coefficients mean:
		- Homogeneity: 0.537
		- Completeness: 0.597
		- V-measure: 0.565
		- Adjusted Rand-Index: 0.519
		- Silhouette Coefficient: 0.008
	- Learning how the code works.
	- Silhouette analysis on python:
		- http://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_silhouette_analysis.html
		- https://stats.stackexchange.com/questions/10540/how-to-interpret-mean-of-silhouette-plot

- **Tue Apr 18 12:53:38 WIB 2017**
	- Meeting Big Data Project.

- **Wed Apr 19 06:29:20 WIB 2017**
	- Graduation Day.
	
- **Thu Apr 20 06:29:20 WIB 2017**
	- Silhouette Analysis.