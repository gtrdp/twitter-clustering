import csv

DEBUG = False

class Kamus:
    def __init__(self):
        self.kamus = []
        self.kamusJW = []
        self.inpKamus = csv.reader(open('kamus.csv', 'rb'), delimiter=',', quotechar='|')
        self.inpKamusJW = csv.reader(open('kamus_jawa.csv', 'rb'), delimiter=',', quotechar='|')

    def analize(self, text):
        for row in self.inpKamus:
            self.kamus.append(row)
        for row in self.inpKamusJW:
            self.kamusJW.append(row)
        data_kamus = self.kamus + self.kamusJW
        data = self.getFeatureVector(text,data_kamus)
        return ' '.join(data)

    def getFeatureVector(self, tweet, kamus):
        featureVector = []
        words = tweet.split()
        for w in words:
            for baris in kamus:
                kata = baris[0]
                ubah = baris[1]
                if (w == kata):
                    w = ubah
                    break
            if (w is None):
                continue
            else:
                featureVector.append(w.lower())
        return featureVector
