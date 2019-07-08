class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if len(matrix) == 0:
            return 0
        if len(matrix[0]) == 0:
            return 0
        h,w = len(matrix),len(matrix[0])
        c = []
        self.result = []
        for i in range(h):
            self.result.append([])
            for j in range(w):
                self.result[-1].append(-1)
        for i in range(h):
            for j in range(w):
                c.append(self.find_path(matrix,[(i,j)]))
        #print (c)

        return max(c)
    
    def find_path(self,matrix,path):            
        i,j = path[-1]
        if self.result[i][j]!=-1:
            return self.result[i][j] + len(path) - 1
        next_step = []
        h,w = len(matrix),len(matrix[0])
        if i>0:
            next_step.append((i-1,j))
        if j<w-1:
            next_step.append((i,j+1))
        if i<h-1:
            next_step.append((i+1,j))
        if j>0:
            next_step.append((i,j-1))
        c = []
        flag = 0
        for s,t in next_step:
            if matrix[s][t]>matrix[i][j]:
                c.append(self.find_path(matrix,path+[(s,t)]))
                flag = 1
        if flag==0:
            res = len(path)
        else:
            res =  max(c)
        self.result[i][j] = res - (len(path) - 1)
        return res
