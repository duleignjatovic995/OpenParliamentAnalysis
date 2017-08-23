"""
This is a file for analysing topics from parliament based on law statements.
"""
from data import get_data
from preprocess.preprocess_data import preprocess_pipeline
from gensim import models
from time import time

# TODO -> lsa, lsi, lda, hdp


# get data from api
start_t0 = time()
data = get_data.akt_naslov_list()
print('get_data time: ', time() - start_t0)

# transform a list of documents to a bag of words model
start_t1 = time()
bag_of_words, dictionary = preprocess_pipeline(data, min_occur=5, max_occur=1)  # save_dict='fajl'
print('preprocessing time: ', time() - start_t1)

# create tf-idf model
tfidf = models.TfidfModel(bag_of_words, normalize=True)

# train tf-idf model
corpus_tfidf = tfidf[bag_of_words]

# initialize an LSI transformation
lsi = models.LdaModel(corpus_tfidf, id2word=dictionary, num_topics=20)
corpus_lsi = lsi[corpus_tfidf]  # create a double wrapper over the original corpus: bow->tfidf->fold-in-lsi
print(lsi.print_topics(20))

print('Overall time: ', time() - start_t0)
