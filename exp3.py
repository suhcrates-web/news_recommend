from gensim.test.utils import common_texts
from gensim.models.doc2vec import Doc2Vec, TaggedDocument

def make_doc2vec_data(data, column, t_document = False):
    data_doc = []
    for tag, doc in zip(data.index, data[column]):
        doc = doc.split(" ")
        data_doc.append(([tag], doc))

    if t_document:
        data = [TaggedDocument(words =text) for tag, text in data_doc]
        return data
    else:
        return data_doc

    