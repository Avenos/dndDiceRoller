
from random import randint
import tkinter as tk

top = tk.Tk()
top.title("D&D Dice Roller")
top.resizable(width=False, height=False)
top.geometry("440x50")

result = tk.Label(top, font = (None, 30), height = 50, width = 10)

def roll(sides):
    newtext = "D%i: " % sides + str(randint(1, sides))
    #newtext = str(randint(1, sides))
    result.config(text = newtext)

d4 = tk.Button(top, text = "D4", height = 50, width = 5, command = lambda: roll(4))
d6 = tk.Button(top, text = "D6", height = 50, width = 5, command = lambda: roll(6))
d8 = tk.Button(top, text = "D8", height = 50, width = 5, command = lambda: roll(8))
d10 = tk.Button(top, text = "D10", height = 50, width = 5, command = lambda: roll(10))
d12 = tk.Button(top, text = "D12", height = 50, width = 5, command = lambda: roll(12))
d20 = tk.Button(top, text = "D20", height = 50, width = 5, command = lambda: roll(20))

d4.pack(side=tk.LEFT)
d6.pack(side=tk.LEFT)
d8.pack(side=tk.LEFT)
d10.pack(side=tk.LEFT)
d12.pack(side=tk.LEFT)
d20.pack(side=tk.LEFT)
result.pack(side=tk.LEFT)

top.mainloop()