class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """
        :type n: int
        :rtype: List[List[str]]
        """
        l=[]
        square=[]
        self.n=n
        self.putQueens(0,square,l)
        return l
    def notDanger(self,column,square):
        for s,i in enumerate(square):
            
            if i[column]=="Q":
                return False
            f=column+len(square)-s
            if f>=0 and f<self.n:
                if i[f]=="Q":
                    return False
            f=column-len(square)+s
            if f>=0 and f<self.n:
                if i[f]=="Q":
                    return False
        return True
    def putQueens(self,row,square,l):
        if row==self.n:
            l.append(square)
        else:
            for i in range(self.n):
                if (self.notDanger(i,square)):
                    s="."*self.n
                    s=s[:i]+"Q"+s[i+1:]
                    square2=square[::]
                    square2.append(s)
                    self.putQueens(row+1,square2,l)
