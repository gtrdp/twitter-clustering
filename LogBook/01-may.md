LogBook
=======
- [April](https://github.com/gtrdp/twitter-clustering/blob/master/LogBook/00-april.md)
- [May](https://github.com/gtrdp/twitter-clustering/blob/master/LogBook/01-may.md)

Algorithm Check List
--------------------
| Algorithm |     Done    |  Remarks  |
|---------|-----------|---------|
| k-Means | Done        | Using bi gram; evaluated using silhouette analysis |
| Statistical Analysis | Done | Visualization is not yet done. |
| Ward hierarchical clustering  |         |           |
| DBSCAN |        |           |
| Latent Dirichlet Allocation | Done |           |
| Non-negative Matrix Factorization |        |           |

Vectorizer:

- Hashingvectorizer
- TFIDF

Parameters:

- TF-IDF n-gram: 2-gram, 3-gram, etc.
- Using DBI and Silhouette
- Jaccard and cosine similarity
- Word (or n-gram) frequencies are typical units of analysis when working with text collections.
- Use PCA with different dimension, plot the result.

**To-Do**

- How to visualize: voronoi tree map, cartesian plot
- Different clustering algorithms: hierarchical clustering (top-down, bottom-up), partitional clustering (centroid-based, density-based)

May #1
---------
- **Mon May  1 10:09:57 WIB 2017**
	- May Day.

- **Tue May  2 07:02:40 WIB 2017**
	- Trying new dataset from Mas Arham.
	- Tempo dataset (n=50) achieves best clustering quality (silhouette) on k=26.
	- PCA on clustering:
		- https://stats.stackexchange.com/questions/157621/how-would-pca-help-with-a-k-means-clustering-analysis
	- **To-Do:**
		- create a simulation to prove whether PCA disrupts clustering or otherwise.

- **Wed May  3 06:44:57 WIB 2017**
	- InAES.

- **Thu May  4 10:17:49 WIB 2017**
	- Progress report.
		- Statistic visualization: with time series, e.g., january-april; how many tweets per day or permonth.
		- Decide what to do first: clustering then sentiment or sentiment then clustering.
		- Sort the keyterms from statistical method, then use the corresponding tweet to perform clustering.
		- Lookfor carrotsearch paper: it may reveal some methods.

- **Sat May  6 06:27:44 WIB 2017**
	- Try to clone the repository.
	```
	ssh-agent bash -c 'ssh-add ~/id_rsa; git clone guntur.dharma@git.dev.ugm.ac.id:bigdata-tj/NLP.git'
	```

May #2
------
- **Mon May 8 14:48:50 WIB 2017**
	- Preparing PPTI presentation

- **Tue May 9 14:48:50 WIB 2017**
	- Headed to Jakarta for PPTI presentation. Presentation notes:
		- keamanan informasi? di simpan di mana? data center? tier 3 ISO 27001
		- hoax?
		- isu public begitu dinamis, dan demand akan itu sangat banyak
		- ada direktorat khusus di kominfo untuk analysis sosial tok, dan bagaimana merespon hal itu, jangan sampai membawa efek negatif ke publik
		- banyak juga penawaran, mulai dari 50jt per bulan, 1M per tahun, dengan banyak keyword dan feature -> tidak terlalu unik
		- lebih banyak yakin dari produk asing
		- keunikan produk ini? karena sudah banyak. -> data non publik; mengembangkan algoritma AI; kedaulatan data lebih mudah diberikan karena produk dalam negeri
		- sustainability produk ini? jaminan pasca jual? (PT GT)
		- sampai mana progress saat ini? preliminary research? sudah ada Big data WG->transjakarta, NLP->twitter
		- seberapa banyak data yang sudah dikumpulkan? 50MB twitter 
		- berapa lama proses komputasi yang digunakan? karena data sosial media dari Indonesia sangat besar
	- hasil kepo singkat Pak Novan:
		- reviewer 1 Ir. Djoko Agung Harijadi, M.M.. Sekretaris Ditjen Aplikasi Informatika
		- reviewer 2. Ir Lolly Amalia Abdullah, MSc,  Direktur Kerjasama dan Fasilitasi Kemenparekraf
		- reviewer 3. Dr. Media Anugerah Ayu, M. Sc. , dari Ilkom Sampurna University
		
- **Wed May 10 14:48:50 WIB 2017**
	- Collections of graph in d3.js: https://github.com/d3/d3/wiki/Gallery

- **Thu May 11 19:46:40 WIB 2017**
	- Waisak Day.

- **Fri May 12 14:33:25 WIB 2017**
	- None (SKK Migas).

May #3
------
- **Mon May 15 10:20:03 WIB 2017**
	- Finding important words: http://www.markhneedham.com/blog/2015/02/15/pythonscikit-learn-calculating-tfidf-on-how-i-met-your-mother-transcripts/
	- Word cloud in Python:
		- http://peekaboo-vision.blogspot.co.id/2012/11/a-wordcloud-in-python.html
		- https://github.com/amueller/word_cloud

- **Tue May 16 13:49:15 WIB 2017**
	- Continuing working on statistical analysis.
	- Nice bubble chart example:
		- https://bl.ocks.org/mbostock/4063269
		- https://bl.ocks.org/mbostock/07ec62d9957a29a30e71cad962ff2efd
	- Statistical is now working. ToDo: repair the text appearance (new line).

- **Wed May 17 10:26:39 WIB 2017**
	- Clustering algorithm comparision in `sklearn`:
		- http://hdbscan.readthedocs.io/en/latest/comparing_clustering_algorithms.html
		- http://scikit-learn.org/stable/modules/clustering.html
	- Word (or n-gram) frequencies are typical units of analysis when working with text collections.
	- https://de.dariah.eu/tatom/working_with_text.html
	- LSA in Python: http://mccormickml.com/2015/08/06/document-clustering-example-in-scikit-learn/
	- https://www.quora.com/What-is-most-used-algorithm-for-text-documents-clustering
	- https://github.com/arnab64/textclusteringDBSCAN
	- http://blog.echen.me/2011/08/22/introduction-to-latent-dirichlet-allocation/

- **Thu May 18 07:01:05 WIB 2017**
	- Use PCA with different dimension, plot the result.
	- Topic extraction:
		- Non-negative Matrix Factorization
		- Latent Dirichlet Allocation
	- DBSCAN does not work in high dimensional space
		- https://www.quora.com/Why-DBSCAN-clustering-will-not-work-in-high-dimensional-space
	- https://www.researchgate.net/post/What_is_the_best_distance_measure_for_high_dimensional_data
	- https://en.wikipedia.org/wiki/Clustering_high-dimensional_data

- **Fri May 19 14:57:23 WIB 2017**
	- Test the algorithm using known datasets.

May #4
------
- **Mon May 22 12:43:14 WIB 2017**
	- Try using labeled data.
	- Got a visit from Mas Kuntoro, Mas Canggih, and Putra.
	
- **Tue May 23 17:28:00 WIB 2017**
	- https://en.wikipedia.org/wiki/Clustering_high-dimensional_data
	- Result from labeled dataset:

	```
	reading the files, stemming, and stopwords removal
	3387 documents
	
	TFIDF Vectorizer
	(3387, 10000)
	beginning clustering...
	clustering with N=4
	Top terms per cluster:
	
	Cluster 0 words:
	 sandvik, kent, apple, newton, com, alink, ksand, cookamunga, tourist, bureau,
	
	Cluster 1 words:
	 god, com, one, people, keith, would, say, article, jesus, sgi,
	
	Cluster 2 words:
	 graphics, com, university, posting, image, host, thanks, nntp, computer, would,
	
	Cluster 3 words:
	 space, nasa, henry, access, digex, toronto, gov, pat, would, alaska,
	```

	- Labeled dataset using sklearn implementation:

	```
	Loading 20 newsgroups dataset for categories:
	['alt.atheism', 'talk.religion.misc', 'comp.graphics', 'sci.space']
	3387 documents
	4 categories
	
	Extracting features from the training dataset using TF-IDF
	done in 1.322455s
	n_samples: 3387, n_features: 10000
	
	Clustering sparse data with KMeans(algorithm='auto', copy_x=True, init='k-means++', max_iter=100,
	    n_clusters=4, n_init=1, n_jobs=1, precompute_distances='auto',
	    random_state=None, tol=0.0001, verbose=False)
	done in 4.049s
	
	Homogeneity: 0.379
	Completeness: 0.559
	V-measure: 0.452
	Adjusted Rand-Index: 0.358
	Silhouette Coefficient: 0.005
	
	Top terms per cluster:
	Cluster 0: ___ jpl nasa gov baalke __ kelvin command ron egalon
	Cluster 1: sgi keith livesey objective morality caltech wpd solntze jon moral
	Cluster 2: space com graphics university posting host nntp access like henry
	Cluster 3: god com sandvik people jesus don article bible christian religion
	```
	
- **Wed May 24 08:38:59 WIB 2017**
	- Progress report preparation.
	- Retweet?

- **Thu May 25 08:38:59 WIB 2017**
	- Ascension of Jesus Christ.

- **Fri May 26 08:38:59 WIB 2017**
	- SKK Migas.

May #5
------
- **Mon May 29 14:52:16 WIB 2017**
	- Short text clustering algorithm.
	- https://github.com/rwalk/gsdmm
- **Tue May 30 12:42:49 WIB 2017**
	- https://radimrehurek.com/gensim/
	- http://mccormickml.com/2016/03/25/lsa-for-text-classification-tutorial/
	- Glancing on short text clustering algorithm.

	> Existing works on classification of short text messages integrate every message with meta-information from external information sources such as Wikipedia and WordNet.
	
	- Found in researchgate:

	> Latent Semantic Analysis works good for unknown data with any number of classes. It requires minimum information before hand.
	
	- Possibly good starting point for short text clustering, Word Mover Distance: http://vene.ro/blog/word-movers-distance-in-python.html
	- Conclusion:
		- GDSMM (https://github.com/rwalk/gsdmm)
		- Word Mover Distance
		- Combination with other text source, eg., wikipedia, etc.

- **Rab Mei 31 10:54:48 WIB 2017**
	- Short text datasets:
		- http://davis.wpi.edu/xmdv/datasets/ohsumed.html
		- http://cogcomp.cs.illinois.edu/Data/QA/QC/
		- https://drive.google.com/drive/u/0/folders/0Bz8a_Dbh9Qhbfll6bVpmNUtUcFdjYmF2SEpmZUZUcVNiMUw1TWN6RDV3a0JHT3kxLVhVR2M
		- https://github.com/jacoxu/StackOverflow
		- http://acube.di.unipi.it/datasets/
	- https://www.researchgate.net/post/What_is_a_good_way_to_perform_topic_modeling_on_short_text
	
		> Topic modelling on Twitter has been analysed in various publications. Despite the short and sparse texts LDA (Latent Dirichlet Allocation)has proven to work good on tweets [1]. We could confirm the observations made in this paper, when applying LDA ourself to large twitter corpora. One particularity in this context is that tweets are very focussed and hardly ever discuss more than 1 or 2 topics identified by LDA.
	
		> If you want to stay with TF-IDF or its variations, you must not use length normalization techniques. We found that length normalization for such short texts are not only unmotivated but eve counterproductive [2].
	
		> [1] J. Weng, E.-P. Lim, J. Jiang, and Q. He. TwitterRank: Finding topic-sensitive influential twitterers. In Proc. Int. Conf. on Web Search and Data Mining, pages 261–270, 2010.
	
		> [2] Naveed, N., Gottron, T., Kunegis, J., Che Alhadi, A.: Searching microblogs: Coping with sparsity and document quality. In: CIKM’11: Proceedings of 20th ACM Conference on Information and Knowledge Management. pp. 183–188 (2011) 

- **Thu Jun  1 10:16:46 WIB 2017**
	- The birth of Indonesian Five Pillars.
- **Fri Jun  2 10:16:46 WIB 2017**
	- Text Stemmer:
		- http://blog.pantaw.com/syntatic-proses-text-stemmer-bahasa-indonesia-dengan-python/
		- https://github.com/har07/PySastrawi