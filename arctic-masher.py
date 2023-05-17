import pygame
import sys
import random

pygame.init()
clock = pygame.time.Clock()

bg_color = pygame.Color('cornsilk4')
red = pygame.Color('brown4') 
blue = pygame.Color('cadetblue3')
green = pygame.Color('green3')
black = pygame.Color("black")

tile = 34

screen_width = tile * 10
screen_height = tile * 10

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Arctic Masher')

class Player:
    def __init__(self, x, y, color, keys):
        self.x = x
        self.y = y
        self.color = color
        commands = {
            "n": lambda: self.move(0,-1),
            "ne": lambda: self.move(1,-1),
            "e": lambda: self.move(1,0),
            "se": lambda: self.move(1,1),
            "s": lambda: self.move(0,1),
            "sw": lambda: self.move(-1,1),
            "w": lambda: self.move(-1,0),
            "nw": lambda: self.move(-1,-1),
        }
        self.commands = []
        for key in keys:
            self.commands.append((key[0], commands[key[1]]))
        self.sprite = pygame.Rect((tile*x)+2,(tile*y)+2,tile-2,tile-2)

    def useKeys(self, keys):
        try:
            for command in self.commands:
                if keys[command[0]]:
                    command[1]()
        except:
            pass

    def move(self, x, y):
        self.x += x
        self.y += y

players = []
players.append(Player(5, 5, red, [
    (pygame.K_w, "n"),
    (pygame.K_e, "ne"),
    (pygame.K_d, "e"),
    (pygame.K_c, "se"),
    (pygame.K_x, "s"),
    (pygame.K_z, "sw"),
    (pygame.K_a, "w"),
    (pygame.K_q, "nw"),
]))
players.append(Player(3, 3, green, [
    (pygame.K_KP_8, "n"),
    (pygame.K_KP_9, "ne"),
    (pygame.K_KP_6, "e"),
    (pygame.K_KP_3, "se"),
    (pygame.K_KP_2, "s"),
    (pygame.K_KP_1, "sw"),
    (pygame.K_KP_4, "w"),
    (pygame.K_KP_7, "nw"),
]))

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