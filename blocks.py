import pygame
import uuid

from globals import *
from enemies import Enemy

class Block:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y
        
        self.sprite = pygame.Rect((x*tile) + 2, (y*tile) + 2, tile - 2, tile - 2)

    def pushed(self, x, y, caller, pusher):
        if self.x + x > tileCountx - 1 or self.y + y > tileCounty - 1 or self.x + x < 0 or self.y + y < 0:
            raise Exception("Cannot push off edge!")
        if gameMap[self.x + x][self.y + y]:
            gameMap[self.x + x][self.y + y].pushed(x, y, self, pusher)
        gameMap[self.x][self.y] = False
        self.x += x
        self.sprite.x = (self.x*tile)+2
        self.y += y
        self.sprite.y = (self.y*tile)+2
        gameMap[self.x][self.y] = self

    def pulled(self, x, y):
        for i in range(-1,2):
            for j in range(-1,2):
                if isinstance(gameMap[self.x + i][self.y + j], Enemy):
                    raise Exception("Cannot pull a block that is touching an enemy")
        gameMap[self.x][self.y] = False
        self.x += x
        self.sprite.x = (self.x*tile)+2
        self.y += y
        self.sprite.y = (self.y*tile)+2
        gameMap[self.x][self.y] = self