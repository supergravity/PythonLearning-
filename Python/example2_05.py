# exercise: format()

msg = '{0} is {1} years old'
msg = msg.format('John', 35)
print(msg)
print(type (msg))


# exercise: format()_2

msg = '{x} is {y} years old'
msg = msg.format(y = 10, x = 'John')
print(msg)
print(type (msg))

print('The volume has decreased {:.3f}%'.format(33.45678))

print('{:5},{:^8},{:5d}'.format(12, 34, 56))

print('{:=^40s}'.format('The legendary divider'))

