class Player:
    def __init__(self, r, c, colour, canvas):
        self.base = (r, c)
        self.colour = colour
        self.drawBase(canvas)
    
    def drawBase(self, canvas):
        x, y = 5, 5
        x += self.base[1]*50
        y += self.base[0]*50
        canvas.create_polygon(x, y, x+15, y, x+15, y+10, x+25, y+10, x+25, y, x+40, y,
                            x+40, y+40, x, y+40)
