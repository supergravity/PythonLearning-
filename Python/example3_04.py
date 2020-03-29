
# Initialization

q_list = ['The Spanish of apple?', 'The number of a dozen?']
a_list = ['manzana','12']


# Argument

total = len(q_list)
score = 0

for q,a in zip(q_list,a_list):
    print (q, end = ' ')
    ans = input().lower().strip()

    if ans == a:
        print ('Good Job! ')
        score += 10
    else:
        print ('Try Again! ')
    print()

print('Total score: ',score)


