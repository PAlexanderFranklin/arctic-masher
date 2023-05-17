import pygame
import sys
import random

from player import *

pygame.init()
clock = pygame.time.Clock()

bg_color = pygame.Color('cornsilk4')
red = pygame.Color('brown4') 
blue = pygame.Color('cadetblue3')
green = pygame.Color('green3')
black = pygame.Color("black")

tile = 34
tileCountx = 50
tileCounty = 30

screen_width = tile * tileCountx
screen_height = tile * tileCounty

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Arctic Masher')

gameMap = []

for i in range(tileCountx):
    column = []
    for j in range(tileCounty):
        column.append(False)
    gameMap.append(column)

players = []
players.append(Player(
    5,
    5,
    red,
    [
        (pygame.K_w, "n"),
        (pygame.K_e, "ne"),
        (pygame.K_d, "e"),
        (pygame.K_c, "se"),
        (pygame.K_x, "s"),
        (pygame.K_z, "sw"),
        (pygame.K_a, "w"),
        (pygame.K_q, "nw"),
    ],
    gameMap,
))
players.append(Player(
    3,
    3,
    green,
    [
        (pygame.K_KP_8, "n"),
        (pygame.K_KP_9, "ne"),
        (pygame.K_KP_6, "e"),
        (pygame.K_KP_3, "se"),
        (pygame.K_KP_2, "s"),
        (pygame.K_KP_1, "sw"),
        (pygame.K_KP_4, "w"),
        (pygame.K_KP_7, "nw"),
    ],
    gameMap,
))
players.append(Player(
    5,
    5,
    red,
    [
        (pygame.K_y, "n"),
        (pygame.K_u, "ne"),
        (pygame.K_j, "e"),
        (pygame.K_m, "se"),
        (pygame.K_n, "s"),
        (pygame.K_b, "sw"),
        (pygame.K_g, "w"),
        (pygame.K_t, "nw"),
    ],
    gameMap,
))

for player in players:
    for i in range(50):
        try:
            spot = [random.randint(0, tileCountx - 1), random.randint(0, tileCounty - 1)]
            if gameMap[spot[0]][spot[1]]:
                raise Exception("spot taken!")
            gameMap[spot[0]][spot[1]] = player
            player.x = spot[0]
            player.y = spot[1]
            break
        except Exception as error:
            print(error)
            if i > 45:
                pygame.quit()
                sys.exit()

sprite_sheet_image = pygame.image.load('assets/penguin.png').convert_alpha()

def get_image(sheet, width, height, scale, colour):
    image = pygame.Surface((width, height)).convert_alpha()
    image.blit(sheet, (0, 0), (0, 0, width, height))
    image = pygame.transform.scale(image, (width * scale, height * scale))
    image.set_colorkey(colour)

    return image
frame_0 = get_image(sprite_sheet_image, 32, 32, (tile-2)/32, black)

game_font = pygame.font.Font("freesansbold.ttf",32)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    for player in players:
        player.useKeys(keys)

    # Rendering
    screen.fill(bg_color)
    for player in players:
        screen.blit(frame_0, ((tile*player.x)+2, (tile*player.y)+2))

    pygame.display.flip()
    clock.tick(60)