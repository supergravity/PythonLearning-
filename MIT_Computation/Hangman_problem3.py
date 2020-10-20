import string 
print(string.ascii_lowercase)

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''

    all_list = list(string.ascii_lowercase)

    remaining_list = list()

    for letter in range(len(all_list)):
        s = True
        for i in range(len(lettersGuessed)):
            if (lettersGuessed[i] == all_list[letter]):
                s = False         
        if(s == True):
            remaining_list.append(all_list[letter])

    print(remaining_list)
    return ''.join(remaining_list)


#lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
lettersGuessed = []
print(getAvailableLetters(lettersGuessed))


