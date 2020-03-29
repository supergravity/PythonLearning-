#The ways of importing functions

#import random
#from random import randint, randrange
import random as rnd

#Normally, in order to create 'real' randomness, the parameter will not be inserted
rnd.seed()

for i in range(4):
    print(rnd.randrange(2,10))
    print()




