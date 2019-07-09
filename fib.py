class Solution:
    def fib(self, N: int) -> int:
        if N in [0,1]:
            return N
        a = 0
        b = 1
        for i in range(N):
            a,b = b,a+b
        return a 
