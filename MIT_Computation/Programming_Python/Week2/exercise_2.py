def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if (a == 0):
        return b
    elif (b == 0):
        return a
    else:
        if(b >= a):
            return  gcdRecur(a,b%a)
        else:
            return gcdRecur(a%b,b)


print(gcdRecur(144,45))
