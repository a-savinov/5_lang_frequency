import collections
import sys


def load_data(filepath):
    words_list = open(filepath, encoding='utf-8').read().strip().split()
    return words_list


def get_most_frequent_words(text_data):
    return collections.Counter(text_data).most_common(10)


if __name__ == '__main__':
    filename = sys.argv[1]
    print(get_most_frequent_words(load_data(filename)))
