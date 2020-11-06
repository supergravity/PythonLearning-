def rem(x, a):
    """
    x: a non-negative integer argument
    a: a positive integer argument

    returns: integer, the remainder when x is divided by a.
    """
    #i = 0 
    if x == a:
        return 0
    elif x < a:
        return x
    else:
        return rem(x-a, a)
        #print(rem(x-a,a))
        #i += 1 
    #print(i)

#print(rem(5,5))
#print(rem(2,5))
#print(rem(7,5))
print(rem(14,5))
