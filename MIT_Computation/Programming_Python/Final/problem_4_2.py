#def getSublists(L, n):
#    return [L[i:i+n] for i in range(len(L)-n+1)]
#
#def longestRun(L):
#    master = []
#    longest = 0
#    for i in range(len(L)+1):
#        for k in getSublists(L, i):
#            print(k)
#            master.append(k)
#    #print(master)
#    for h in master:
#        if sorted(h) == h and len(h) >= longest:
#            longest = len(h)
#    return longest
#
#print(getSublists(L,4))


#1.Get the sublist of the list
#2.find the longeset sorted sublist


def GetSublist(L,m):
    temp_list = []
    for i in range(len(L)-m+1):
        temp_list.append(L[i:i+m])
    return temp_list

#print(GetSublist(L,4))

def longestRun(L):
    All_SubSet = []
    Max_length = 0
    for i in range(len(L)+1):
        for j in GetSublist(L,i):
            All_SubSet.append(j)
    #Find the longest sorted subset
    for l in All_SubSet:
        if ((sorted(l) == l) and (len(l) >= Max_length)): 
            Max_length = len(l)
    return Max_length

#L = [1, 2, 3, -1, -2, -3, -4, -5, -6]
L = [10, 4, 6, 8, 3, 4, 5, 7, 7, 2]
print(longestRun(L))

