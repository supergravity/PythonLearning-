# Illustration of the function 'All()' and 'Any()'
# All() and Any() both accept a iteratable object

# Set up an iteratable object
a = [8,'Hello', 3 > 2, True, -1]

b = ['',0.0,None,a]


# Exercise
print('IF all(a):')
if all(a):
    print('Cool!')
else:
    print('OHNO!')

print('IF all(b):')
if all(b):
    print('Cool!')
else:
    print('OHNO!')

print('IF any(b):')
if any(b):
    print('Cool!')
else:
    print('OHNO!')
    

