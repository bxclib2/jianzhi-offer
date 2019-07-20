def quickSort(l):
    if len(l)<=1:
        return l
    pivot = l[0]
    i = 0
    j = len(l) - 1
    flag = 1
    while i!=j:
        if flag == 1:
            if l[j]>=pivot:
                j = j - 1
            else:
                flag = 0
            continue
        if flag == 0:
            if l[i]<= pivot:
                i = i + 1
            else:
                l[i],l[j] = l[j],l[i]
                flag = 1
            continue
    l[0],l[i] = l[i],l[0]
    l = quickSort(l[0:i])+[l[i]]+quickSort(l[i+1:])
    return l

l = [1,3,4,8,51,4,7,29,2,3,7]
#l = [6,1,2,7,9,3,4,5,10,8]
print (quickSort(l))
