def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    min_val = min(a,b)
    print(min_val)
    while(min_val > 1):
        if ((a % min_val == 0) and (b % min_val == 0)):
            return min_val
        min_val = min_val - 1 
        print(min_val)
    return min_val

print(gcdIter(144,45))
