# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string 

WORDLIST_FILENAME = "words.txt"

def loadWords():
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

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    index = 0
    for word in range(len(secretWord)):
        for i in range(len(lettersGuessed)):
            if lettersGuessed[i] == secretWord[word]:
                index += 1
                break
    #print(index)
    if index == len(secretWord):
        return True
    else:
        return False



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    #print(guessedList)
    guessedList = list('_'*len(secretWord))
    for word in range(len(secretWord)):
        for i in range(len(lettersGuessed)):
            if (lettersGuessed[i] == secretWord[word]):
                guessedList[word] = secretWord[word]
                #guessedList.append(secretWord[word])

    return ''.join(guessedList)



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    all_list = list(string.ascii_lowercase)

    remaining_list = list()

    for letter in range(len(all_list)):
        s = True
        for i in range(len(lettersGuessed)):
            if (lettersGuessed[i] == all_list[letter]):
                s = False         
        if(s == True):
            remaining_list.append(all_list[letter])

    #print(remaining_list)
    return ''.join(remaining_list)
   
def goodGuess(secretWord, keyletter):
    s = False
    for letter in range(len(secretWord)):
        if(keyletter == secretWord[letter]):
            s = True
            return s
            break
    return s 
        




def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    #Let the user know how many letters the secretWord contains.
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is ' +str(len(secretWord)) +  ' letters long.')
    print('-----------')
    num_Guess = 8
    lettersGuessed = list()
    lettersGuessed_str = str()
    lettersGuessed_default = str()
    lettersGuessed_default = ('_'*len(secretWord))  
    while (num_Guess > 0):
        print('You have ' + str(num_Guess) + ' guesses left.')
        print('Available letters: ' + getAvailableLetters(lettersGuessed))
        guess = input('Please guess a letter: ')
        keyword = guess.lower()
        lettersGuessed.append(keyword)
        #lettersGuessed.append(input('Please guess a letter: '))
        #print(lettersGuessed)
        #print(lettersGuessed_default)
        lettersGuessed_str = getGuessedWord(secretWord, lettersGuessed)
        #print(lettersGuessed_str)
        if(isWordGuessed(secretWord, lettersGuessed)):
            print('Good guess: ' + lettersGuessed_str)
            print('-----------')
            print('Congratulations, you won!') 
            break

        if(lettersGuessed_str != lettersGuessed_default):
            print('Good guess: ' + lettersGuessed_str)
            lettersGuessed_default = lettersGuessed_str
        elif(lettersGuessed_str == lettersGuessed_default):
            if(goodGuess(secretWord,keyword)):
                #print(goodGuess(secretWord,keyword))
                print("Oops! You've already guessed that letter: " + lettersGuessed_str)
            else:
                print('Oops! That letter is not in my word: ' + lettersGuessed_str)
                num_Guess -= 1
        print('-----------')
    if(num_Guess == 0):
        print('Sorry, you ran out of guesses. The word was else.')


secretWord = 'y'
hangman(secretWord)




# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

#secretWord = chooseWord(wordlist).lower()
#hangman(secretWord)

