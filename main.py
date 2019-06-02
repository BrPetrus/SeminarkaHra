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
players.append(Player(1, 5, 1, 5, c))

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

def checkCell(row, col):
    for iPlayer in range(len(players)):
        p = players[iPlayer]
        if (row, col) == p.base:
            return(1, iPlayer)  # Base
        for iUnit in range(len(p.units)):
            if p.units[iUnit][0:2] == [row, col]:
                return(2, iPlayer, iUnit)   # Unit
    if B.map[row][col] != -1:
        return(0, B.map[row][col])  # Cell
    return None # Empty cell

def isCellProtectedByEnemy(row, col):
    iEnemy = 1 if currentPlayer == 0 else 0
    enemy = players[iEnemy]
    maxLevel = 0
    for iUnit in range(len(enemy.units)):
        if enemy.doesUnitProtectCell(iUnit, row, col): # If it does protect
            maxLevel = max(maxLevel, enemy.units[iUnit][2])
    return maxLevel

def canPlayerTakeCell(row, cell, iUnit):
    unit = players[currentPlayer].units[iUnit]
    if unit[2] == 3: # if lvl 3, then takes anything
        return True
    else:
        lvl = isCellProtectedByEnemy(row, cell)
        print(lvl)
        if lvl < unit[2]:
            return True
    return False
    

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

        cell = checkCell(row, col)

        def moveUnit():
            global selectedUnit
            # Move the selected unit
            players[currentPlayer].units[selectedUnit][0] = row
            players[currentPlayer].units[selectedUnit][1] = col
            # Update map colours
            B.map[row][col] = players[currentPlayer].colour
            
            # Reset action points
            players[currentPlayer].ableToMove[selectedUnit] = False
            selectedUnit = -1

        def createUnit(t):
            if players[currentPlayer].coins >= 5:
                B.map[row][col] = players[currentPlayer].colour
                players[currentPlayer].addUnit(row, col, t)
                players[currentPlayer].coins -= 5

        if lastKey == 'M':
            if selectedUnit == -1: # We have not selected a unit
                if cell != None and cell[0] == 2 and cell[1] == currentPlayer: # If we clicked on our unit
                    selectedUnit = cell[2]  # Select ths unit for further movement
            elif selectedUnit != -1 and players[currentPlayer].ableToMove[selectedUnit] and B.isCellAdjacent(row, col, players[currentPlayer].colour): # If we selected a unit and is adjacent to already owned cell
                if cell == None: # Empty cell
                    moveUnit()
                elif cell[0] == 0 and cell[1] == currentPlayer: # Our own empty cell
                    moveUnit()
                elif cell[0] == 2 and cell[1] == currentPlayer: # We clicked on our own unit
                    selectedUnit = cell[2]
                elif cell[0] == 0 and cell[1] != currentPlayer and canPlayerTakeCell(row, col, selectedUnit): # Enemy cell
                    moveUnit()
                elif cell[0] == 2 and cell[1] != currentPlayer: # Enemy unit
                    if players[currentPlayer].units[selectedUnit][2] > players[cell[1]].units[cell[2]][2]: # if he is stronger
                        # Destroy enemy
                        players[cell[1]].units = players[cell[1]].units[:cell[2]] + players[cell[1]].units[cell[2]+1:]
                        moveUnit()
                elif cell[0] == 1 and cell[1] != currentPlayer and canPlayerTakeCell(row, col, selectedUnit) : # Enemy castle
                    moveUnit()
                    isRunning = False
                    winningPlayer = currentPlayer
                    c.create_text(HEIGHT/2, WIDTH/2, text="Vyhral hrac #{:}".format(currentPlayer+1), font='Arial 30 bold')  
            else:
                selectedUnit = -1

        elif lastKey == 'A':
            if cell == None and B.isCellAdjacent(row, col, players[currentPlayer].colour): # If its an empty cell and adjacent to us
                createUnit(False)
            elif cell == None:
                pass
            elif cell[0] == 0 and cell[1] == currentPlayer: # Empty but our cell
                createUnit(True)
            elif cell[0] == 0 and cell[1] != currentPlayer and canPlayerTakeCell(row, col, selectedUnit): # Empty enemy cell
                createUnit(False)
            elif cell[0] == 2 and cell[1] == currentPlayer: # Upgrade unit
                players[currentPlayer].upgradeUnit(cell[2])

    if isRunning == True:    
        draw()
    
def key(event):
    global lastKey, selectedUnit
    lastKey = event.char.upper()
    if lastKey == 'A':
        selectedUnit = -1
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

    players[currentPlayer].resetMoves()
    selectedUnit = -1

    # Income
    players[currentPlayer].income = getIncome(B, players[currentPlayer].base[0], players[currentPlayer].base[1])
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


