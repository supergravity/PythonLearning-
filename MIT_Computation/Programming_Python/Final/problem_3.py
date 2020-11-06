def McNuggets(n):
    """
    n is an int

    Returns True if some integer combination of 6, 9 and 20 equals n
    Otherwise returns False.
    """
#    a = 0
#    b = 0
#    c = 0 
#
#    m = 20
#    o = 9
#    p = 6
#
#    while(n >= m):
#        n = n - m
#        c += 1
#
#    print(c)
#    print(n)

#    if(n < 0):
#        return False
#    
#    elif(n == 0):
#        return True
#
#    else:
#        k = n % 20
#        k = k % 9
#        k = k % 6
#        if(k == 0):
#            return True
#        else:
#            return False 
#(NOT working WHY?????)


    a = 20
    b = 9
    c = 6

    for i in range n:
        for j in range n:
            for k in range n:
                if ((c*i + b*j + a*k) == n):
                    return True
    return False




print(McNuggets(101))
