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
pygame.display.set_caption('Arctic Masher')

class Player:
    def __init__(self, x, y, color, keys):
        self.x = x
        self.y = y
        self.color = color
        self.keys = keys
        self.commands = {
            "n": lambda: self.move(0,-1),
            "ne": lambda: self.move(1,-1),
            "e": lambda: self.move(1,0),
            "se": lambda: self.move(1,1),
            "s": lambda: self.move(0,1),
            "sw": lambda: self.move(-1,1),
            "w": lambda: self.move(-1,0),
            "nw": lambda: self.move(-1,-1),
        }
        self.sprite = pygame.Rect((tile*x)+2,(tile*y)+2,tile-2,tile-2)

    def move(self, x, y):
        self.x += x
        self.y += y

players = []
players.append(Player(25, 20, red, {
    pygame.K_w: "n",
    pygame.K_e: "ne",
    pygame.K_d: "e",
    pygame.K_c: "se",
    pygame.K_x: "s",
    pygame.K_z: "sw",
    pygame.K_a: "w",
    pygame.K_q: "nw"
}))
players.append(Player(25, 20, green, {
    pygame.K_KP_8: "n",
    pygame.K_KP_9: "ne",
    pygame.K_KP_6: "e",
    pygame.K_KP_3: "se",
    pygame.K_KP_2: "s",
    pygame.K_KP_1: "sw",
    pygame.K_KP_4: "w",
    pygame.K_KP_7: "nw"
}))

game_font = pygame.font.Font("freesansbold.ttf",32)

pygame.key.set_repeat(300, 40)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            for player in players:
                try:
                    player.commands[player.keys[event.key]]()
                except:
                    pass

    keys = pygame.key.get_pressed()
    # Rendering
    screen.fill(bg_color)
    for player in players:
        player.sprite.x = (tile*player.x)+2
        player.sprite.y = (tile*player.y)+2
        pygame.draw.rect(screen, player.color, player.sprite)

    pygame.display.flip()
    clock.tick(60)