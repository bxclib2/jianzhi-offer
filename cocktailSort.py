# cocktailSort.py
def cocktailSort(l):
    left = 0
    right = len(l)-1
    while left<right:
        for j in range(left,right):
            if l[j]>l[j+1]:
                l[j],l[j+1] = l[j+1],l[j]
        right = right - 1
        for s in range(right,left,-1):
            if l[s-1]>l[s]:
                l[s],l[s-1] = l[s-1],l[s]
        left = left + 1
        print (l)
    return l

cocktailSort([3,6,4,2,11,10,5])
