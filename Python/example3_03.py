# Another way of making request using while loop

print('Please insert a number:', end = ' ')
ans = input()

while not ans.isdigit():
    print('Please insert a number:', end = ' ')
    ans = input()

print(ans,'to go')
