def radixSort(l):
    # 注意非比较排序的几种算法，大部分都要查找数的最大最小值，
    # 对于空列表都要单独处理，否则会报错
    if l == []:
        return l
    radix_stack = []
    for i in range(10):
        radix_stack.append([])
    maximal = max(l)
    if maximal <= 9:
        i = 1
    else:
        i = 0
        while maximal >= 1:
            maximal = maximal /10
            i = i + 1
    for t in range(i):
        for n in l:
            p = n
            for _ in range(t):
                p = p // 10
            radix_stack[p].append(n)
        l = []
        for k in range(10):
            while radix_stack[k]!=[]:
                l.append(radix_stack[k].pop())
    return l
            
l = [4,5,9,7,1,5,8,9,8,7,1,2,7,9,3]
print (radixSort(l))
