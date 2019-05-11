import tkinter
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
B.print()

P = Panel(0, 350, 50)

# Iniialise players
players = []
players.append(Player(1, 2, 0, 5, c))
players.append(Player(1, 5, 1, 0, c))

currentPlayer = 0
def clickOnBoard(r, c):
    if B.map[r][c] is players[currentPlayer].colour:
        for p in players:
            if p.base == (r, c):
                print(True)
            else:
                print(False)

def clickOnPanel(coordinates):
    drawCoins()

def click(coordinates):
    if coordinates.y > 300:
        clickOnPanel(coordinates)
    else:
        r = coordinates.y // 50
        c = coordinates.x // 50
        clickOnBoard(r, c)
    

c.bind('<Button-1>', click)

def nextTurn():
    global currentPlayer
    if currentPlayer == 0:
        currentPlayer = 1
    else:
        currentPlayer = 0
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
    P.draw(0,0,0,c)
    for p in players:
        p.drawBase(c)
    tmp = players[currentPlayer].base
    drawBorders(B, tmp[0], tmp[1], c)
    drawCoins()

# Mainloop
draw()
c.mainloop()
c.create_text(100, 100, text='BLAAA')


