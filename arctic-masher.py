from profilehooks import profile

import pygame
import sys
import random
import uuid

from globals import *
import mapgen
from player import *
from blocks import *
from enemies import *

@profile
def main():

    pygame.init()
    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((screen_width,screen_height))
    pygame.display.set_caption('Arctic Masher')

    bottomBar = pygame.Rect(0, screen_height - bottomBarHeight, screen_width, bottomBarHeight)

    players["1"] = (Player(
        "1",
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
            (pygame.K_LSHIFT, "p"),
        ],
    ))
    players["2"] = (Player(
        "2",
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
            (pygame.K_KP_0, "p"),
        ],
    ))
    # players["3"] = (Player(
    #     "3",
    #     5,
    #     5,
    #     red,
    #     [
    #         (pygame.K_y, "n"),
    #         (pygame.K_u, "ne"),
    #         (pygame.K_j, "e"),
    #         (pygame.K_m, "se"),
    #         (pygame.K_n, "s"),
    #         (pygame.K_b, "sw"),
    #         (pygame.K_g, "w"),
    #         (pygame.K_t, "nw"),
    #         (pygame.K_h, "p"),
    #     ],
    # ))

    mapgen.generateMap()

    sprite_sheet_image = pygame.image.load('assets/penguin.png').convert_alpha()

    def get_image(sheet, x, y, width, height, scale, colour):
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(sheet, (0, 0), (x, y, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey(colour)

        return image
    frame_0 = get_image(sprite_sheet_image, 0, 0, 32, 32, (tile-2)/32, black)
    frame_1 = get_image(sprite_sheet_image, 0, 32, 32, 32, (tile-2)/32, black)
    frame_4 = get_image(sprite_sheet_image, 32, 0, 32, 32, (tile-2)/32, black)

    game_font = pygame.font.Font("freesansbold.ttf",32)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()

        for id, player in players.items():
            player.useKeys(keys)
        
        for id, enemy in enemies.items():
            enemy.runAI()

        # Rendering
        screen.fill(bg_color)
        pygame.draw.rect(screen, bar_color, bottomBar)
        for column in gameMap:
            for spot in column:
                if not spot:
                    continue
                elif isinstance(spot, Block):
                    pygame.draw.rect(screen, spot.color, spot.sprite)
                elif isinstance(spot, Enemy):
                    screen.blit(spot.sprite, ((tile*spot.renderPos[0])+2, (tile*spot.renderPos[1])+2))
                elif isinstance(spot, Player):
                    screen.blit(frame_0, ((tile*spot.renderPos[0])+2, (tile*spot.renderPos[1])+2))
                    scoreSurface = game_font.render(f'player {spot.id} kills: {spot.kills} lives: {spot.lives}', False, black)
                    screen.blit(scoreSurface, (500*int(spot.id) - 400, screen_height - bottomBarHeight + 20))
                try:
                    spot.renderPos = ((spot.x - spot.renderPos[0])/3 + spot.renderPos[0], (spot.y - spot.renderPos[1])/3 + spot.renderPos[1])
                except:
                    pass
        pygame.display.flip()
        clock.tick(60)

if __name__ == '__main__':
    main()
