import pygame
import uuid

from globals import *
from player import *
from blocks import *

class Enemy:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y
        

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
        pass