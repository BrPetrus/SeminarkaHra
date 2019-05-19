import tkinter, queue
from board import Board, drawBorders, getIncome
from player import Player
from panel import Panel

HEIGHT = 400
WIDTH = 400
c = tkinter.Canvas(width = WIDTH, height = HEIGHT)
c.pack()


B = Board() # Create board
P = Panel(0, 350, 50)   # Panel

# Initialise players
players = []
players.append(Player(1, 2, 0, 5, c))
players.append(Player(1, 5, 1, 0, c))

currentPlayer = 0
lastKey = ''
selectedUnit = -1
isRunning = True
winningPlayer = -1

def clickOnBoard(r, c):
    pass

    # # tu sa nic nedeje

    # if B.map[r][c] is players[currentPlayer].colour:
    #     for p in players:
    #         if p.base == (r, c):
    #             #print(True)
    #             pass
    #         else:
    #             pass
    #             #print(False)

# def clickOnPanel(coordinates):
#     drawCoins()

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
    global lastKey, selectedUnit, isRunning, winningPlayer
    if isRunning == False:
        return 0

    if coordinates.y > 300:
        pass
    else:
        row = coordinates.y // 50
        col = coordinates.x // 50

        if row == 0 or row == 6 or col == 0 or col == 7:
            # We clicked outside
            return 0

        if lastKey == '':
            return 0

        cell = checkCellForBasesAndUnits(row, col)

        def moveUnit():
            global selectedUnit
            # Move the selected unit
            players[currentPlayer].units[selectedUnit][0] = row
            players[currentPlayer].units[selectedUnit][1] = col
            # Update map colours
            B.map[row][col] = players[currentPlayer].colour
            # Reset
            selectedUnit = -1
        if lastKey == 'M':
            if selectedUnit == -1: # We have not selected a unit
                if cell != -1 and cell[0] == currentPlayer: # If we clicked on our unit
                    selectedUnit = cell[1]  # Select ths unit for furthe movement
            else:   # We have already selected a unit
                if cell == -1: # Empty cell
                    moveUnit()
                elif len(cell) == 2 and cell[0] != currentPlayer: # Enemy unit
                    if players[currentPlayer].units[selectedUnit][2] > players[cell[0]].units[cell[1]][2]: # if he is stronger
                        # Destroy enemy
                        players[cell[0]].units = players[cell[0]].units[:cell[1]] + players[cell[0]].units[cell[1]+1:]
                        moveUnit()
                elif len(cell) == 1 and cell[0] != currentPlayer:    # Enemy castle
                    moveUnit()
                    isRunning = False
                    winningPlayer = currentPlayer
                    c.create_text(HEIGHT/2, WIDTH/2, text="Vyhral hrac #{:}".format(currentPlayer+1), font='Arial 30 bold')
                    

        elif lastKey == 'A':
            if cell == -1:  # Empty cell
                B.map[row][col] = players[currentPlayer].colour
                players[currentPlayer].addUnit(row, col, 1)
                lastKey = ''
            elif len(cell) == 1:    # Base
                pass
            elif cell[0] == currentPlayer:   # Does it belong to the same player
                # Upgrade unit
                players[currentPlayer].units[cell[1]][2] += 1
                lastKey = ''

    if isRunning == True:    
        draw()
    
def key(event):
    global lastKey
    lastKey = event.char.upper()
    draw()

c.bind('<Button-1>', click)
c.bind_all('<Key>', key)

def nextTurn():
    global currentPlayer, selectedUnit, players
    if isRunning == False:
        return 0
    if currentPlayer == 0:
        currentPlayer = 1
    else:
        currentPlayer = 0

    selectedUnit = -1

    # Income
    players[currentPlayer].income = getIncome(B, players[currentPlayer].base[0], players[currentPlayer].base[1])
    print(players[currentPlayer].income)
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
    if selectedUnit != -1:
        players[currentPlayer].highlightUnit(selectedUnit, c)
    tmp = players[currentPlayer].base
    income = drawBorders(B, tmp[0], tmp[1], c)
    players[currentPlayer].income = income
    drawCoins()

# Mainloop
draw()
c.mainloop()
c.create_text(100, 100, text='BLAAA')


