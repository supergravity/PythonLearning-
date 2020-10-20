def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    num_entity = 0
    aDictKey_list = list(aDict.keys())
    print(aDictKey_list)
    entityList = list()
    for i in range(len(aDict.keys())):

        entity = len(aDict[aDictKey_list[i]])
        print(entity)
        entityList.append(entity)
        num_entity = num_entity + entity
    if (num_entity == 0):
        return 'None'
    Maximum = max(entityList)
    print(Maximum)
    char = list()
    for k in range(len(aDict.keys())):

        entity = len(aDict[aDictKey_list[k]])
        if entity == Maximum:
            char.append(aDictKey_list[k])
    print(char)
    return char[0]



animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

#halo = dict()

print(biggest(animals))
#print(biggest(halo))
