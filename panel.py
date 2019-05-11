class Panel:
    def __init__(self, x, y, height):
        self.x = x
        self.y = y
        self.height = height

    def draw(self, coins, income, selection, canvas):
        canvas.delete('panel')
        x, y = self.x, self.y
        
        # Unit
        canvas.create_oval(x + 5, y + 5, x + 45, y + 45, fill='black', tags='panel')
        x += 50

        # Wall
        canvas.create_rectangle(x + 5, y + 5, x + 45, y + 45, fill='gray', tags='panel')
        x += 50

        # Farm
        canvas.create_rectangle(x + 5, y + 5, x + 45, y + 45, fill='yellow', tags='panel')


