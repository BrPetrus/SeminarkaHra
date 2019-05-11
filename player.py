class Player:
    def __init__(self, r, c, colour, income, canvas):
        self.base = (r, c)
        self.colour = colour
        self.income = income
        self.troops = []
        self.coins = 0

    def drawBase(self, canvas):
        x, y = 5, 5
        x += self.base[1]*50
        y += self.base[0]*50
        canvas.create_polygon(x, y, x+15, y, x+15, y+10, x+25, y+10, x+25, y, x+40, y,
                            x+40, y+40, x, y+40, tags='player')
    
    def addTroop(self, r, c, canvas):
        self.troops.append((r,c))