#import string
#
#def goodGuess(secretWord, keyletter):
#    s = False
#    for letter in range(len(secretWord)):
#        if (keyletter == secretWord[letter]):
#            s = True
#            return s
#            break
#    return s
#
#
#def hangman(secretWord):
#    '''
#    secretWord: string, the secret word to guess.
#
#    Starts up an interactive game of Hangman.
#
#    * At the start of the game, let the user know how many
#      letters the secretWord contains.
#
#    * Ask the user to supply one guess (i.e. letter) per round.
#
#    * The user should receive feedback immediately after each guess
#      about whether their guess appears in the computers word.
#
#    * After each round, you should also display to the user the
#      partially guessed word so far, as well as letters that the
#      user has not yet guessed.
#
#    Follows the other limitations detailed in the problem write-up.
#    '''
#    print('Welcome to the game, Hangman!')
#    print('I am thinking of a word that is ' + str(len(secretWord)) + ' letters long.')
#    print('-----------')
#    num_Guess = 8
#    lettersGuessed = list()
#    lettersGuessed_str = str()
#    lettersGuessed_default = str()
#    lettersGuessed_default = ('_' * len(secretWord))
#    while (num_Guess > 0):
#        print('You have ' + str(num_Guess) + ' guesses left.')
#        print('Available letters: ' + getAvailableLetters(lettersGuessed))
#        guess = input('Please guess a letter: ')
#        keyword = guess.lower()
#        lettersGuessed.append(keyword)
#        lettersGuessed_str = getGuessedWord(secretWord, lettersGuessed)
#        if (isWordGuessed(secretWord, lettersGuessed)):
#            print('Good guess: ' + lettersGuessed_str)
#            print('Congratulations, you won!')
#            break
#
#        if (lettersGuessed_str != lettersGuessed_default):
#            print('Good guess: ' + lettersGuessed_str)
#            lettersGuessed_default = lettersGuessed_str
#        elif (lettersGuessed_str == lettersGuessed_default):
#            if (goodGuess(secretWord, keyword)):
#                print("Oops! You've already guessed that letter: " + lettersGuessed_str)
#            else:
#                print('Oops! That letter is not in my word: ' + lettersGuessed_str)
#                num_Guess -= 1
#        print('-----------')
#    if (num_Guess == 0):
#        print('Sorry, you ran out of guesses. The word was else.')
import string


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''

    # FILL IN YOUR CODE HERE...
    # Let the user know how many letters the secretWord contains.
    def isWordGuessed(secretWord, lettersGuessed):
        index = 0
        for word in range(len(secretWord)):
            for i in range(len(lettersGuessed)):
                if lettersGuessed[i] == secretWord[word]:
                    index += 1
                    break
        # print(index)
        if index == len(secretWord):
            return True
        else:
            return False

    def getGuessedWord(secretWord, lettersGuessed):
        guessedList = list('_' * len(secretWord))
        for word in range(len(secretWord)):
            for i in range(len(lettersGuessed)):
                if (lettersGuessed[i] == secretWord[word]):
                    guessedList[word] = secretWord[word]
                # guessedList.append(secretWord[word])

        return ''.join(guessedList)

    def getAvailableLetters(lettersGuessed):
        all_list = list(string.ascii_lowercase)

        remaining_list = list()

        for letter in range(len(all_list)):
            s = True
            for i in range(len(lettersGuessed)):
                if (lettersGuessed[i] == all_list[letter]):
                    s = False
            if (s == True):
                remaining_list.append(all_list[letter])

        # print(remaining_list)
        return ''.join(remaining_list)

    def goodGuess(secretWord, keyletter):
        s = False
        for letter in range(len(secretWord)):
            if (keyletter == secretWord[letter]):
                s = True
                return s
                break
        return s

    def alreadyGuess(lettersGuessed, keyletter):
        s = False
        for letter in range(len(lettersGuessed)):
            if (keyletter == lettersGuessed[letter]):
                s = True
                return s
                break
        return s

    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is ' + str(len(secretWord)) + ' letters long.')
    print('-----------')
    num_Guess = 8
    lettersGuessed = list()
    lettersGuessed_str = str()
    lettersGuessed_default = str()
    lettersGuessed_default = ('_' * len(secretWord))
    while (num_Guess > 0):
        print('You have ' + str(num_Guess) + ' guesses left.')
        print('Available letters: ' + getAvailableLetters(lettersGuessed))
        guess = input('Please guess a letter: ')
        keyword = guess.lower()
        lettersGuessed.append(keyword)
        # lettersGuessed.append(input('Please guess a letter: '))
        # print(lettersGuessed)
        # print(lettersGuessed_default)
        lettersGuessed_str = getGuessedWord(secretWord, lettersGuessed)
        # print(lettersGuessed_str)
        if (isWordGuessed(secretWord, lettersGuessed)):
            print('Good guess: ' + lettersGuessed_str)
            print('-----------')
            print('Congratulations, you won!')
            break

        if (lettersGuessed_str != lettersGuessed_default):
            print('Good guess: ' + lettersGuessed_str)
            lettersGuessed_default = lettersGuessed_str
        elif (lettersGuessed_str == lettersGuessed_default):
            if (goodGuess(secretWord, keyword) & & (alreadyGuess(lettersGuessed_str, keyword):
            # print(goodGuess(secretWord,keyword))
            print("Oops! You've already guessed that letter: " + lettersGuessed_str)
                    else:
                    print('Oops! That letter is not in my word: ' + lettersGuessed_str)
            num_Guess -= 1
            print('-----------')
            if (num_Guess == 0):
                print('Sorry, you ran out of guesses. The word was else.')