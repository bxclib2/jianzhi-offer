def adjustHeap(l,head):
    left_index = 2*head + 1
    right_index = 2*head + 2
    if left_index > len(l) - 1:
        return l
    if left_index == len(l) - 1:
        if l[head] <= l[left_index]:
            return l
        else:
            l[head],l[left_index] = l[left_index],l[head]
            return adjustHeap(l,left_index)
    if left_index < len(l) - 1:
        if l[head] <= l[left_index] and l[head] <= l[right_index]:
            return l
        if  l[head] > l[left_index] and l[left_index] <= l[right_index]:
            l[head],l[left_index] = l[left_index],l[head]            
            return adjustHeap(l,left_index)
        if  l[head] > l[right_index] and l[left_index] >= l[right_index]:
            l[head],l[right_index] = l[right_index],l[head]            
            return adjustHeap(l,right_index)
def buildHeap(l):
    if len(l)<2:
        return l
    head = (len(l) - 2)//2
    for i in range(head,-1,-1):
        adjustHeap(l,i)
    return l
def popHeap(l):
    if len(l) == 1:
        return [],l.pop()
    r = l[0]
    l[0] = l.pop()
    if l!=[]:
        l = adjustHeap(l,0)
    return l,r
def heapSort(l):
    l = buildHeap(l)
    res = []
    while l!=[]:
        l,r = popHeap(l)
        res.append(r)
    return res


print (heapSort([7,8,2,4,6,9,3,4,81,0.3]))
