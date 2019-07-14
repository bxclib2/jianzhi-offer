def shellSort(l):
    d = len(l)
    while True:
        d = d//2
        for k in range(d):
            for i in range(k+d,len(l)):
                # l[i] 是无序部分的第一个数
                # 向前依次比较，把其放在应该放的位置
                # 插入的方式是交换，依次向前交换直到不用交换了，就放到正确位置了
                for j in range(i,0,-d):
                    if l[j-d] > l[j]:
                        l[j-d],l[j] = l[j],l[j-d]
            if d==1:
                return l
