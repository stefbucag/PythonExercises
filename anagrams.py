"""EXERCISE #1.

Implement a function that uses the word list provided to return the anagrams
of a given word.
"""
import itertools
from argparse import ArgumentParser


class Anagrams(object):
    """Return anagrams of a word in the list provided."""

    def __init__(self):
        """Initialize."""
        self.input_file = open('WORD.LST')
        self.word_list = [word.rstrip() for word in self.input_file]

    def anagrams(self, word):
        """Return anagrams of the word.

        :param word: Word input.
        :param type: str
        :return anagrams: Angrams of the input word.
        :return type list
        """
        anagrams = [''.join(perm) for perm in itertools.permutations(word)]
        return anagrams

    def run(self, word):
        """Get anagrams of the word in the given list."""
        word_anagrams = self.anagrams(word)

        # Get the word anagrams in the input list
        listed_anagrams = list(set(self.word_list).intersection(word_anagrams))

        print '{word} - {anagrams}...'.format(anagrams=listed_anagrams,
                                              word=word.upper())


def __get_argparser():
    parser = ArgumentParser(description=__doc__)
    parser.add_argument('word', help='Word', type=str)

    return parser


if __name__ == '__main__':
    argparser = __get_argparser()
    args = argparser.parse_args()

    application = Anagrams()
    application.run(args.word)
