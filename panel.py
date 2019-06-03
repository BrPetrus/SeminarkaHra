class Panel:
    def __init__(self, x, y, height):
        self.x = x
        self.y = y
        self.height = height

    def draw(self, coins, income, selection, canvas):
        x, y = self.x, self.y
        x += 10
        
        # Unit
        if selection == 0:
            canvas.create_rectangle(x-10, y, x+60, y+50, fill='orange', tags='panel')
        #canvas.create_oval(x + 5, y + 5, x + 45, y + 45, fill='black', tags='panel')
        canvas.create_text(x+25, y+25, text='Add', font='Arial 18 bold', tags='panel')
        x += 50

        # Wall
        #canvas.create_rectangle(x + 5, y + 5, x + 45, y + 45, fill='gray', tags='panel')
        x += 30

        # Farm
        #canvas.create_rectangle(x + 5, y + 5, x + 45, y + 45, fill='yellow', tags='panel')

        # Move
        if selection == 1:
            canvas.create_rectangle(x-10, y, x+60, y+50, fill='orange', tags='panel')
        canvas.create_text(x+27, y+25, text='Move', font='Arial 18 bold', tags='panel')


