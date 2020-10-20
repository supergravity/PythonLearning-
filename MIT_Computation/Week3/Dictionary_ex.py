def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    num_entity = 0
    aDictKey_list = list(aDict.keys())
    print(aDictKey_list)
    for i in range(len(aDict.keys())):

        entity = len(aDict[aDictKey_list[i]])
        print(entity)
        num_entity = num_entity + entity
    
    return num_entity


animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

print(animals)
print(how_many(animals))
