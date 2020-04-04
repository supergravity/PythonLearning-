# The usage of List 

# Exercise 1
print('exercise 1: Counting Function')

nums = [3, 14, 1, 5, 9, 2, 6, 5, 3, 5, 9]
print(nums)
print('nums.count(5):' + str(nums.count(5)))

print()
# Exercise 2
print('exercise 2: Indices')

toys = ['Eevee','Charizard','Bulbasaur']
print(toys)
print(toys[-1])

#print(toys[30])

print()
print('exercise 3: Insertion')
#toys.append('Mew')
#print(toys[3] + '(append)')
toys.insert(3,'Mew')
print(toys[3] + '(insert)')
print(toys)


print()
print('exercise 4: Assignment')
toys[1] = 'Pikachu'
print('toys[1] : ' + toys[1])
print(toys)


print()
print('exercise 5: Pop removing the last element')
toys.pop()
print(toys)


print()
print('exercise 6: Insertion with Index')
toys.insert(0,'Primeape')
print(toys)


print()
print('exercise 7: Pop with Index')
toys.pop(0)
print(toys)

print()
print('exercise 8: extend with Extend or += ')
toys.extend(['Mewtwo','Dragonite'])
print(toys)
toys += ['Mew','Articuno']
print(toys)

print()
print('exercise 9: multiply the elements')
items = ['Lemon','Honey']
items *= 5
print(items)

print()
print('exercise 10: Removing or Deleting the elements')
toys.remove('Bulbasaur')
print(toys)
del toys[2]
print(toys)


