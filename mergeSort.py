def mergeSort(l):
    if len(l) <= 1:
         return l
    mid = len(l)//2
    a = mergeSort(l[:mid])
    b = mergeSort(l[mid:])
    merged = []
    while len(a) * len(b) != 0:
        if a[0] <= b[0]:
            merged.append(a.pop(0))
        else:
            merged.append(b.pop(0))
    merged = merged + a + b
    return merged
        
l = [4,5,9,7,1,5,8,9,8,7,1,2,7,9,3]
print (mergeSort(l))
