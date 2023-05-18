import pygame
import uuid

from globals import *
from blocks import *

def buildPathMap(x, y):
    pathMap = []
    for i in range(tileCountx):
        column = []
        for j in range(tileCounty):
            column.append(False)
        pathMap.append(column)
    pathMap[x][y] = (x,y,(0,0))
    currentTiles = [pathMap[x][y]]
    newTiles = set()
    while True:
        for tile in currentTiles:
            for i in range(-1,2):
                for j in range(-1,2):
                    newX = tile[0] + i
                    newY = tile[1] + j
                    if (i != 0 or j != 0) and not checkOOBounds((newX,newY)) and not pathMap[newX][newY]:
                        pathMap[newX][newY] = (newX,newY,(-i,-j))
                        if not gameMap[newX][newY]:
                            newTiles.add(pathMap[newX][newY])
        if len(currentTiles) < 1:
            break
        currentTiles = list(newTiles)
        newTiles = set()
    return pathMap

class Player:
    def __init__(self, id, x, y, sprite, keys):
        self.id = id
        self.x = x
        self.y = y
        self.renderPos = (x,y)
        self.pathMap = []
        self.sprite = sprite
        self.pull = False
        self.PLAYER = True
        self.kills = 0
        self.lives = 3
        self.alive = True
        
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
    
    def buildOwnPathMap(self):
        self.pathMap = buildPathMap(self.x, self.y)

    def useKeys(self, keys):
        try:
            if keys[self.pullKey]:
                self.pull = True
            else:
                self.pull = False
            for command in self.commands:
                try:
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
                    command[2] = 0
                    command[3] = 0
        except:
            pass

    def move(self, x, y):
        try:
            if checkOOBounds((self.x + x, self.y + y)):
                raise Exception("Cannot move off edge!")
            pulling = self.pull and hasattr(gameMap[self.x - x][self.y - y], "BLOCK")
            if gameMap[self.x + x][self.y + y]:
                if pulling:
                    raise Exception("Cannot push and pull at the same time")
                gameMap[self.x + x][self.y + y].pushed(x, y, self, self)
            gameMap[self.x][self.y] = False
            self.x += x
            self.y += y
            gameMap[self.x][self.y] = self
            for id, player in players.items():
                try:
                    player.buildOwnPathMap()
                except Exception as error:
                    print(error)
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
        maxTries = 5
        for i in range(maxTries + 1):
            if self.lives < 1:
                del players[self.id]
                self.alive = False
                break
            if i == maxTries:
                raise Exception("No spots found for player!")
            try:
                spot = [random.randint(0, tileCountx - 1), random.randint(0, tileCounty - 1)]
                if gameMap[spot[0]][spot[1]]:
                    raise Exception("spot taken!")
                gameMap[spot[0]][spot[1]] = self
                self.x = spot[0]
                self.y = spot[1]
                self.lives -= 1
                try:
                    self.buildOwnPathMap()
                except Exception as error:
                    print(error)
                break
            except Exception as error:
                continue