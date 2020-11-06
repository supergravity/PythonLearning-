import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'


SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10}



#words = 'quail'
#words = 'zzz'
#words = 'ql'
#words = 'mail'

#Hand = {'a': 1, 'q': 1, 'l': 2, 'm': 1, 'u': 1, 'i': 1}
#Hand = {'n':1, 'e':1, 't':1, 'a':1, 'r':1, 'i':2}
#Hand = {'w':1, 's':1, 't':2, 'a':1, 'o':1, 'f':1}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

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
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print("  ", len(wordList), "words loaded.")
    return wordList


def getWordScore(word, n):

    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    score = 0
    letter_list = list(SCRABBLE_LETTER_VALUES.keys())
    #print(letter_list)
    for char in word:
        for i in letter_list:
            if char == i:
                score = score + SCRABBLE_LETTER_VALUES[i]
    if(len(word) == n):
        score = (score * len(word)) + 50
    else:
        score = score * len(word)
    return score


def dealHand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    numVowels = n // 3
    
    for i in range(numVowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(numVowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand

def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it.

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)
    returns: dictionary (string -> int)
    """
    #hand_list = list(hand.keys())
    #input_string = word
    #print(hand)
    #print(hand_list)
    #for i in hand_list:
    hand_cp = hand.copy()
    for i in list(hand_cp.keys()):
        #for char in input_string:
        for char in word:
            if (char == i):
                hand_cp[i] = hand_cp[i] - 1 
    #print('hand: ' + str(hand))
    #print('hand_cp: ' + str(hand_cp))
    return hand_cp 


#input_string = 'apple'
#input_string = 'great'
##print(getWordScore(input_string,7))
#
#hand_ = updateHand(Hand,words)
#hand_remaining = hand_.keys()
#    
#print(hand_)

def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    hand_check = False
    wordList_check = False
    hand_cp = hand.copy()
    wordList_cp = wordList.copy()
    counter = 0
    for i in list(hand_cp.keys()):
        for char in word:
            if (char == i) and (hand_cp[i] >= 1):
                counter = counter + 1
                hand_cp[i] = hand_cp[i] - 1 
    if counter == len(word):
        hand_check = True
    #End of the hand_check
    for v in wordList_cp:
        if(word == v):
            wordList_check = True 
            break
    
    if (hand_check) and (wordList_check):
        return True 
    else:
        return False

#result = isValidWord(words, Hand, wordList)
#print(result)
#print(wordList)
def calculateHandlen(hand):
    """
    Returns the length (number of letters) in the current hand.

    hand: dictionary (string int)
    returns: integer
    """
    length = 0
    #length_ = 0
    for letter in hand.keys():
        length = length + hand[letter]
    
    #for value in hand.values():
    #    length_ = length_ + value

    #print(length)
    #print(length_)

    return length
        
#length_hand = calculateHandlen(Hand)
#print(length_hand)

def displayHand(hand):
    """
    Displays the letters currently in the hand.

    For example:
    >>> displayHand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter,end=" ")       # print all on the same line
    print()                             # print an empty line

def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".")
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)

    """
    #Initialization
    # Keep track of the total score
    score = 0
    total_score = 0
    hand_cp = hand.copy()
    # As long as there are still letters left in the hand:
    while(calculateHandlen(hand_cp) != 0):
        # Display the hand
        print()
        print('Current Hand: ',end = " ")
        displayHand(hand_cp)
        # Ask user for input
        word = input('Enter word, or a "." to indicate that you are finished:')
        # If the input is a single period:
        if (word == "."):
            # End the game (break out of the loop)
            break
            
        # Otherwise (the input is not a single period):
        else:
            # If the word is not valid:
            if(not isValidWord(word, hand_cp, wordList)):
                # Reject invalid word (print a message followed by a blank line)
                print('Invalid word, please try again.')
            # Otherwise (the word is valid):
            else:
                # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
                score = getWordScore(word, n)
                total_score = total_score + score
                print(word + ' earned ' + str(score) + ' points. Total: ' + str(total_score) + ' points')
                #print()
                # Update the hand 
                hand_cp = updateHand(hand_cp,word)
    print()
    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    if(word == '.'): 
        print('Goodbye! Total score: ' + str(total_score) + ' points')
    else:
        print('Run out of letters. Total score: ' + str(total_score) + ' points')

def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
 
    2) When done playing the hand, repeat from step 1
    """
    HAND_SIZE = 7
    n = HAND_SIZE
    Hand = {}
    char_input = 'i'
    #1) Asks the user to input 'n' or 'r' or 'e'.
    #char_input = input('Enter n to deal a new hand, r to replay the last hand, or e to end game:')
    first_play = True
    while(char_input != 'e'):
        # If the user inputs 'n', let the user play a new (random) hand.
        char_input = input('Enter n to deal a new hand, r to replay the last hand, or e to end game:')
        if (char_input == 'n'):
            Hand = dealHand(n)
            playHand(Hand,wordList,n)
            first_play = False
        # If the user inputs 'r', let the user play the last hand again.
        elif(char_input == 'r') :
            if(first_play == True):
                print('You have not played a hand yet. Please play a new hand first!')
                #first_play = False
            else:
                playHand(Hand,wordList,n)
        # If the user inputs 'e', exit the game.
        elif(char_input == 'e'):
            break
        # If the user inputs anything else, tell them their input was invalid.
        else:
            print('Invalid command.')

wordList = loadWords()
playGame(wordList)
