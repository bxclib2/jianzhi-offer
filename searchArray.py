#array = [[1,2,3,4],[2,3,4,5],[3,4,5,6],[4,5,6,7]]

def searchArray(a,key):
    M = len(a)
    N = len(a[0])
    m = 0
    n = N - 1
    while m<M and n>=0:
        temp = a[m][n] 
        if key == temp:
            return m,n
        if key < temp:
            n = n - 1
        if key > temp:
            m = m + 1
    return -1

