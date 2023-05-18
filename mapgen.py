import random
import uuid

from globals import *
from player import *
from blocks import *
from enemies import *

def generateMap():
    gameMap.clear()
    for i in range(tileCountx):
        column = []
        for j in range(tileCounty):
            column.append(False)
        gameMap.append(column)
    for i in range(300):
        try:
            spot = [random.randint(0, tileCountx - 1), random.randint(0, tileCounty - 1)]
            if gameMap[spot[0]][spot[1]]:
                raise Exception("spot taken!")
            gameMap[spot[0]][spot[1]] = Block(uuid.uuid4(), spot[0], spot[1])
        except Exception as error:
            continue

    for i in range(50):
        for j in range(50):
            try:
                spot = [random.randint(0, tileCountx - 1), random.randint(0, tileCounty - 1)]
                if gameMap[spot[0]][spot[1]]:
                    raise Exception("spot taken!")
                newEnemy = Enemy(uuid.uuid4(), spot[0], spot[1])
                gameMap[spot[0]][spot[1]] = newEnemy
                enemies[newEnemy.id] = newEnemy
                break
            except Exception as error:
                continue

    for i in range(3):
        for j in range(50):
            try:
                spot = [random.randint(0, tileCountx - 1), random.randint(0, tileCounty - 1)]
                if gameMap[spot[0]][spot[1]]:
                    raise Exception("spot taken!")
                newEnemy = Smart(uuid.uuid4(), spot[0], spot[1])
                gameMap[spot[0]][spot[1]] = newEnemy
                enemies[newEnemy.id] = newEnemy
                break
            except Exception as error:
                continue

    for id, player in players.items():
        maxTries = 5
        for i in range(maxTries + 1):
            if i == maxTries:
                raise Exception("No spots found for player!")
            try:
                spot = [random.randint(0, tileCountx - 1), random.randint(0, tileCounty - 1)]
                if gameMap[spot[0]][spot[1]]:
                    raise Exception("spot taken!")
                gameMap[spot[0]][spot[1]] = player
                player.x = spot[0]
                player.y = spot[1]
                player.buildOwnPathMap()
                break
            except Exception as error:
                continue