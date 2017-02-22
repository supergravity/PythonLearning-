import sys

while True:
    print('Please insert the word "exit"')
    the_word = input()
    if the_word == 'exit':
        sys.exit()
    print('you typed: ' + the_word)
