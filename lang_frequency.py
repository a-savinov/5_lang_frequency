import collections
import sys


def load_data(filepath):
    with open(filepath, "r", encoding='utf-8') as input_file:
        raw_text = input_file.read()
    return raw_text


def get_words_as_list(raw_text):
    words_as_list = raw_text.strip().split()
    return words_as_list


def get_n_most_frequent_words(text_data, count):
    return collections.Counter(text_data).most_common(count)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        raw_data = load_data(filename)
        words_count = 10
        print(get_n_most_frequent_words(get_words_as_list(raw_data), words_count))
    else:
        print('No data for analyse')
