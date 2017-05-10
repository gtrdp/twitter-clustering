LogBook
-------
- [April](https://github.com/gtrdp/twitter-clustering/blob/master/LogBook/00-april.md)
- [May](https://github.com/gtrdp/twitter-clustering/blob/master/LogBook/01-may.md)

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
		
- **Wed May 10 14:48:50 WIB 2017**
