#Another function example:
from random import choice

def words (status=True):
    right = ['Nice~','Great','Awesome','Bingo']
    wrong = ['Try Again','Dont Give Up','Oops']

    if status:
        msg = choice(right)
    else:
        msg = choice(wrong)

    return msg

a_list = ['SpaceX','Tesla','Neurallink']


print('What company did Elon Musk found?')

ans = input().strip()

if ans in a_list:
    print(words(True))
else:
    print (words(False))




