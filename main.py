import pygame, sys, os
import random, time
#TODO Import ONLY modules
from title import StartScreen, PlayerInput
from characters import Player, Enemy

BLACK = (0,0,0)
GREY = (180,180,180)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 480
#count the rap of stage
stage_num = 0

def load_png(name):
    """ Load image and return image object"""
    fullname = os.path.join('assets/images', name)
    try:
        image = pygame.image.load(fullname)
        if image.get_alpha() is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
    except pygame.error as message:

        raise SystemExit
    return image

# ---- draw!
def redrawGameWindow(player, enemy):
    font = pygame.font.Font('assets/dragon-warrior-1.ttf',15)
    ## display name and gold
    nameText = font.render(str(player.name), 1, (0,0,0))
    win.blit(nameText, (380, 5))
    goldText = font.render('Gold: ' + str(player.money), 1, (0,0,0))
    win.blit(goldText, (350, 20))
    
    enemy.draw(win)
    player.draw(win)
    
    pygame.display.update()


#win.blit(object, (x,y))
def text_objects(text, font):
    # render(text, antialias, color, background=None) -> Surface
    textSurface = font.render(text, True, (255,255,255), (0,0,0))
    return textSurface, textSurface.get_rect()

def message_display(text, x = SCREEN_WIDTH//2, y = SCREEN_HEIGHT-100):
    textFont = pygame.font.Font('assets/dragon-warrior-1.ttf',15)
    TextSurf, TextRect = text_objects(text, textFont)
    TextRect.center = (x,y)
    win.blit(TextSurf, TextRect)
    pygame.display.update()

def get_enemy():
  enemies = {}
  enemies["slime"] = Enemy(400, 410, 40, 40, "slime", 30)
  enemies["vampire"] = Enemy(400, 410, 40, 40, "vampire", 60)
  enemies["wolf"] = Enemy(400, 410, 40, 40, "wolf", 110)

  if stage_num < 2:
    return enemies["slime"]
  elif stage_num >= 2 and stage_num < 5:
    return enemies["vampire"]
  else:
    return enemies["wolf"]

def main():
    StartScreen()
    player = Player(200, 410, PlayerInput())

    run = True
    while run:
        win.blit(bg, (0,0))
        clock.tick(12)
        pygame.time.delay(10)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # player-enemy interaction
        enemy = get_enemy()
        if abs(player.x - enemy.x) < 20:
            # lift enemy by 20
            enemy.y = 390
            if keys[pygame.K_SPACE]:
                #display text
                win_or_lose = player.fight(enemy)
                print(win_or_lose)
                print(enemy.name)
                if win_or_lose:
                  message_display("win!!!!")
                else:
                  message_display("lose!!!")  
                global stage_num
                stage_num += 1
        else:
            textDisplayed = False
            enemy.y = 410
        
        # ---- key control
        keys = pygame.key.get_pressed()

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
bg = load_png("bg.jpg")
# bg = pygame.image.load('assets/images/bg.jpg')
clock = pygame.time.Clock()

if __name__ == "__main__":
    main()
