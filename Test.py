import gensim
import tensorflow
import os




root_path =
if not os.path.exists((root_path + filename).strip('.zip')):
    zipfile.ZipFile(root_path+filename).extractall()

sentences = word2vec.Text8Corpus((root_path + filename).strip('.zip'))


class MySentences(object):
    def __init__(self, dirname):
        self.dirname = dirname

    def __iter__(self):
        for fname in os.listdir(self.dirname):
            for line in open(os.path.join(self.dirname, fname)):
                yield line.split()

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
model = word2vec.Word2Vec(sentences, iter=10, min_count=10, size=300, workers=4)

print(model.wv['the'])

print(model.wv.index2word[0], model.wv.index2word[1], model.wv.index2word[2])