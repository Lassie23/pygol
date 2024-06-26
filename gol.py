import pygame
import random
pygame.init()
def getconfig():
    global bx
    global by
    global res
    global grl
    global survival
    global birth
    global randomcell
    print()
    bx = input("enter board width(leave blank for 192): ")
    by = input("enter board height(leave blank for 108): ")
    res = input("enter cell size in pixels(leave blank for 10): ")
    grl = input("enter grid line thickness in pixels(leave blank for 1, or 0 for no grid lines): ")
    survival = input("enter survival conditions(leave blank for 23, classic GOL, or 9 for no survival): ")
    birth = input("enter birth conditions(leave blank for 3, classic GOL, or 9 for no birth): ")
    randomcell = input("randomise cells? [Y/n]: ")
    if bx == "":
        bx = 192
    else:
        bx = int(bx)
    if by == "":
        by = 108
    else:
        by = int(by)
    if res == "":
        res = 10
    else:
        res = int(res)
    if grl == "":
        grl = 1
    else:
        grl = int(grl)
    if survival == "":
        survival = "23"
    if birth == "":
        birth = "3"
    if randomcell.lower() in ["","y","yes"]:
        randomcell = lambda : random.choice([0,0,1])
    else:
        randomcell = lambda : 0
def makescreen():
    global screen
    global board
    global sboard
    screen = pygame.display.set_mode((bx*res, by*res))
    board = [[randomcell() for y in range(0,by)] for x in range(0,bx)]
    sboard = [[0 for y in range(0,by)] for x in range(0,bx)]
getconfig()
makescreen()
def updateboard():
    x = -1
    for a in board:
        x += 1
        y = -1
        for b in a:
            y += 1
            z = str(
            board[(x-1)%bx][(y-1)%by] +
            board[(x-1)%bx][y] +
            board[(x-1)%bx][(y+1)%by] +
            board[x][(y-1)%by] +
            board[x][(y+1)%by] +
            board[(x+1)%bx][(y-1)%by] +
            board[(x+1)%bx][y] +
            board[(x+1)%bx][(y+1)%by])
            if board[x][y] == 1:
                if z in survival:
                    sboard[x][y] = 1
                else:
                    sboard[x][y] = 0
            else:
                if z in birth:
                    sboard[x][y] = 1
    x = -1
    for a in board:
        x += 1
        y = -1
        for b in a:
            y += 1
            board[x][y] = sboard[x][y]
def draw():
    screen.fill((0,0,0))
    x = -1
    for a in board:
        x += 1
        y = -1
        for b in a:
            y += 1
            if b == 1:
                screen.fill((255,255,255),(x * res,y * res,res,res))
    for x in range(1,bx):
        screen.fill((128,128,128),(x*res,0,grl,by*res))
    for y in range(1,by):
        screen.fill((128,128,128),(0,y*res,bx*res,grl))
    pygame.display.flip()
draw()
while True:
    for event in pygame.event.get():
        if event.type == 771:
            if event.__dict__["text"] == " ":
                updateboard()
            elif event.__dict__["text"] == "r":
                board = [[randomcell() for y in range(0,by)] for x in range(0,bx)]
            elif event.__dict__["text"] == "c":
                pygame.display.quit()
                getconfig()
                makescreen()
            draw()
        if event.type == 1025:
            x = event.__dict__["pos"][0]//res
            y = event.__dict__["pos"][1]//res
            if board[x][y] == 0:
                board[x][y] = 1
            else:
                board[x][y] = 0
            draw()
        elif event.type == pygame.QUIT:
            quit()
