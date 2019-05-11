import tkinter
HEIGHT = 400
WIDTH = 400
c = tkinter.Canvas(width = WIDTH, height = HEIGHT, bg='white')
c.pack()

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
                canvas.create_rectangle(x, y, x+50, y+50, fill=self.colours[self.map[r][c]])
                x += 50
            x = 0
            y += 50

class Player:
    pass

B = Board()
B.print()
B.draw(c)
c.mainloop()