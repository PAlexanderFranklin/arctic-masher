from globals import *

def checkOOBounds(pos):
    return pos[0] > tileCountx - 1 or pos[1] > tileCounty - 1 or pos[0] < 0 or pos[1] < 0