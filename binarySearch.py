def binarySearch(l,key):
    left = 0
    right = len(l) - 1 # 右边界是最大值，数组最后一个下标
    while left<=right: #这里一定是小于等于
        mid = (left+right)//2
        if l[mid] == key:
            return mid
        if l[mid] < key:
            left = mid+1
        if l[mid] > key:
            right = mid-1
    return -1
        
