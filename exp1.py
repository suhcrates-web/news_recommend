from gensim.models import Doc2Vec

class Word2VecCorpus:
    def __init__(self, fname):
        self.fname = fname
    def __iter__(self):
        with open(self.fname, encoding = 'utf-8') as f:
            for doc in f:
                yield doc.split()