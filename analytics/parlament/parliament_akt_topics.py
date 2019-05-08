"""
This is a file for analysing topics from parliament based on law statements.
"""
from data import get_data, cache
from preprocess.preprocess_data import preprocess_pipeline
from gensim import models
from time import time
from pprint import pprint
import pyLDAvis.gensim

# TODO -> lsa, lsi, lda, hdp


# get data from api
start_t0 = time()
#data = get_data.akt_naslov_list()  # get adequate document list. data = get_data.akt_naslov_list()
data = cache.get_cached_akt()
print('get_data time: ', time() - start_t0)

# transform a list of documents to a bag of words model
start_t1 = time()
bag_of_words, dictionary = preprocess_pipeline(data, ngram=True, min_occur=5, max_occur=0.5)  # save_dict='fajl'
print('preprocessing time: ', time() - start_t1)


# create tf-idf model
tfidf = models.TfidfModel(bag_of_words, normalize=True)

# train tf-idf model
corpus_tfidf = tfidf[bag_of_words]


# Set training parameters.
num_topics = 20
chunksize = 2000
passes = 20
iterations = 400
eval_every = None  # Don't evaluate model perplexity, takes too much time.


model = models.LdaModel(corpus=bag_of_words, id2word=dictionary, chunksize=chunksize, alpha='auto', eta='auto',
                        iterations=iterations, num_topics=num_topics, passes=passes, eval_every=eval_every)
top_topics = model.top_topics(bag_of_words, num_words=20)
pprint(top_topics)
# print(model[doc_bow])
# pyLDAvis.gensim.prepare(model, corpus_tfidf, dictionary)




# initialize an LSI transformation
# lsi = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=20)
# corpus_lsi = lsi[corpus_tfidf]  # create a double wrapper over the original corpus: bow->tfidf->fold-in-lsi
# print(lsi.print_topics(20))

print('Overall time: ', time() - start_t0)
