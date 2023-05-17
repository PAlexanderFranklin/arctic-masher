import pygame

from constants import *

class Block:
    def __init__(self, x, y, gameMap):
        self.x = x
        self.y = y
        self.gameMap = gameMap
        self.sprite = pygame.Rect((x*tile) + 2, (y*tile) + 2, tile - 2, tile - 2)

    def pushed(self, x, y, caller, pusher):
        if self.gameMap[self.x + x][self.y + y]:
            self.gameMap[self.x + x][self.y + y].pushed(x, y, self, pusher)
        self.gameMap[self.x][self.y] = 0
        self.x += x
        self.sprite.x = (self.x*tile)+2
        self.y += y
        self.sprite.y = (self.y*tile)+2
        self.gameMap[self.x][self.y] = self