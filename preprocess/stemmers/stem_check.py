from preprocess.stemmers import Croatian_stemmer as CroStemmer
import re
from collections import defaultdict
from data import get_data


def separate_words(text):
    """
    Method for creating list of words from raw text.

    :param text: raw text
    :return: list of words
    """
    splitter = re.compile('\\W*')
    return [s.lower().rstrip().lstrip() for s in splitter.split(text) if s != '']


def store_words(text, stem_dict):
    # Get individual words
    words = separate_words(text)

    for i in range(len(words)):
        word = words[i]
        try:
            stm_word = CroStemmer.stem_str(word)
        except TypeError:
            print(word)
            continue

        stem_dict[stm_word].add(word)


def get_stem_dictionary(data):
    """
    Method for returning dictionary {stemmed_word: {set of original words}}
    :param data: list of documents
    :return: stem dictionary
    """
    w_dict = defaultdict(set)  #
    for d in data:
        store_words(d, w_dict)
    return w_dict


if __name__ == '__main__':
    print(get_stem_dictionary(get_data.akt_naslov_list()))