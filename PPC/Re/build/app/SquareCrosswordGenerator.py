import random
from RegexSequenceDirector import *
import RegexGenerators

symbols = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

def random_word(len):
    """
    :param len: The length of the word
    :return: string: Random word, containing a set of the symbols's elements
    """
    return ''.join(random.sample(symbols, len))


def random_words_in_square(dimention):
    """
    :param dimention: the number of words to be generated (each of len dimention)
    :return: list of generated words
    """
    square_words = []
    for i in range(0, dimention):
        row = random_word(dimention)
        square_words.append(row)
    return square_words


def generate_noise_sample(word):
    """
    :param word: The word for which random noise will be generated
    :return: Dictionary that is required by the SequenceDirector
    """
    noise = {}
    for letter in word:
        letter_noise = {}
        letter_noise['positive'] = random.sample(symbols, len(word))
        letter_noise['negative'] = random.sample(set(symbols).difference(letter_noise['positive']), len(word))
        noise[letter] = letter_noise
    return noise


def random_square_crossword(dimention):
    """
    :param dimention: The dimention of the generated crossword (dimention x dimention)
    :return: Dictionary containing rows and cols, each containing the generated regexes
    """
    words = random_words_in_square(dimention)
    col_words = []
    for i in range(0, dimention):
        col_words.append(''.join(letter for word in words for letter in word[i]))

    rd = RegexSequenceDirector(dimention, symbols, RegexGenerators.RegexGeneratorsFactory())
    rows_regexes, col_regexes = [], []
    for row_word in words:
        sample_noise = generate_noise_sample(row_word)
        rows_regexes.append(rd.generate_regex(row_word, sample_noise))
    for col_word in col_words:
        sample_noise = generate_noise_sample(col_word)
        col_regexes.append(rd.generate_regex(col_word, sample_noise))

    return {'rows_regexes': rows_regexes, 'cols_regexes': col_regexes}


