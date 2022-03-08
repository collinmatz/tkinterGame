# GUI.py
# responsible for drawing the sreen every tick

from tkinter import *
from time import sleep

class GUI():
    def __init__(self, root, tickSpeed):
        # create / initialize root screen
        self.root = root # <-- main game root
        self.root.title("Dungeon Quest")
        self.root.geometry("500x500")
        self.root.resizable(0,0)

        # create / initialize canvas
        self.canvas = Canvas(self.root, height=500, width=500)
        self.canvas.pack()
        self.tickSpeed = tickSpeed
        self.MAX_FPS = 60

    def update():
        print("updating")

    
