def countingSort(l):
    minimal = min(l)
    maximal = max(l)
    for i in range(len(l)):
        l[i] = l[i] - minimal
    count = []
    for i in range(maximal-minimal+1):
        count.append(0)
    for i in l:
        count[i] = count[i] + 1
    res = []
    for i,c in enumerate(count):
        for j in range(c):
            res.append(i)
    for i in range(len(res)):
        res[i] = res[i] + minimal
    return res

l = [4,5,9,7,1,5,8,9,8,7,1,2,7,9,3]
print (countingSort(l))
