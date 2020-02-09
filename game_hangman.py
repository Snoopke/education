# Hangman game - classical game in words, where you should guess a word before you die
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(words):
    """
    Words (list): list of words (strings)
    Returns a word from wordlist at random
    """
    return random.choice(words)


words = load_words()


def is_word_guessed(secretWord, lettersGuessed):
    """
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    """
    # FILL IN YOUR CODE HERE...
    for letter in secretWord:
        if letter in lettersGuessed:
            continue
        else:
            return False
    return True


def get_guessed_word(secretWord, lettersGuessed):
    """
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    """
    current_res = ''
    for letter in secretWord:
        if letter in lettersGuessed:
            current_res += letter + ' '
        else:
            current_res += '_ '
    return current_res


def get_available_letters(lettersGuessed):
    """
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    """
    # FILL IN YOUR CODE HERE...
    alphabet = set(string.ascii_lowercase)
    lettersGuessed = set(lettersGuessed)
    ans = alphabet - lettersGuessed
    return ''.join(sorted(ans))
    

def hangman(secret_word):
    """
    secretWord: string, the secret word to guess.
    Starts up an interactive game of Hangman.
    """
    guesses_left = 8
    lettersGuessed = []
    print('Welcome to the game, Hangman!\n'
          'I am thinking of a word that is {} letters long'.format(len(secretWord)))
    while not is_word_guessed(secretWord, lettersGuessed):
        print('-------------')
        print('You have {} guesses left'.format(guesses_left))
        print('Available letters: ', get_available_letters(lettersGuessed))
        guess = input('Please guess a letter: ')
        if guess not in lettersGuessed:
            lettersGuessed.append(guess)
            if guess in secretWord:
                print('Good guess: ', get_guessed_word(secretWord, lettersGuessed))
                if is_word_guessed(secretWord, lettersGuessed):
                    print('-----------')
                    print('Congratulations, you won!')
                    break
            else:
                print('Oops! That letter is not in my word: ', get_guessed_word(secretWord, lettersGuessed))
                guesses_left -= 1
                if guesses_left == 0:
                    print('-----------')
                    print('Sorry, you ran out of guesses. The word was {}.'.format(secretWord))
                    print(' #########')
                    print('  |     ##')
                    print('  O     ##')
                    print(' /|\    ##')
                    print(' / \    ##')
                    print('________##')
                    break
                else:
                    continue
        else:
            print("Oops! You've already guessed that letter: ", get_guessed_word(secretWord, lettersGuessed))


secretWord = choose_word(words).lower()
hangman(secretWord)
