import tkinter, queue
from board import Board, drawBorders
from player import Player
from panel import Panel

HEIGHT = 400
WIDTH = 400
c = tkinter.Canvas(width = WIDTH, height = HEIGHT)
c.pack()

run = True 
def exit():
    global run
    run = False
c.bind('<Escape>', func=exit)

# Create board
B = Board()

P = Panel(0, 350, 50)

# Iniialise players
players = []
players.append(Player(1, 2, 0, 5, c))
players.append(Player(1, 5, 1, 0, c))

currentPlayer = 0

# Key queue
#keys = queue.Queue(maxsize=1)
lastKey = ''

# Moving
selectedUnit = 0

def clickOnBoard(r, c):
    if B.map[r][c] is players[currentPlayer].colour:
        for p in players:
            if p.base == (r, c):
                #print(True)
                pass
            else:
                pass
                #print(False)

def clickOnPanel(coordinates):
    drawCoins()

def checkCellForBasesAndUnits(row, col):
    for iPlayer in range(len(players)):
        p = players[iPlayer]
        if (row, col) == p.base:
            return(iPlayer, )
        for iUnit in range(len(p.units)):
            if p.units[iUnit][0:2] == [row, col]:
                return(iPlayer, iUnit)
    return(-1)

def click(coordinates):
    global lastKey
    if coordinates.y > 300:
        pass
    else:
        row = coordinates.y // 50
        col = coordinates.x // 50

        if row == 0 or row == 6 or col == 0 or col == 7:
            # We clicked outside
            return 0

        clickOnBoard(row, col)

        if lastKey == '':
            return 0

        cell = checkCellForBasesAndUnits(row, col)

        if lastKey == 'M':
            pass
        elif lastKey == 'A':
            if cell == -1:  # Empty cell
                B.map[row][col] = players[currentPlayer].colour
                players[currentPlayer].addUnit(row, col, 1, c)
                lastKey = ''
            elif len(cell) == 1:    # Base
                pass
            elif cell[0] == currentPlayer:   # Does it belong to the same player
                # Upgrade unit
                players[currentPlayer].units[cell[1]][2] += 1
                lastKey = ''
        
    draw()
    
def key(event):
    global lastKey
    lastKey = event.char.upper()
    draw()

c.bind('<Button-1>', click)
c.bind_all('<Key>', key)

def nextTurn():
    global currentPlayer
    if currentPlayer == 0:
        currentPlayer = 1
    else:
        currentPlayer = 0

    # Income
    players[currentPlayer].coins += players[currentPlayer].income 
    draw()

bTurn = tkinter.Button(text='Next Turn', command = nextTurn)
bTurn.place(x=200, y=350)

def drawCoins():
    c.create_text(200, 390, text="Coins: {:}".format(players[currentPlayer].coins), tags='money')
    c.create_text(300, 390, text="Income: {:}".format(players[currentPlayer].income), tags='money')

def draw():
    c.delete('money')
    c.delete('player')
    c.delete('board')
    c.delete('panel')
    B.draw(c)

    select = -1
    if lastKey == 'A':
        select = 0
    P.draw(0,0,select,c)
    
    for p in players:
        p.draw(c)
    tmp = players[currentPlayer].base
    income = drawBorders(B, tmp[0], tmp[1], c)
    players[currentPlayer].income = income
    drawCoins()

# Mainloop
draw()
c.mainloop()
c.create_text(100, 100, text='BLAAA')


