class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.res = []
        self.nums = range(1,n+1)
        self.k = k
        for pos,n in enumerate(self.nums):
            self.backtrace([],n,pos)
        return self.res
        
    def backtrace(self, temp, n, pos):
        temp.append(n)
        if len(temp) == self.k:
            self.res.append(temp)
        else:
            for i,n_ in enumerate(self.nums[pos:]):
                if n!=n_:
                    if len(temp) + len(self.nums)  - pos + 1 >= self.k:
                        self.backtrace(temp.copy(),n_,pos+i)
