def bucketSort(l,bucket_num = 5):
    if l == []:
        return l
    minimal = min(l)
    # 这里为了后面程序好写，把范围扩大一点点，要不最大值还要单独处理，挺麻烦的
    maximal = max(l) + 1
    bucket_range = []
    bucket = []
    for i in range(bucket_num):
        bucket.append([])
    for i in range(bucket_num):
        bucket_range.append((minimal+i*(maximal-minimal)/bucket_num,minimal+(i+1)*(maximal-minimal)/bucket_num))
    for n in l:
        for i,(a,b) in enumerate(bucket_range):
            if n >= a and n < b:
                   bucket[i] .append(n)
    res = []
    for b in bucket:
        res = res + sorted(b)
    return res


l = [4,5,9,7,1,5,8,9,8,7,1,2,7,9,3]
print (bucketSort(l))
