import pygame, sys, os
import random, time
#TODO Import ONLY modules
from title import StartScreen, PlayerInput
from characters import Player, Enemy
from setting import *

BLACK = (0,0,0)
GREY = (180,180,180)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 480
stage = 0

def main():
    # StartScreen()
    player = Player(PlayerInput(), 100)
    slime = {"slime": Enemy("slime", 30)}
    vampire = Enemy("vampire",60)
    wolf = Enemy("wolf", 110)
    enemies = {"slime": Enemy("slime", 30), "vampire": Enemy("vampire", 60), "wolf": Enemy("wolf", 110)}
    global stage
    stage = 0
    textShown = False
    text = ''
    run = True
    while run:
        font = pygame.font.Font('assets/dragon-warrior-1.ttf',15)
        keys = pygame.key.get_pressed()
        clock.tick(12)
        pygame.time.delay(10)
        # change background depending on stage
        if len(bg_images) > stage:
            bg = pygame.transform.scale(load_png(bg_images[stage]) ,(SCREEN_WIDTH, SCREEN_HEIGHT))
        else:
            bg = pygame.transform.scale(load_png(bg_images[len(bg_images)-1]), (SCREEN_WIDTH, SCREEN_HEIGHT))
        win.blit(bg, (0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        # player-enemy interaction
        enemy = get_enemy(enemies)
        if abs(player.x - enemy.x) < 30:
            # lift enemy by 20
            enemy.y = 330
            strengthEnemyText = font.render('HP: ' + str(enemy.strength), 1, (0,0,0))
            win.blit(strengthEnemyText, (0, 50))
            if keys[pygame.K_RETURN]:
                # display text, then fight
                enemy.textShown = True
                text = enemy.text
                fight_result = player.fight(enemy)
                if fight_result:
                    enemy.strength = 100
                    stage += 1
                    enemy = get_enemy(enemies)
                    enemy.textShown = False

        else:
            textDisplayed = False
            enemy.y = 340


        if keys[pygame.K_LEFT] and player.x > player.vel:
            player.x -= player.vel
            player.standing = False
            player.right = False
            player.left = True
        elif keys[pygame.K_RIGHT] and player.x < SCREEN_WIDTH - player.vel:
            player.x += player.vel
            player.standing = False
            player.right = True
            player.left = False
        #Only if idle images facing front exist
        # else:
        #     player.standing = True
        #     player.right = False
        #     player.left = False
            # TODO reset walkcount when key is released
            # player.walkCount = 0

        # ---- Game logic
        # if player enter a door, restart from 200
        if player.x > SCREEN_WIDTH:
            player.x = 200

        redrawGameWindow(player,enemy)
        
    pygame.quit()
    sys.exit()

win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.init()

pygame.display.set_caption("Slime Game")
bg_images = ["bg.jpg", "back_field.jpeg", "back_castle.jpeg", "castle_back.png", "field_back.png"]



# bg = pygame.image.load('assets/images/bg.jpg')
clock = pygame.time.Clock()

if __name__ == "__main__":
    main()
