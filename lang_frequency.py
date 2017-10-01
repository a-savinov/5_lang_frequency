import collections
import sys


def load_data(filepath):
    with open(filepath, "r", encoding='utf-8') as input_file:
        raw_text = input_file.read()
    return raw_text


def get_words_as_list(raw_text):
    words_as_list = raw_text.lower().strip().split()
    return words_as_list


def get_n_most_frequent_words(text_data, count):
    return collections.Counter(text_data).most_common(count)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        raw_data = load_data(filename)
        words_count = 10
        words_list = get_n_most_frequent_words(get_words_as_list(raw_data), words_count)
        print('Most used words:')
        for word in words_list:
            print('Word: {:15}  Frequency: {}'.format(word[0], word[1]))
    else:
        print('No data for analyse')
