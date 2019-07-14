def bubbleSort(l):
    for i in range(len(l)):
        change = 0
        for j in range(1,len(l)-i):
            if l[j] ? l[j-1]:
                l[j],l[j-1] = l[j-1],l[j]
                change = 1
        if change == 0:
            return l
        print (l)
    return l

bubbleSort([3,6,4,2,11,10,5])
            
