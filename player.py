class Player:
    def __init__(self, x, y, sprite, keys, gameMap):
        self.x = x
        self.y = y
        self.sprite = sprite
        self.gameMap = gameMap
        commands = {
            "n": lambda: self.move(0,-1),
            "ne": lambda: self.move(1,-1),
            "e": lambda: self.move(1,0),
            "se": lambda: self.move(1,1),
            "s": lambda: self.move(0,1),
            "sw": lambda: self.move(-1,1),
            "w": lambda: self.move(-1,0),
            "nw": lambda: self.move(-1,-1),
        }
        self.commands = []
        for key in keys:
            self.commands.append([key[0], commands[key[1]], 0, 0])

    def useKeys(self, keys):
        try:
            for command in self.commands:
                if keys[command[0]]:
                    if command[2] == 0 or (command[2] > 10 and command[3] > 2):
                        command[1]()
                        command[3] = 0
                    command[2] += 1
                    command[3] += 1
                else:
                    command[2] = 0
                    command[3] = 0
        except:
            pass

    def move(self, x, y, caller=False):
        try:
            if isinstance(caller, Player):
                raise Exception("Cannot push other players.")
            if self.gameMap[self.x + x][self.y + y]:
                self.gameMap[self.x + x][self.y + y].move(x, y, caller=self)
            self.gameMap[self.x][self.y] = 0
            self.x += x
            self.y += y
            self.gameMap[self.x][self.y] = self
        except Exception as error:
            raise error