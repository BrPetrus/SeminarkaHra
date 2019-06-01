class Player:
    def __init__(self, r, c, colour, income, canvas):
        self.base = (r, c)
        self.colour = colour
        self.income = income
        self.units = []
        self.coins = 0

    def drawBase(self, canvas):
        x, y = 5, 5
        x += self.base[1]*50
        y += self.base[0]*50
        canvas.create_polygon(x, y, x+15, y, x+15, y+10, x+25, y+10, x+25, y, x+40, y,
                            x+40, y+40, x, y+40, tags='player')
    
    def drawUnits(self, canvas):
        x, y = 0 , 0
        for unit in self.units:
            x, y = unit[1]*50, unit[0]*50
            canvas.create_oval(x+5, y+5, x+45, y+45, fill='black', tags='player')
            if unit[2] >= 2:
                canvas.create_oval(x+10, y+10, x+40, y+40, fill='gray', tags='player')
            if unit[2] == 3:
                canvas.create_oval(x+15, y+15, x+35, y+35, fill='aqua', tags='player')

    def highlightUnit(self, index, canvas):
        y, x = self.units[index][0] * 50, self.units[index][1] * 50
        canvas.create_oval(x+20, y+20, x+30, y+30, fill='yellow', tags='player')

    def draw(self, canvas):
        self.drawBase(canvas)
        self.drawUnits(canvas)

    def addUnit(self, r, c):
        self.units.append([r,c,1])

    def upgradeUnit(self, iUnit):
        lvl = self.units[iUnit][2]
        if lvl <= 2:
            self.units[iUnit][2] += 1

    def doesUnitProtectCell(self, iUnit, r, c):
        """
        Checks if unit at given index does protect given cell.
        """
        unit = self.units[iUnit] # Unit
        
        # Top
        if unit[0]-1 == r and unit[1] == c:
            pass
        elif unit[0]+1 and unit[1] == c: # Bottom
            pass
        elif unit[0] == r and unit[1] == c-1: # Left
            pass
        elif unit[0] == r and unit[1] == c+1: # Right
            pass
        else:
            return False
        return True
