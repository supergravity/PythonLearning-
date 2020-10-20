def lessThan4(aList):
    '''
    aList: a list of strings
    '''
    subaList = list()
    for i in range(len(aList)):
        if (len(aList[i]) < 4):
            subaList.append(aList[i])

    return subaList


aList = ["apple", "cat", "dog", "banana"]

print(lessThan4(aList))
