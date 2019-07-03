# Q3
# enumerate the list
# for each i,m:
# loop:
# if i==m: go to the next digit
# else: then compare whether l[m] is m, if yes, found the duplicate
# else: put m to where it should be in l[m]
def find_duplicate(l):
    for i in range(len(l)):
        while True:
            m = l[i]
            if i == l[i]:
                break
            if l[m] == m:
                return m
            else:
                l[m],l[i] = l[i],l[m]


print (find_duplicate([3,1,0,2,5,3]))
            
            
