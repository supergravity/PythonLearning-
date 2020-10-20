def keysWithValue(aDict, target):
    '''
    aDict: a dictionary
    target: an integer
    '''
    targetList = list()
    keyList = list(aDict.keys())
    print(keyList)
    for i in range(len(keyList)):
        if(aDict[keyList[i]] == target):
            targetList.append(keyList[i])

    targetList.sort()

    return targetList



numDict = {2:3,1:2,3:4,4:5,11:5,5:6,6:7,10:5,7:4,8:3,9:6}
target = 5

print(keysWithValue(numDict,target))
