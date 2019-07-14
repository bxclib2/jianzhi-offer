def selectSort(l):
    for i in range(len(l)-1):
        m = i
        # Find the min
        for j in range(i+1,len(l)):
            if l[j] < l[m]:
                m = j
        l[i],l[m] = l[m],l[i]
    return l

l = [4,5,9,7,1,5,8,9,8,7,1,2,7,9,3]

print (selectSort(l))

