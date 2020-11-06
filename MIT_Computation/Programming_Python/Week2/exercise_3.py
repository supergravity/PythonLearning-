def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    #print(aStr)
    #print('ho')
    if (len(aStr) == 0):
        return False

    elif (len(aStr) == 1):
        if(char == aStr):
            return True
        elif(char != aStr):
            return False
    else:   
        #print(len(aStr)//2)
        if(len(aStr)%2 == 0):
            mid = aStr[len(aStr)//2 -1]
        else:
            mid = aStr[len(aStr)//2]

        #print(mid)
        #print(aStr)
        #print()
        #print('hi')
        if(char == mid):
            return True

        elif(char < mid):
            if(len(aStr)%2 == 0):
                aStr = aStr[0:len(aStr)//2 -1]
            else:
                aStr = aStr[0:len(aStr)//2]
            #print(aStr)
            #print('yo')
            return isIn(char,aStr)

        elif(char > mid):
            if(len(aStr)%2 ==0):
                aStr = aStr[len(aStr)//2 -1 :len(aStr)]
            else:
                aStr = aStr[len(aStr)//2 :len(aStr)]
            #print(aStr)
            #print('jo')
            return isIn(char,aStr)

#print(isIn('t', 'cdfilquw'))
#print(isIn('t', ''))
#print(isIn('t', 'q'))
isIn('l', 'abbeffffgkkkmnoqwy')
def isIn(char, aStr):
    if len(aStr) == 0:
        return False  
    middleIndex = len(aStr) // 2
    middleChar = aStr[middleIndex]
    if char == middleChar:
        return True
    else:
        if char > middleChar:
            return isIn(char, aStr[middleIndex+1:])
        else:
            return isIn(char, aStr[:middleIndex])
