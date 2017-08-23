"""
The code below is used to measure how good a stemmer is working for Serbian language.

Main idea is to compute score for each stemmer by slicing stemmed words and comparing two lists.
"""
import re
import urllib.request as urllib
from collections import defaultdict
from time import time
from urllib.parse import urljoin

import bs4 as bs
import requests
from nltk.stem import SnowballStemmer, PorterStemmer, LancasterStemmer
from stemming import porter2

from preprocess.stemmers import Croatian_stemmer as CroStemmer
from preprocess.stemmers import Serbian_stemmer as SerbStemmer

stemmers = [
    PorterStemmer().stem,  # 0
    porter2.stem,  # 1
    SnowballStemmer('porter').stem,  # 2
    SnowballStemmer('russian').stem,  # 3
    SnowballStemmer('danish').stem,  # 4
    SnowballStemmer('dutch').stem,  # 5
    SnowballStemmer('english').stem,  # 6
    SnowballStemmer('finnish').stem,  # 7
    SnowballStemmer('hungarian').stem,  # 8
    SnowballStemmer('italian').stem,  # 9
    SnowballStemmer('norwegian').stem,  # 10
    SnowballStemmer('portuguese').stem,  # 11
    SnowballStemmer('romanian').stem,  # 12
    SnowballStemmer('spanish').stem,  # 13
    SnowballStemmer('swedish').stem,  # 14
    LancasterStemmer().stem,  # 15
    CroStemmer,  # 15
    SerbStemmer  # 16
]  # stemming algorithms

pages = [
    'http://www.kurir.rs/vesti',
    'http://www.kurir.rs/stars',
    'http://www.blic.rs/vesti',
    'http://informer.rs/vesti'
]  # web pages from scraping

reci = defaultdict(set)  # {stemmed_word: [list of original words]}
checklist = []  # list of sliced words


def chekword(word, n=5):
    """
    Slice first n characters of the given word
    :param word: word to be sliced
    :param n: number of chars to be sliced from the beginning
    :return: sliced word with length = n
    """
    return word[:n]


def compress_list(word_list):
    """
    Method for getting unique values in list
    :param word_list: list with possible duplicate values
    :return: list with unique values
    """
    return list(set(word_list))


def stemmer_score(lista_stem, lista_test):
    """
    Method for computing score for stemmers by comparing list of stemmed words with list of sliced words.
    
    :param lista_stem: list of stemmed words
    :param lista_test: list of sliced words
    :return: score for stemmer
    """
    return len(compress_list(lista_test)) / len(lista_stem)


def store_words(soup, stemmer=SerbStemmer, n=30):
    """
    Method for extracting words from scraped text and adding them to appropriate 
    list and dict.
    :param soup: BeautifulSoup object of scraped web page
    :param stemmer: stemming algorithm
    :param n: length for sliced words
    """
    # Get individual words
    text = get_text(soup)
    words = separate_words(text)

    for i in range(len(words)):
        word = words[i]
        checklist.append(chekword(word, n=n))
        try:
            stm_word = stemmer(word)
        except TypeError:
            print(word)
            continue

        reci[stm_word].add(word)


def get_text(soup):
    """
    Method for getting raw text from scraped webpage
    
    :param soup: BeautifulSoup object of scraped web page
    :return: raw text
    """
    text = soup.string
    if text is None:
        contents = soup.contents
        resulttext = ''
        for cont in contents:
            subtext = get_text(cont)
            resulttext += subtext + '\n'
        return resulttext
    else:
        return text.strip()


def separate_words(text):
    """
    Method for creating list of words from raw text.
    
    :param text: raw text
    :return: list of words
    """
    splitter = re.compile('\\W*')
    return [s.lower().rstrip().lstrip() for s in splitter.split(text) if s != '']


def crawl(pages, depth=2, time_crawl=50):
    """
    Crawling method.
    
    :param pages: list of pages to bre crawled
    :param depth: depth for crawling
    """
    start = time()
    for i in range(depth):
        new_pages = set()
        for page in pages:
            try:
                c = urllib.urlopen(page)
            except Exception:
                print("Can\'t open %s" % page)
                continue
            soup = bs.BeautifulSoup(c.read(), 'html.parser')
            store_words(soup)

            links = soup('a')
            for link in links:
                if 'href' in dict(link.attrs):
                    url = urljoin(page, link['href'])
                    if url.find("'") != -1:
                        # example: javascript:printOrder('http://www.serbianrailways.com/active/.../print.html')
                        continue
                    url = url.split('#')[0]  # remove location portion
                    if url[0:4] == 'http':
                        new_pages.add(url)
            if time() - start > time_crawl:
                return
        pages = new_pages


def crawl2(pages):
    """
    Method for crawling only the given pages.
    
    :param pages: list of pages to be crawled
    """
    for page in pages:
        try:
            c = urllib.urlopen(page)
        except Exception:
            print("Can\'t open %s" % page)
            continue
        soup = bs.BeautifulSoup(c.read(), 'html.parser')
        store_words(soup)


def test_with_fixed_n(n=5):
    for i, s in enumerate(stemmers):
        print(str(i), '. Stemmer:')
        for page in pages:
            try:
                c = urllib.urlopen(page)
            except Exception:
                print("Can\'t open %s" % page)
                continue
            soup = bs.BeautifulSoup(c.read(), 'html.parser')
            store_words(soup, stemmer=s, n=n)
        lista = list(reci.keys())
        print(stemmer_score(lista, checklist))
        print()
        checklist.clear()
        reci.clear()


def main_test(range_from=2, range_to=10):
    rng = range(range_from, range_to)
    for i, s in enumerate(stemmers):
        print(str(i), '. Stemmer:')
        score = 0
        for n in rng:
            for page in pages:
                try:
                    c = urllib.urlopen(page)
                except:
                    print("Can\'t open %s" % page)
                    continue
                soup = bs.BeautifulSoup(c.read(), 'html.parser')
                store_words(soup, stemmer=s, n=n)
            lista = list(reci.keys())
            score += stemmer_score(lista, checklist)
            checklist.clear()
            reci.clear()
        print(score)
        print()


if __name__ == '__main__':
    # crawl(pages, time_crawl=50)
    # crawl2(pages)
    # lista = list(reci.keys())
    # lista.sort()
    # print(lista)
    # print(reci)
    # print(stemmer_score(lista, checklist))
    # main_test(range_from=5, range_to=10)
    pass
    # print(s)
