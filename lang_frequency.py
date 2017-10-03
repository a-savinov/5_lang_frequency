import argparse
import collections


def load_data(filepath):
    with open(filepath, "r", encoding='utf-8') as input_file:
        raw_text = input_file.read()
    return raw_text


def get_words_as_list(raw_text):
    words_as_list = raw_text.lower().strip().split()
    return words_as_list


def get_n_most_frequent_words(text_data, count):
    return collections.Counter(text_data).most_common(count)


def input_argument_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', required=True,
                        help='File for analyse')
    return parser


if __name__ == '__main__':
    parser = input_argument_parser()
    namespace = parser.parse_args()
    filename = namespace.file
    raw_data = load_data(filename)
    words_count = 10
    words_list = get_n_most_frequent_words(get_words_as_list(raw_data),
                                           words_count)
    print('Most used words:')
    for word in words_list:
        print('Word: {:15}  Frequency: {}'.format(word[0], word[1]))
