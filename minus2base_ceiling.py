# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    if len(A) <= 1:
        return []
    if A[0] == 1 and A[1] == 0:
        flag = True
    else:
        flag = False
    if A[0] == 1 and A[1] == 1:
        A[0] = 0
        A[1] = 0
    A.pop(0)
    A.append(0)
    reverse = []
    i = 0
    while i < len(A) - 1:
        if A[i] == 0:
            reverse.append(0)
            i = i + 1
        else:
            reverse.append(1)
            reverse.append(1-A[i+1])
            i = i + 2
    if reverse == []:
        if flag:
            return [1]
        else:
            return []
    else:
        if flag:
            reverse[0] = 1
        while len(reverse) > 0:
            if reverse[-1] == 0:
                reverse.pop()
            else:
                break
        return reverse
