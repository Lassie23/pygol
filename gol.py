bx = 10
by = 10
board = [0,0,0,0,0,0,0,0,0,0,
         0,1,0,0,0,0,0,0,0,0,
         0,0,1,1,0,0,0,0,0,0,
         0,1,1,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,0,0,0]
sboard = [0,0,0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0,0,0,0]
def updateboard():
    x = -1
    for y in board:
        x = x + 1
        if x % bx != 0 and x % bx != bx - 1:
            if x > bx - 1 and x < bx * by - bx:
                sboard[x] = board[x-bx-1] + board[x-bx] + board[x-bx+1] + board[x-1] + board[x+1] + board[x+bx-1] + board[x+bx] + board[x+bx+1]
    x = -1
    for y in board:
        x = x + 1
        if board[x] == 1:
            if sboard[x] < 2 or sboard[x] > 3:
                board[x] = 0
        else:
            if sboard[x] == 3:
                board[x] = 1
while True:
    input(board)
    updateboard()