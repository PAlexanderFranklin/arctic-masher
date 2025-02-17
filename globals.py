import pygame

bg_color = pygame.Color('lightsalmon3')
bar_color = pygame.Color('white')
red = pygame.Color('brown4') 
blue = pygame.Color('cadetblue3')
green = pygame.Color('green3')
grey = pygame.Color("gray26")
black = pygame.Color("black")
white = pygame.Color("white")
purple = pygame.Color("purple")

tile = 34
tileCountx = 50
tileCounty = 25

bottomBarHeight = 100

screen_width = tile * tileCountx
screen_height = tile * tileCounty + bottomBarHeight

# Game Entity Arrays
gameMap = []
players = {}
enemies = {}