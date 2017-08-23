from data import get_data
from preprocess.preprocess_data import preprocess_pipeline
from gensim.summarization import summarize
from time import time


def summarize_poslanik_govor(poslanik_id):
    data = get_data.poslanik_govori(poslanik_id)
    s = ''
    for d in data[:5]:
        s += d
    return summarize(s, word_count=200)


if __name__ == '__main__':
    print(summarize_poslanik_govor(8647))  # Bosko Obradovic 8608
