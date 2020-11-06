def general_poly (L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
    
    def Poly(x):
        poly_z = 0
#        if(len(L) == 0):
#            return 'None'
#        elif(x == 0):
#            return 0
#        else:
        for i in range(len(L)):
            poly_z = L[len(L)-i-1] * (x ** i) + poly_z       
        return poly_z

    return Poly

#print(general_poly([1, 2, 3, 4])(10))
#print(general_poly([])(3))
#print(general_poly([1,2,3,4])(0))



def general_poly (L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
    def Poly (x):
        n = 0
        for i in L:
            n = x*n + i
        return n
    return Poly
print(general_poly([1,2,3,4])(-1))
