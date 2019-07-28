class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        self.board = board
        self.h = len(board)
        if board == 0:
            return False
        self.w = len(board[0])
        passed = []
        for i in range(self.h):
            for j in range(self.w):
                if self.dfs((i,j),word,passed.copy()):
                    return True
        return False
        
        
    def dfs(self,pos,string,passed):
        if string == "":
            return True
        else:
            if string[0] == self.board[pos[0]][pos[1]]:
                passed.append(pos)
                if string[1:]=="":
                    return True
                if pos[0]-1>=0 and (pos[0]-1,pos[1]) not in passed:
                    res = self.dfs((pos[0]-1,pos[1]),string[1:],passed.copy())
                    if res == True:
                        return True
                if pos[0]+1<self.h and (pos[0]+1,pos[1]) not in passed:
                    res = self.dfs((pos[0]+1,pos[1]),string[1:],passed.copy())
                    if res == True:
                        return True                
                if pos[1]+1<self.w and (pos[0],pos[1]+1) not in passed:
                    res = self.dfs((pos[0],pos[1]+1),string[1:],passed.copy())
                    if res == True:
                        return True             
                if pos[1]-1>=0 and (pos[0],pos[1]-1) not in passed:
                    res = self.dfs((pos[0],pos[1]-1),string[1:],passed.copy())
                    if res == True:
                        return True       
        return False
