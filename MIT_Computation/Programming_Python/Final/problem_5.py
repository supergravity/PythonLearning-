def f(a,b):
    return a + b




def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    d1_copy = d1.copy()
    d2_copy = d2.copy()
    print(d1_copy)
    print(d2_copy)
    
    dict_intersect = {}
    dict_diff = {}
    
    #append the calculation 
    for i in d1_copy.keys():
        for j in d2_copy.keys():
            if (i == j):
                dict_intersect[i] = f(d1_copy[i], d2_copy[j])

    d1_diff = [item for item in d1_copy.copy() if item not in dict_intersect.keys()]
    d2_diff = [item for item in d2_copy.copy() if item not in dict_intersect.keys()]
    
    for k in d1_diff:
        dict_diff[k] = d1_copy[k] 
    for l in d2_diff:
        dict_diff[l] = d2_copy[l] 

    #for k in d1_copy.keys():
    #    for l in dict_intersect.keys():
    #        if (k != l):
    #            dict_diff[k] = d1_copy[k]
    #for n in d2_copy.keys():
    #    for m in dict_intersect.keys():
    #        if (n != m):
    #            dict_diff[n] = d2_copy[m]
    
    #dict_diff.keys().sort()

    #print(dict_intersect)
    #print(d1_diff)
    #print(d2_diff)
    #print(dict_diff)

    tuple_result = dict_intersect,dict_diff
    return tuple_result

    print(tuple_result)


d1 = {1:30, 2:20, 3:30, 5:80}
d2 = {1:40, 2:50, 3:60, 4:70, 6:90}

dict_interdiff(d1, d2)


#print(dict_interdiff(d1,d2))

