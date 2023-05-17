import pygame
import sys
import random

pygame.init()
clock = pygame.time.Clock()

bg_color = pygame.Color('cornsilk4')
red = pygame.Color('brown4') 
blue = pygame.Color('cadetblue3')
green = pygame.Color('green3')

tile = 34

screen_width = tile * 50
screen_height = tile * 40

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('monster-masher-clone')

class Player:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.sprite = pygame.Rect((tile*x)+2,(tile*y)+2,tile-2,tile-2)

players = []
players.append(Player(25, 20, red))
players.append(Player(20, 15, blue))
players.append(Player(30, 15, green))

game_font = pygame.font.Font("freesansbold.ttf",32)

pygame.key.set_repeat(300, 40)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            for player in players:
                if event.key == pygame.K_s:
                    player.y += 1
                if event.key == pygame.K_w:
                    player.y -= 1
                if event.key == pygame.K_a:
                    player.x -= 1
                if event.key == pygame.K_d:
                    player.x += 1

    # Rendering
    screen.fill(bg_color)
    for player in players:
        player.sprite.x = (tile*player.x)+2
        player.sprite.y = (tile*player.y)+2
        pygame.draw.rect(screen, player.color, player.sprite)

    pygame.display.flip()
    clock.tick(60)