import pygame

from constants import *

class Block:
    def __init__(self, x, y, gameMap):
        self.x = x
        self.y = y
        self.gameMap = gameMap
        self.sprite = pygame.Rect((x*tile) + 2, (y*tile) + 2, tile - 2, tile - 2)

    def move(self, x, y, caller=False):
        try:
            if self.gameMap[self.x + x][self.y + y]:
                self.gameMap[self.x + x][self.y + y].move(x, y, caller=self)
            self.gameMap[self.x][self.y] = 0
            self.x += x
            self.sprite.x = (self.x*tile)+2
            self.y += y
            self.sprite.y = (self.y*tile)+2
            self.gameMap[self.x][self.y] = self
        except Exception as error:
            raise error