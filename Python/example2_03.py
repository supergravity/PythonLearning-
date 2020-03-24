
print('The spanish of apple?')
ans = input().lower() # the function of an object

if ans == 'manzana':
    print('Good Job!')
else:
    print('Try Again ~')

# Another way of writing it

print('The spanish of apple?')
ans = input()

if ans.lower().strip() == 'manzana':
    print('Good Job!')
else:
    print('Try Again ~')


print('The spanish of apple?')
ans = input().lower().strip() # the function of an object

if ans == 'manzana':
    print('Good Job!')
else:
    print('Try Again ~')
