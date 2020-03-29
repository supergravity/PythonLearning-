# The example of importing library from others

import random 

right = ['Good Job','Excellent','Awesome','Bingo']

msg = random.choice(right)
print(msg)

print()

#other functions

print(random.randint(1,10))

print(random.randrange(7,10))

print()

eats = ['apple','chocolate','cake']
print(eats)
print()
random.shuffle(eats)
print(eats)

