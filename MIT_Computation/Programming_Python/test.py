#def f(x, y):
#   '''
#   x: int or float.
#   y: int or float
#   '''
#   x + y - 2
#
#print(f(4,2))
#
#
#def c(x, y):
#   '''
#   x: int or float.
#   y: int or float.
#   '''
#   return x + y
#
#print(c(4,3))
#
#
#def a(x):
#   '''
#   x: int or float.
#   '''
#   return x + 1
#
#print(a(4.0))


#str1 = 'exterminate!'
#str2 = 'number one - the larch'
##print(str1.upper)
##print(str1.upper())
#str1.isupper()
#print(str1.isupper())
#print(str2.islower())
#
#str2 = str2.capitalize()
#print(str2)
#str2.swapcase()
#print(str2.swapcase())
#str1.index('e')
#print(str1.index('e'))
#str2.index('n')
#print(str2.index('n'))
#str2.find('n')
#print(str2.find('n'))
##str2.index('!')
##print(str2.index('!'))
#str2.find('!')
#print(str2.find('!'))
#str1.count('e')
#print(str1.count('e'))
#
#str1 = str1.replace('e', '*')
#print(str1)
#str2.replace('one', 'seven')
#print(str2.replace('one', 'seven'))



x = (1, 2, (3, 'John', 4), 'Hi')
#print(x[2][2])
#print(x[-1][-1])
##print(x[-1][2])
#print(x[0:1])
#print(x[0:-1])
#print(len(x))
#print(2 in x)
#print(3 in x)
#print(x[0] = 8)

#def oddTuples(aTup):
#    '''
#    aTup: a tuple
#
#    returns: tuple, every other element of aTup.
#    '''
#    alist = list(aTup)
#    #for t in alist:
#    blist = list()
#    blist.extend(alist[0:len(alist):2])
#        #t += 1
#    return tuple(blist)
#
#y = oddTuples(x)
#print(y)


#x = [1, 2, [3, 'John', 4], 'Hi']
#print(x[0:1])
#x[0] = 8
#print(x)
#listA = [1, 4, 3, 0]
#listB = ['x', 'z', 't', 'q']
#listA.sort
#print(listA.sort)
#listA.sort()
#print(listA)
#listA.insert(0, 100)
#print(listA.insert(0, 100))
#listA.remove(3)
#print(listA.remove(3))
#listA.append(7)
#print(listA.append(7))
#listA
#print(listA)
#listA + listB
#print(listA + listB)
#print(listB.sort())
#print(listB.pop())

#print(listB.count('a'))
#listB.remove('a')
#listA.extend([4, 1, 6, 3, 4])
#print(listA.count(4))
#listA.index(1)
#print(listA.index(1))
#listA.pop(4)
#print(listA.pop(4))
#listA.reverse()
#print(listA)

#aList = [0, 1, 2, 3, 4, 5]
#bList = aList
#aList[2] = 'hello'
#aList == bList
#
#print(aList == bList)
#aList is bList
#print(aList is bList)
#print(aList)
#print(bList)
#
#
#
#
#cList = [6, 5, 4, 3, 2]
#dList = []
#for num in cList:
#    dList.append(num)
#
#cList == dList
#print(cList == dList)
#print(cList is dList)
#cList[2] = 20
#print(cList)
#
#print(dList)

def applyEachTo(L, x):
    result = []
    for i in range(len(L)):
        result.append(L[i](x))
    return result

def square(a):
    return a*a

def halve(a):
    return a/2

def inc(a):
    return a+1

applyEachTo([inc, square, halve, abs], 3.0)

print(applyEachTo([inc, square, halve, abs], 3.0))
print(applyEachTo([inc, max, int], -3))

