import queue
import tkinter

class Board:
    rows = 4
    col = 4

    colours = {
        -1: 'blue',
        -2: 'gray',
        1: 'green',
        0: 'brown'
    }
    
    def __init__(self):
        self.map = [[0] * self.rows] * self.col
        self.generateMap()

    def generateMap(self):
        self.map = [[-2, -2, -2, -2],[-2, -2, 0, 0],[-2, 1, 1, -2],[-2, 1, -2, -2]]

    def print(self):
        print(self.map)

    def draw(self, canvas):
        x, y = 0, 0
        for r in range(len(self.map)):
            for c in range(len(self.map[r])):
                canvas.create_rectangle(x, y, x+50, y+50, fill=self.colours[self.map[r][c]], width=0, outline='white')
                x += 50
            x = 0
            y += 50

def drawBorders(board, r, c, canvas):
    q = queue.Queue()
    m = [[False, False, False, False], [False, False, False, False], [False, False,False,False], [False,False,False,False]]
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
                canvas.create_line(c*50, r*50, c*50 + 50, r*50, width=2, dash=(4,4))

        # Bottom
        if r+1 < 4:
            if board.map[r+1][c] == colour:
                if m[r+1][c] == False:
                    q.put((r+1, c))
            else:
                canvas.create_line(c*50, r*50 + 50, c*50 + 50, r*50 + 50, width=2, dash=(4,4))

        # Left
        if c-1 > -1:
            if board.map[r][c-1] == colour:
                if m[r][c-1] == False:
                    q.put((r, c-1))
            else:
                canvas.create_line(c*50, r*50, c*50, r*50+50, width=2, dash=(4,4))

        # Right
        if c+1 < 4:
            if board.map[r][c+1] == colour:
                if m[r][c+1] == False:
                    q.put((r, c+1))
            else:
                canvas.create_line(c*50+50, r*50, c*50 + 50, r*50+50, width=2, dash=(4,4))
    return n