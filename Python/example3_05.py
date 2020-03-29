# Another way of writing conditions 'if' with "in" and "not in"

print('What company did Elon Musk found?', end = ' ')
corrects = ['Tesla','SpaceX','Neurallink']
ans = input().strip()

if ans in corrects:
    print('Good Job! ')
else:
    print('Try Again! ')


