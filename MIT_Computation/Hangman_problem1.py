def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    index = 0
    for word in range(len(secretWord)):
        for i in range(len(lettersGuessed)):
            if lettersGuessed[i] == secretWord[word]:
                index += 1
                break
    print(index)
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
    guessedList = list('_'*len(secretWord))
    #print(guessedList)
    for word in range(len(secretWord)):
        for i in range(len(lettersGuessed)):
            if (lettersGuessed[i] == secretWord[word]):
                #guessedList[word] = secretWord[word]
                guessedList.append()

    return ''.join(guessedList)





#for i in range(len(lettersGuessed)):
#        index = 0
#        for word in range(len(secretWord)):
#            print(lettersGuessed[i])
#            print(secretWord[word])
#            if lettersGuessed[i] != secretWord[word]:
#                index += 1
#        print(index)
#        if (index == len(secretWord)):
#            return False
#            break
#    return True


secretWord = 'apple'
#lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
lettersGuessed = ['e', 'a', 'k', 'p', 'l', 's']
print(isWordGuessed(secretWord, lettersGuessed))
print(getGuessedWord(secretWord, lettersGuessed))
