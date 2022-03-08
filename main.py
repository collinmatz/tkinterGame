from tkinter import *
from GameSetup import GameSetup
from GUI import GUI
from Player import Player
from Enemy import Enemy

class StartGameIntro(GameSetup):
    def __init__(self):
        self.root = Tk()
        self.root.title("Welcome, traveler...")
        GameSetup.__init__(self, self.root)
        self.root.mainloop()

def main():
    startGameIntro = StartGameIntro()

    root = Tk() # main game root
    gui = GUI(root, 10) # create GUI for game
    player = Player(gui.canvas)
    root.mainloop() # start game
    

if __name__ == "__main__":
    main()