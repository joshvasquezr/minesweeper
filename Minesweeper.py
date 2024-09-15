from tkinter import Tk, Button
import random

class Minesweeper:
    def __init__(self, root, rows, cols):
        self.root = root
        self.rows = rows
        self.cols = cols
        self.grid = []


    def create_grid(self):
        for i in range(self.rows):
            for j in range(self.cols):
                new_button = Button(self.root, text =" ")
                new_button.grid(row=i, column=j)

    def place_mines(self, n):
        for _ in range(n):
            r1 = random.randint(0,9)
            r2 = random.randint(0, 9)
            mine_index = [r1, r2]

        for i in range(0,9):
            for j in range(0,9):


root = Tk()

game = Minesweeper(root, 9, 9)

game.create_grid()

root.mainloop()