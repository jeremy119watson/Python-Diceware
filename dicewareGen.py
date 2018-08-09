import sys
from random import randint
import argparse

wordList = {}

def begin():

    parser = argparse.ArgumentParser()
    parser.add_argument(    
        "-w",
        "--words", 
        type = int,
        help = """Specify the number of words in the password. 
                Must be in range of 0 to 100 inclusive, because
                ... well anything more than 10 words is ridiculous,
                but I absolutly draw the line at 100."""
    )
    parser.add_argument(
        "-v",
        "--verbose",
        help="output password with fancy presentation",
        action="store_true"
    )
    args = parser.parse_args()
    
    word_count = 6
    
    if args.words is not None:
        word_count = args.words
        
    if not 0 <= word_count <= 100:
        print("\nError: -w [Integer] must be in range of 0 to 100 inclusive\n")
        return
    
    password = gen_password(word_count)

    print("\n    PASSWORD\t: %s" % password)

    if args.verbose:
        print("    WORD COUNT\t: %d" % word_count)
        print("    CHAR COUNT\t: %d (including spaces)" % len(password))
    
    print("")
    

# ----------------------------------------

def gen_password(word_count):

    password = ""

    read_list()

    for _ in range(0,word_count):
        wordNumber = str(randint(1,6))
        wordNumber += str(randint(1,6))
        wordNumber += str(randint(1,6))
        wordNumber += str(randint(1,6))
        wordNumber += str(randint(1,6))
        password += wordList[wordNumber]
    return password.replace('\n',' ').strip(' ')

# ----------------------------------------

def read_list():

    try:
        f = open('dicewords.txt','r')
        for line in f:
            k,w = line.split('\t')
            wordList[k] = w
        f.close()
    except OSError:
        print("Error: dicewords.txt not found. Make sure it is in this directory.")

# ----------------------------------------

if __name__ == '__main__':
    begin()