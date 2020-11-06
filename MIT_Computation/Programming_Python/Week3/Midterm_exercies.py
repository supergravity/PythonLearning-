#def f(x):
#    while x> 3:
#        f(x+1)
#        print(f(x+1))
#
#
#f(2)


def g(x):
    a = []
    print(a)
    while x> 0:
        a.append(x)
        g(x-1)

#g(2)
#print(a)

#L = [1,2,3]
#d = {'a': 'b'}
#def f(x):
#    return 3
#
##print(L[3])
##print(d['b'])
#for i in range(1000001,-1,-2):
#    print(f)
#
#print(int('abc'))

stuff  = (["iBoy","iQ"],)
for thing in stuff:
    if thing == 'iQ':
        print("Found it")
        break

#print("Wrong!!!")



def Square(x):
    return SquareHelper(abs(x), abs(x))

def SquareHelper(n, x):
    if n == 0:
        return 0
    return SquareHelper(n-1, x) + x

print(Square(-1))
print(Square(-2))
print(Square(0))
print(Square(3.2))
