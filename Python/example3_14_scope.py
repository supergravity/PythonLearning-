# the scope of a variable

print('Exercise 1')
print()

def spec(status = True):
    tea = 'bubble milk tea'
    print(tea)

spec()

print()

#print(tea)
print('Exercise 2')
print()
'''
total = 10       # 'total' as a Global variable 
def count(tree = True):
    total += 1 
    print(total)

count()
'''
print('Exercise 3')
print()

sum = 10
#def plus(groot = True):
def plus():
    sum = 0      # 'sum' NOW as a Regional variable
    sum += 1
    print(sum)

plus()

print('Exercise 4')
print()
total = 10
def addition():
    global total # 'total' NOW as a Global variable 
    total += 1 
    print(total)

addition()


