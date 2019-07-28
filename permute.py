class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.nums = nums
        for n in self.nums:
            self.backtrace([],n)
        return self.res
        
    def backtrace(self, temp, n):
        temp.append(n)
        if len(temp) == len(self.nums):
            self.res.append(temp)
        else:
            for n in self.nums:
                if n not in temp:
                    self.backtrace(temp.copy(),n)
