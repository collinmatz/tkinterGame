# class to create player objects
#   must be passed a root frame; may be passed a starting x and y coordinate

class Player():
    def __init__(self, root, startx=250, starty=250):
        self.root = root
        self.x = startx
        self.y = starty
        self.root.bind("<KeyPress>", self.keyPress)
        self.root.bind("<KeyRelease>", self.keyRelease)

        # player inventory: stored in playerData.txt
        self.inv = []
        try:
            f = open("playerData.txt", "r")
        except:
            print("Error, file not found. Please check the root directory")
        else:
            print(f.read(1))
            f.close()

        # player stats
        self.health = 0
        self.damage = 0
        self.speed = 0

    def keyRelease(self, keyInput):
        c = keyInput.char
        print("released", c)

    def keyPress(self, keyInput):
        c = keyInput.char
        if (c == "w"):
            self.y -= 10
            print(self.y)
        if (c == "s"):
            self.y += 10
            print(self.y)
        if (c == "a"):
            self.x -= 10
            print(self.x)
        if (c == "d"):
            self.x += 10
            print(self.x)