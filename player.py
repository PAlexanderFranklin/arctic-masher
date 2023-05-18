import uuid

from globals import *
from blocks import Block

class Player:
    def __init__(self, id, x, y, sprite, keys):
        self.id = id
        self.x = x
        self.y = y
        self.sprite = sprite
        self.pull = False
        
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
            if key[1] == "p":
                self.pullKey = key[0]
            else:
                self.commands.append([key[0], commands[key[1]], 0, 0])

    def useKeys(self, keys):
        try:
            if keys[self.pullKey]:
                self.pull = True
            else:
                self.pull = False
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

    def move(self, x, y):
        try:
            if self.x + x > tileCountx - 1 or self.y + y > tileCounty - 1 or self.x + x < 0 or self.y + y < 0:
                raise Exception("Cannot move off edge!")
            pulling = self.pull and isinstance(gameMap[self.x - x][self.y - y], Block)
            if gameMap[self.x + x][self.y + y]:
                if pulling:
                    raise Exception("Cannot push and pull at the same time")
                gameMap[self.x + x][self.y + y].pushed(x, y, self, self)
            gameMap[self.x][self.y] = False
            self.x += x
            self.y += y
            gameMap[self.x][self.y] = self
            try:
                if pulling:
                    gameMap[self.x - 2*x][self.y - 2*y].pulled(x, y)
            except:
                pass
        except Exception as error:
            raise error
    
    def pushed(self, x, y, caller, pusher):
        raise Exception("Cannot push other players.")
    
    def die(self):
        del players[self.id]