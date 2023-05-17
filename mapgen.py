import random
import uuid

from constants import *
from player import *
from blocks import *
from enemies import *

def generateMap(gameMap, players):
    for i in range(300):
        try:
            spot = [random.randint(0, tileCountx - 1), random.randint(0, tileCounty - 1)]
            if gameMap[spot[0]][spot[1]]:
                raise Exception("spot taken!")
            gameMap[spot[0]][spot[1]] = Block(uuid.uuid4(), spot[0], spot[1], gameMap)
        except Exception as error:
            continue

    for i in range(50):
        for j in range(50):
            try:
                spot = [random.randint(0, tileCountx - 1), random.randint(0, tileCounty - 1)]
                if gameMap[spot[0]][spot[1]]:
                    raise Exception("spot taken!")
                gameMap[spot[0]][spot[1]] = Enemy(uuid.uuid4(), spot[0], spot[1], gameMap)
                break
            except Exception as error:
                continue

    for id, player in players.items():
        maxTries = 5
        for i in range(maxTries):
            if i == maxTries - 1:
                raise Exception("No spots found for player!")
            try:
                spot = [random.randint(0, tileCountx - 1), random.randint(0, tileCounty - 1)]
                if gameMap[spot[0]][spot[1]]:
                    raise Exception("spot taken!")
                gameMap[spot[0]][spot[1]] = player
                player.x = spot[0]
                player.y = spot[1]
                break
            except Exception as error:
                continue