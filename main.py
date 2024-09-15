import tkinter as tk
from tkinter import Button

root = tk.Tk()

for i in range(0,9):
    for j in range(0,9):
        new_button = Button(root)
        new_button.grid(row=i,column=j)

root.mainloop()