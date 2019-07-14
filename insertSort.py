def insertSort(l):
    for i in range(1,len(l)):
        # l[i] 是无序部分的第一个数
        # 向前依次比较，把其放在应该放的位置
        # 插入的方式是交换，依次向前交换直到不用交换了，就放到正确位置了
        for j in range(i,0,-1):
            if l[j-1] > l[j]:
                l[j-1],l[j] = l[j],l[j-1]
    return l

l = [4,5,9,7,1,5,8,9,8,7,1,2,7,9,3]
print (insertSort(l))
