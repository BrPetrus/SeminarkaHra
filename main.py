import tkinter
from board import Board, drawBorders
from player import Player

HEIGHT = 400
WIDTH = 400
c = tkinter.Canvas(width = WIDTH, height = HEIGHT, bg='white')
c.pack()
 

B = Board()
B.print()
B.draw(c)
print(drawBorders(B, 0, 0, c))
drawBorders(B, 3, 3, c)
drawBorders(B, 1, 2, c)
p = Player(1, 3, 1, c)
p = Player(3, 1, 1, c)
c.mainloop()