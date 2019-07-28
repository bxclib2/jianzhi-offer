import numpy as np
dx = [1,2,2,1,-1,-2,-2,-1]
dy = [2,1,-1,-2,-2,-1,1,2]
def knight_travesal(n = 8,start = (0,0)):
    chess_board = np.zeros((n,n)) - 1
    step = 0
    res = dfs(chess_board,step,start,n)
    if res[0] is True:
        print (res[1])
    else:
        print ("No solution")
def dfs(chess_board,step,start,n):
    option = []
    chess_board[start[0],start[1]] = step   
    if step == n*n-1:
        return True,chess_board
    for i,j in zip(dx,dy):
        if start[0]+i in range(n) and start[1]+j in range(n) and chess_board[start[0]+i,start[1]+j] == -1:
            option.append((start[0]+i,start[1]+j))
    if option == []:
        #print (chess_board)
        return False,chess_board

    while option!=[]:
        next_pos = option.pop(0)
        res = dfs(chess_board.copy(),step+1,next_pos,n)
        if res[0] is True:
            return res
    return False,chess_board
