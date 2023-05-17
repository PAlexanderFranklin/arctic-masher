import pygame

from constants import *

class Enemy:
    def __init__(self, x, y, gameMap):
        self.x = x
        self.y = y
        self.gameMap = gameMap

    def pushed(self, x, y, caller, pusher):
        if self.gameMap[self.x + x][self.y + y]:
            self.gameMap[self.x + x][self.y + y].pushed(x, y, self, pusher)
        self.gameMap[self.x][self.y] = 0
        self.x += x
        self.y += y
        self.gameMap[self.x][self.y] = self