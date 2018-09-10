import sys
from random import randint
import argparse

wordList = {}
default_word_count = 6


def begin():

    args = parse_arguments()

    password = gen_password(args.word_count)

    print("\n    PASSWORD\t: %s" % password)

    if args.verbose:
        print("    WORD COUNT\t: %d" % args.word_count)
        print("    CHAR COUNT\t: %d (including spaces)" % len(password))

    print("")


def parse_arguments():

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-w",
        "--word-count",
        type=int,
        help="""Specify the number of words in the password
                in range of 1 to 100 inclusive."""
    )
    parser.add_argument(
        "-v",
        "--verbose",
        help="Output password with fancy presentation.",
        action="store_true"
    )
    args = parser.parse_args()

    if args.word_count is None:
        args.word_count = default_word_count
    elif not 0 < args.word_count <= 100:
        fatal_error(
            "-w|--word-count [Integer] must be in range of 1 to 100 inclusive")

    return args


def gen_password(word_count):

    password = ""

    read_list()

    for _ in range(0, word_count):
        wordNumber = str(randint(1, 6))
        wordNumber += str(randint(1, 6))
        wordNumber += str(randint(1, 6))
        wordNumber += str(randint(1, 6))
        wordNumber += str(randint(1, 6))
        password += wordList[wordNumber]
    return password.replace('\n', ' ').strip(' ')


def read_list():

    try:
        f = open('dicewords.txt', 'r')
        for line in f:
            k, w = line.split('\t')
            wordList[k] = w
        f.close()
    except OSError:
        fatal_error(
            "dicewords.txt not found. Make sure it is in this directory.")


def fatal_error(error_message):
    print("Error: %s" % error_message)
    quit()

if __name__ == '__main__':
    begin()
