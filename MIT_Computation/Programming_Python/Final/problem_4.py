def longestRun(L):
    
    def GetLongRun(G):

        longRun = list()
        for i in range(len(G[:-1])):
            if(G[i] <= G[i+1]):
                longRun.append(G[i])
            elif((i != 0) and (G[i-1] <= G[i]) and (G[i] >= G[i+1])):
                longRun.append(G[i])
        
        return longRun
    
    def isSort(L):
        for i in range(len(L[:-1])):
            if(L[i] > L[i+1]):
                return False
        return True


    is_Sort = isSort(L)
    list_ = GetLongRun(L)
    print(list_)
    while (not is_Sort):
        
        list_ = GetLongRun(list_)
        print(list_)
        is_Sort = isSort(list_)



    


L = [10, 4, 6, 8, 3, 4, 5, 7, 7, 2]

longestRun(L)

