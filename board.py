import queue
import tkinter

class Board:
    rows = 7
    col = 8

    colours = {
        -1: 'gray',
        -2: 'blue',
        1: 'green',
        0: 'brown'
    }
    
    def __init__(self):
        self.map = [[0] * self.rows] * self.col
        self.generateMap()

    def generateMap(self):
        self.map = [[-2, -2, -2, -2, -2, -2, -2, -2],
                    [-2, -1, 0, -1, -1, 1, -1, -2],
                    [-2, -1, -1, -1, -1, -1, -1, -2],
                    [-2, -1, -1, -1, -1, -1, -1, -2],
                    [-2, -1, -1, -1, -1, -1, -1, -2],
                    [-2, -1, -1, -1, -1, -1, -1, -2],
                    [-2, -2, -2, -2, -2, -2, -2, -2]]

    def print(self):
        print(self.map)

    def draw(self, canvas):
        x, y = 0, 0
        for r in range(len(self.map)):
            for c in range(len(self.map[r])):
                canvas.create_rectangle(x, y, x+50, y+50, fill=self.colours[self.map[r][c]], width=0, outline='white', tags='board')
                x += 50
            x = 0
            y += 50

    def isCellAdjacent(self, row, col, colour):
        """
        Check if there is a neighbourng cell of your own colour.
        """
        # Top
        if self.map[row-1][col] == colour:
            pass
        elif self.map[row+1][col] == colour: # Bottom
            pass
        elif self.map[row][col-1] == colour: # Left
            pass
        elif self.map[row][col+1] == colour: # Right
            pass
        else:
            return False
        return True

def getIncome(board, r, c):
    q = queue.Queue(-1)
    m = list()
    for i in range(board.rows):
        m.append([False]*board.col)
    q.put((r,c))

    n = 0
    while not q.empty():
        cell = q.get()
        r = cell[0]
        c = cell[1]
        colour = board.map[r][c]
        if m[r][c] == True:
            continue
        m[r][c] = True
        n += 1

        # Check neighbours
        # Top
        if r-1 > -1:
            if board.map[r-1][c] == colour:
                if m[r-1][c] == False:
                    q.put((r-1, c))

        # Bottom
        if r+1 < board.rows:
            if board.map[r+1][c] == colour:
                if m[r+1][c] == False:
                    q.put((r+1, c))
        
        # Left
        if c-1 > -1:
            if board.map[r][c-1] == colour:
                if m[r][c-1] == False:
                    q.put((r, c-1))
            
        # Right
        if c+1 < board.col:
            if board.map[r][c+1] == colour:
                if m[r][c+1] == False:
                    q.put((r, c+1))

    return n

def drawBorders(board, r, c, canvas):
    q = queue.Queue(-1)
    m = list()
    for i in range(board.rows):
        m.append([False]*board.col)
    q.put((r,c))

    n = 0
    while not q.empty():
        cell = q.get()
        r = cell[0]
        c = cell[1]
        colour = board.map[r][c]
        if m[r][c] == True:
            continue
        m[r][c] = True
        n += 1

        # Check neighbours
        # Top
        if r-1 > -1:
            if board.map[r-1][c] == colour:
                if m[r-1][c] == False:
                    q.put((r-1, c))
            else:
                canvas.create_line(c*50, r*50, c*50 + 50, r*50, width=2, dash=(4,4), tags='player')

        # Bottom
        if r+1 < board.rows:
            if board.map[r+1][c] == colour:
                if m[r+1][c] == False:
                    q.put((r+1, c))
            else:
                canvas.create_line(c*50, r*50 + 50, c*50 + 50, r*50 + 50, width=2, dash=(4,4), tags='player')

        # Left
        if c-1 > -1:
            if board.map[r][c-1] == colour:
                if m[r][c-1] == False:
                    q.put((r, c-1))
            else:
                canvas.create_line(c*50, r*50, c*50, r*50+50, width=2, dash=(4,4), tags='player')

        # Right
        if c+1 < board.col:
            if board.map[r][c+1] == colour:
                if m[r][c+1] == False:
                    q.put((r, c+1))
            else:
                canvas.create_line(c*50+50, r*50, c*50 + 50, r*50+50, width=2, dash=(4,4), tags='player')
    return n