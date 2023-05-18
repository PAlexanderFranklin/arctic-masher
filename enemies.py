import pygame
import uuid
import random

from globals import *
from player import Player
from blocks import Block

def findClosestPlayer(x, y):
    closestPlayerPosition = {"difference": (1,1), "distance": 9999}
    for id, player in players.items():
        difference = (player.x - x, player.y - y)
        distance = max(abs(difference[0]), abs(difference[1]))
        if distance > closestPlayerPosition["distance"]:
            continue
        closestPlayerPosition = {"difference": difference, "distance": distance}
    return closestPlayerPosition

class Enemy:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y
        self.AITime = random.randint(150, 200)
        

    def die(self):
        del enemies[self.id]

    def pushed(self, x, y, caller, pusher):
        if isinstance(pusher, Player) and isinstance(caller, Block):
            wallCrush = self.x + x > tileCountx - 1 or self.y + y > tileCounty - 1 or self.x + x < 0 or self.y + y < 0
            if wallCrush or isinstance(gameMap[self.x + x][self.y + y], Block):
                self.die()
                return
        raise Exception("Not crushing enemy!")
    
    def move(self, x, y):
        try:
            if self.x + x > tileCountx - 1 or self.y + y > tileCounty - 1 or self.x + x < 0 or self.y + y < 0:
                raise Exception("Cannot move off edge!")
            if gameMap[self.x + x][self.y + y]:
                if isinstance(gameMap[self.x + x][self.y + y], Player):
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