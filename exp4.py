from gensim.models.doc2vec import Doc2Vec, TaggedDocument
import gensim
import gensim.downloader as api

dataset = api.load("text8")

data = [d for d in dataset]
print(data[0])