import pygame

from constants import *

class Enemy:
    def __init__(self, x, y, gameMap):
        self.x = x
        self.y = y
        self.gameMap = gameMap

    def pushed(self, x, y, caller, pusher):
        if self.x + x > tileCountx - 1 or self.y + y > tileCounty or self.x + x < 0 or self.y + y < 0:
            raise Exception("Cannot push off edge!")
        if self.gameMap[self.x + x][self.y + y]:
            self.gameMap[self.x + x][self.y + y].pushed(x, y, self, pusher)
        self.gameMap[self.x][self.y] = 0
        self.x += x
        self.y += y
        self.gameMap[self.x][self.y] = self