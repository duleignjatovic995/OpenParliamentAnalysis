"""
This file contains methods for preprocessing text.
The intendet pipeline would be:
    1. s = get_stemmed_list_of_documents(list_of_documents)  # parsing one document at a time
    2. d = create_dictionary(s)
    3. m = create_document_term_matrix(d, s)  # bag of words
"""

from preprocess.stemmers.Croatian_stemmer import stem_list as CroStemmer
from nltk.tokenize import word_tokenize
from preprocess.stop_words import stop_words, waste_words
from gensim import corpora, models
import os
import re


def get_stemmed_document_list(text):
    """
    Method for converting raw text to list of stemmed tokens.
    :param text: raw text
    :return: list of preprocessed tokens
    """
    # Remove punctuation
    string = re.sub('[\.,:;\(\)\'“`]', ' ', text)
    # Get list of tokens
    tokens = word_tokenize(string.lower())
    # Remove stop words
    stop_tokens = [token for token in tokens if not token in stop_words]
    # Stemming
    stemmed_tokens = CroStemmer(stop_tokens)
    # Filter useless words
    filtered_tokens = [token for token in stemmed_tokens if not token in waste_words]
    return filtered_tokens


def get_stemmed_list_of_documents(list_of_documents):
    """
    Method for converting list of documents 
    :param list_of_documents: e.g. ['tomato potato', 'salad soup meat', ...]
    :return: list of stemmed document lists e.g. [['tomat', 'potat'], ['salad', 'sou', 'mea'] ...]
    """
    dictionary = [get_stemmed_document_list(text) for text in list_of_documents]
    return dictionary


def get_ngrams(list_of_tokenized_documents, min_count=20):
    """
    Method for finding most occurring bigrams.
    :param list_of_tokenized_documents: 
    :param min_count: ignore all words and bigrams with total collected count lower than this.
    :return: documents with most common bi-grams
    """
    ngram = models.phrases.Phrases(list_of_tokenized_documents, min_count=min_count)
    for idx in range(len(list_of_tokenized_documents)):
        for token in ngram[list_of_tokenized_documents[idx]]:
            if '_' in token:
                # Token is a bigram - add to document (list of tokens)
                list_of_tokenized_documents[idx].append(token)
    return list_of_tokenized_documents


def create_dictionary(list_of_tokenized_documents, min_occur=1, max_occur=1, save='', print_dict=False):
    """
    Method for creating tokenized documents into a id <-> term dictionary
    :param list_of_tokenized_documents: list of stemmed document lists e.g. [['tomat', 'potat'], ['salad', 'sou', 'mea'] ...]
    :param min_occur: number of minimum word occurrences in documents
    :param max_occur: maximum percentage for word occurrence in documents
    :param save: if True, saves the document in temp folder
    :param print_dict: prints id <-> terms
    :return: id <-> term dictionary
    """
    dictionary = corpora.Dictionary(list_of_tokenized_documents)
    dictionary.filter_extremes(no_below=min_occur, no_above=max_occur)
    if save != '':
        pathname = '../temp/' + save
        try:
            with open(os.path.join(os.path.dirname(__file__), pathname), 'wb') as f:
                dictionary.save(f)
        except IOError:
            print("Couldn't save dictionary to temp folder :(")

    if print_dict is True:
        print(dictionary.token2id)

    return dictionary


def create_document_term_matrix(dictionary, list_of_tokenized_documents):
    """
    Method for creating bag of words model.
    
    :param dictionary: id <-> term dictionary
    :param list_of_tokenized_documents: 
    :return: list of stemmed document lists e.g. [['tomat', 'potat'], ['salad', 'sou', 'mea'] ...]
    """
    dt_matrix = [dictionary.doc2bow(text) for text in list_of_tokenized_documents]
    return dt_matrix


def preprocess_pipeline(list_of_documents, ngram=True, min_occur=1, max_occur=1, save_dict=''):
    # process list of documents -> doc = list of stemmed words
    tokenized_doc_list = get_stemmed_list_of_documents(list_of_documents)
    if ngram is True:
        tokenized_doc_list = get_ngrams(tokenized_doc_list)
    dictionary = create_dictionary(tokenized_doc_list, min_occur=min_occur, max_occur=max_occur, save=save_dict)
    bow = create_document_term_matrix(dictionary, tokenized_doc_list)
    return bow, dictionary
