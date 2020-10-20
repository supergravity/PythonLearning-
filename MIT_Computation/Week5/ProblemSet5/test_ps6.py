import string

### DO NOT MODIFY THIS FUNCTION ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print('Loading word list from file...')
    # inFile: file
    in_file = open(file_name, 'r')
    # line: string
    line = in_file.readline()
    # word_list: list of strings
    word_list = line.split()
    print('  ', len(word_list), 'words loaded.')
    in_file.close()
    return word_list

### DO NOT MODIFY THIS FUNCTION ###
def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

### DO NOT MODIFY THIS FUNCTION ###
def get_story_string():
    """
    Returns: a joke in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

WORDLIST_FILENAME = 'words.txt'





class Message(object):
    ### DO NOT MODIFY THIS METHOD ###
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    ### DO NOT MODIFY THIS METHOD ###
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    ### DO NOT MODIFY THIS METHOD ###
    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]
        
    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        cipher_dict = {}
        alpha_string = string.ascii_lowercase + string.ascii_uppercase
        alpha_list = []
        shift_string_lowercase_list = []
        shift_string_uppercase_list = []
        #shift_string_lowercase = str()
        #shift_string_uppercase = str()
        for i in range(len(alpha_string)):
            alpha_list.append(alpha_string[i])


        for e in range(len(string.ascii_lowercase)):
            shift_string_lowercase_list.append(string.ascii_lowercase[(e+shift)%len(string.ascii_lowercase)])
            shift_string_uppercase_list.append(string.ascii_uppercase[(e+shift)%len(string.ascii_uppercase)])
        shift_string_list = shift_string_lowercase_list + shift_string_uppercase_list
        for i in range(len(alpha_string)):
            cipher_dict[alpha_list[i]] = shift_string_list[i]
       
        self.cipher_dict = cipher_dict
        #print(self.cipher_dict)
        return self.cipher_dict
        
    
    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        input_text_list = list(self.message_text)
        input_text_cp = input_text_list.copy()
        cipher_dict = self.build_shift_dict(shift)
        for i in range(len(input_text_list)):
            for k in cipher_dict.keys():
                if (input_text_list[i] == k):
                    input_text_cp[i] = cipher_dict[k]
                    #print(self.cipher_dict[k])
        self.shifted_text = ''.join(map(str, input_text_cp))

        return self.shifted_text

#Code = Message(text)
#Code.build_shift_dict(shift)
#secret = Code.apply_shift(shift)
#print(secret)

class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encrypting_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        Hint: consider using the parent class constructor so less 
        code is repeated
        '''
        Message.__init__(self,text)
        self.shift = shift
        #encrypting_dict = Message.build_shift_dict(self,shift)
        #self.encrypting_dict = encrypting_dict.copy()
        self.encrypting_dict = Message.build_shift_dict(self,shift).copy()
        self.message_text_encrypted = Message.apply_shift(self,shift)

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.shift

    def get_encrypting_dict(self):
        '''
        Used to safely access a copy self.encrypting_dict outside of the class
        
        Returns: a COPY of self.encrypting_dict
        '''
        return self.encrypting_dict

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        return self.message_text_encrypted

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift (ie. self.encrypting_dict and 
        message_text_encrypted).
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        self.shift = shift
        #encrypting_dict = Message.build_shift_dict(self,shift)
        #self.encrypting_dict = encrypting_dict.copy()
        self.encrypting_dict = Message.build_shift_dict(self,shift).copy()
        self.message_text_encrypted = Message.apply_shift(self,shift)


class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        Message.__init__(self,text)

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are  equally good such that they all create 
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        #self.message_text = text
        #word_list = load_words(WORDLIST_FILENAME)
        decrypt_pair = dict()
        decrypt_pair_2 = dict()
        for t in range(len(string.ascii_lowercase)):
            score = 0
            self.decrypted_dict = Message.build_shift_dict(self,t).copy()
            self.message_text_decrypted = Message.apply_shift(self,t)
            wordlist = self.message_text_decrypted.split(' ')
            #print(wordlist)
            for word in wordlist:
                if (is_word(self.valid_words, word)):
                    score = score + 1;
            decrypt_pair[t] = score
            decrypt_pair_2[t] = self.message_text_decrypted
        #print(decrypt_pair)
        #print(decrypt_pair_2)
        keypair = decrypt_pair.keys()
        keypair_2 = decrypt_pair.values()
        max_score = max(keypair_2)
        decrypt_pair_list = list()
        for i in keypair:
            if (decrypt_pair[i] == max_score):
                decrypt_pair_list.append(i)
                decrypt_pair_list.append(decrypt_pair_2[i])
        decrypt_pair_tuple = tuple(decrypt_pair_list)
        #print(decrypt_pair_tuple)
        self.pair_tuple = decrypt_pair_tuple
        return self.pair_tuple




#text = 'apple'
#shift = 3
#Code = PlaintextMessage(text,shift)
#
#text_out = Code.get_message_text()
#print(text_out)
#shift_obtained = Code.get_shift()
#print(shift_obtained)
#dict_code = Code.get_encrypting_dict()
#print(dict_code)
#encrypted = Code.get_message_text_encrypted()
#print(encrypted)
#
#print()
#shift = 10
#Code.change_shift(shift)
#text_out = Code.get_message_text()
##print(text_out)
#shift_obtained = Code.get_shift()
#print(shift_obtained)
#dict_code = Code.get_encrypting_dict()
#print(dict_code)
#encrypted = Code.get_message_text_encrypted()
#print(encrypted)
#Example test case (PlaintextMessage)
#plaintext = PlaintextMessage('hello world', 2)
#print('Expected Output: jgnnq')
#a = plaintext.get_message_text_encrypted()
#print('Actual Output:', plaintext.get_message_text_encrypted())
#ciphertext = CiphertextMessage(a)
#ciphertext.decrypt_message()
#print(cipertext)
#Example test case (CiphertextMessage)
#ciphertext = CiphertextMessage('jgnnq ')
#print('Expected Output:', (24, 'hello'))
#print('Actual Output:', ciphertext.decrypt_message())
### DO NOT MODIFY THIS FUNCTION ###

def decrypt_story():

    def get_story_string():
        """
        Returns: a joke in encrypted text.
        """
        f = open("story.txt", "r")
        story = str(f.read())
        f.close()
        
        return story
    
    story = get_story_string()

    Decrypt_story = CiphertextMessage(story)
    truth = Decrypt_story.decrypt_message()

    return truth 

print(decrypt_story())
