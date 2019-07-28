class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board) == 0:
            return
        self.h = len(board)
        self.w = len(board[0])
        self.board = board
        for i in range(self.h):
            for j in range(self.w):
                if i == 0 or i == self.h-1 or j == 0 or j == self.w-1:
                    #print (i,j)
                    self.dfs((i,j))
        for i in range(self.h):
            for j in range(self.w):
                if self.board[i][j]=="O":
                    self.board[i][j]="X"
        for i in range(self.h):
            for j in range(self.w):
                if self.board[i][j]=="#":
                    self.board[i][j]="O"
                    
    def dfs(self,pos):
        if self.board[pos[0]][pos[1]] == "O":
            self.board[pos[0]][pos[1]] = "#"
            if pos[0] - 1 >= 0:
                self.dfs((pos[0] - 1,pos[1]))
            if pos[0] + 1 <self.h:
                self.dfs((pos[0] + 1,pos[1]))
            if pos[1] - 1 >= 0:
                self.dfs((pos[0],pos[1]-1))
            if pos[1] + 1 <self.w:
                self.dfs((pos[0],pos[1]+1))
