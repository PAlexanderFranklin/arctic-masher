import pygame
import uuid
import random

from globals import *
from utilities import *
from player import *
from blocks import *

def findClosestPlayer(x, y):
    closestPlayerPosition = {"difference": (1,1), "distance": 9999}
    for id, player in players.items():
        difference = (player.x - x, player.y - y)
        distance = max(abs(difference[0]), abs(difference[1]))
        if distance > closestPlayerPosition["distance"]:
            continue
        closestPlayerPosition = {"difference": difference, "distance": distance, "player": player}
    return closestPlayerPosition

class Enemy:
    def __init__(self, id, x, y):
        self.id = id
        self.ENEMY = True
        self.x = x
        self.y = y
        self.renderPos = (x,y)
        # self.AITime = random.randint(350, 600)
        self.AITime = random.randint(10, 50)
        self.deathColor = white
        
    def die(self):
        del enemies[self.id]

    def pushed(self, x, y, caller, pusher):
        if hasattr(pusher, "PLAYER") and hasattr(caller, "BLOCK"):
            if checkOOBounds((self.x + x, self.y + y)) or hasattr(gameMap[self.x + x][self.y + y], "BLOCK"):
                pusher.kills += 1
                caller.color = self.deathColor
                self.die()
                return
        raise Exception("Not crushing enemy!")
    
    def move(self, x, y):
        try:
            if checkOOBounds((self.x + x, self.y + y)):
                raise Exception("Cannot move off edge!")
            if gameMap[self.x + x][self.y + y]:
                if hasattr(gameMap[self.x + x][self.y + y], "PLAYER"):
                    gameMap[self.x + x][self.y + y].die()
                else:
                    raise Exception("Path is blocked.")
            gameMap[self.x][self.y] = False
            self.x += x
            self.y += y
            gameMap[self.x][self.y] = self
        except Exception as error:
            raise error
    
    def runAI(self):
        self.AITime -= 1
        if self.AITime < 1:
            try:
                closestPlayer = findClosestPlayer(self.x, self.y)
                weightsx = [-closestPlayer["difference"][0], abs(closestPlayer["difference"][1]), closestPlayer["difference"][0]]
                if weightsx[0] < 0:
                    weightsx[0] = weightsx[2]/6
                elif weightsx[2] < 0:
                    weightsx[2] = weightsx[0]/6
                else:
                    weightsx[0] = weightsx[1]/8
                    weightsx[2] = weightsx[1]/8
                weightsy = [-closestPlayer["difference"][1], abs(closestPlayer["difference"][0]), closestPlayer["difference"][1]]
                if weightsy[0] < 0:
                    weightsy[0] = weightsy[2]/6
                elif weightsy[2] < 0:
                    weightsy[2] = weightsy[0]/6
                else:
                    weightsy[0] = weightsy[1]/8
                    weightsy[2] = weightsy[1]/8
                movementx = random.choices([-1, 0, 1], weightsx)[0]
                movementy = random.choices([-1, 0, 1], weightsy)[0]
                self.move(movementx, movementy)
                self.AITime = random.randint(150, 200)
            except Exception as error:
                pass

class Smart(Enemy):
    def __init__(self, id, x, y):
        Enemy.__init__(self, id, x, y)
        self.deathColor = red
        self.trackedPlayer = False
        self.trackingCounter = 0
    
    def runAI(self):
        self.AITime -= 1
        if self.AITime < 1:
            try:
                if self.trackedPlayer and self.trackedPlayer.alive:
                    fastDir = self.trackedPlayer.pathMap[self.x][self.y][2]
                    # movementx = random.choices([-1, 0, 1], weightsx)[0]
                    # movementy = random.choices([-1, 0, 1], weightsy)[0]
                    movementx = fastDir[0]
                    movementy = fastDir[1]
                    # self.move(movementx, movementy)
                    self.trackingCounter -= 1
                    if self.trackingCounter < 1:
                        self.AITime = random.randint(500, 1000)
                        self.trackedPlayer = False
                    self.AITime = random.randint(10, 15)
                else:
                    closestPlayer = findClosestPlayer(self.x, self.y)
                    self.trackedPlayer = closestPlayer["player"]
                    self.trackingCounter = 8
                    self.AITime = random.randint(10, 15)
            except Exception as error:
                print(error)