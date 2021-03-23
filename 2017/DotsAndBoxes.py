#inputList = input().split()
#p1, m1, p2, m2, t = inputList

#initialize 2d array for Boxes Made
boxes = [["*" for i in range(5)] for j in range(5)]

#initialize 3d Array for the Dots on the board
#1st Dimention is the X co-ordinate of the Dot
#2nd Dimention is the X co-ordinate of the Dot
#3rd Dimention is the X and y of connected dots
board = [[[]for i in range(6)] for j in range(6)]

def connectDots(x1,y1,x2,y2):
    board[x1][y1].append([x2, y2])
    board[x2][y2].append([x1, y1])

def completeSquare(x,y):
    Connections = [False, False, False, False]
    if [x+1,y] in board[x][y]:
        Connections[0] = True
    if [x,y+1] in board[x][y]:
        Connections[1] = True
    if x < len(board) - 1:
        if [x+1,y+1] in board[x+1][y]:
            Connections[2] = True
    if y < len(board) - 1:
        if [x+1, y+1] in board[x][y+1]:
            Connections[3] = True
    return not False in Connections

def movePlayer1(pos, mod):
    if mod+pos > 36:
        pos = (mod+pos)%36
    x, y = (((mod+pos) % 6)), ((mod+pos-1)//6) + 1
    if x == 0:
        x = 5
    print(x)
    print(y)
    if y > 6:
        y = 0
    if [x, y-1] not in board[x][y] and y != 0:
        connectDots(x,y,x,y-1)
    elif [x+1,y] not in board[x][y] and x != 5:
        connectDots(x,y,x+1,y)
    elif [x, y+1] not in board[x][y] and y != 5:
        connectDots(x,y,x,y+1)
    elif [x-1, y] not in board[x][y] and x != 0:
        connectDots(x,y,x-1,y)
    


movePlayer1(1,1)
movePlayer1(2,1)
movePlayer1(7,1)
movePlayer1(8,1)
print(completeSquare(0,0))
