#def laceStringsRecur(s1, s2):
#    """
#    s1 and s2 are strings.
#
#    Returns a new str with elements of s1 and s2 interlaced,
#    beginning with s1. If strings are not of same length, 
#    then the extra elements should appear at the end.
#    """
#    def helpLaceStrings(s1, s2, out):
#        #if s1 == '':
#            #s1 = helpLaceStrings(s1, s2, '')
#            #PLACE A LINE OF CODE HERE
#            
#        #if s2 == '':
#            #s2 = helpLaceStrings(s1, s2, '')
#            #PLACE A LINE OF CODE HERE
#        #else:
#            s1 + s2
#            #PLACE A LINE OF CODE HERE
#    return helpLaceStrings(s1, s2, '')
#


def laceStringsRecur(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length,
    then the extra elements should appear at the end.
    """
    def helpLaceStrings(s1, s2, out):
        if s1 == '':
            return out + s2
            #PLACE A LINE OF CODE HERE
        if s2 == '':
            return out + s1
            #PLACE A LINE OF CODE HERE
        else:
            return helpLaceStrings(s1[1:], s2[1:], out + s1[0] + s2[0])
            #PLACE A LINE OF CODE HERE
    return helpLaceStrings(s1, s2, '')

s1 = 'an apple'
s2 = 'boy'
print(laceStringsRecur(s1, s2))
