# The usage of 'continue' and 'break' in  while/for loop

nums = [3, 14, 1, 5, 9, 2, 6, 5, 3, 5, 9]

print(nums)
print()

# The 'continue' usage
print('The "continue" usage')
print()
for n in nums:
    if n%2 != 0:
        continue
    print(n)

print('the loop ends')
print()

# The 'break' usage
print('The "break" usage')
print()
for n in nums:
    if n == 5:
        break 
    print(n)

print('the loop ends')
print()



