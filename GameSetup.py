from tkinter import *
import tkinter as tk
from tkinter import ttk

class GameSetup():
    def __init__(self, root):
        print("Game Setup Initialized")
        self.greetingWindow = self.openGreeting()
        self.settingsWindow = self.openSettings()
        self.root = root
        self.greetingWindow.pack()

    def startGame(self):
        # destroy active windows and transfer control
        self.greetingWindow.destroy()
        self.root.destroy()

    def switchToSettings(self):
        self.greetingWindow.destroy()
        self.settingsWindow = self.openSettings()
        self.settingsWindow.pack()

    def switchToGreeting(self):
        self.settingsWindow.destroy()
        self.greetingWindow = self.openGreeting()
        self.greetingWindow.pack()

    def openSettings(self):
        settings = Frame(self.root) # create settings frame
        
        title = Label(settings, text="SETTINGS", justify=CENTER)
        backButton = Button(settings, text="BACK", justify=CENTER, command=self.switchToGreeting)

        title.pack()
        backButton.pack()
        return settings

    def openGreeting(self):
        intro = Frame(self.root) # create intro frame
        text = R'''
 _____  _    _ _   _  _____ ______ ____  _   _    ____  _    _ ______  _____ _______ 
|  __ \| |  | | \ | |/ ____|  ____/ __ \| \ | |  / __ \| |  | |  ____|/ ____|__   __|
| |  | | |  | |  \| | |  __| |__ | |  | |  \| | | |  | | |  | | |__  | (___    | |   
| |  | | |  | | . ` | | |_ |  __|| |  | | . ` | | |  | | |  | |  __|  \___ \   | |   
| |__| | |__| | |\  | |__| | |___| |__| | |\  | | |__| | |__| | |____ ____) |  | |   
|_____/ \____/|_| \_|\_____|______\____/|_| \_|  \___\_\\____/|______|_____/   |_|   

    '''
        greeting = Label(intro, text=text, font="TkFixedFont", fg="red")
        playButton = Button(intro, text="PLAY", command=self.startGame) # start game
        settingsButton = Button(intro, text="SETTINGS", command=self.switchToSettings) # open settings

        greeting.pack()
        playButton.pack()
        settingsButton.pack()
        return intro
