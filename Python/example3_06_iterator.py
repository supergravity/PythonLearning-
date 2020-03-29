# An example of an iterator

# Set up an iteratable object
fruits = ['apple','banana']

#Build a iterator
f = iter(fruits)

#Print out the elements in the object with Next()



for g in range(len(fruits)):
    print(next(f))
    print(type(g))
    print()


print()


for k in fruits:
    print(type(k))
    print(next(f))
    print()


