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

def displayText(text):
    font = pygame.font.Font('assets/dragon-warrior-1.ttf',15)
    textSurface = font.render(text, True, (255,255,255), (0,0,0))
    win.blit(textSurface, (30, 30))
    pygame.display.update()

# ---- draw!
def redrawGameWindow(player, enemy, text, textShown):
    font = pygame.font.Font('assets/dragon-warrior-1.ttf',15)
    ## display name and gold
    nameText = font.render(str(player.name), 1, (0,0,0))
    win.blit(nameText, (380, 5))
    goldText = font.render('Gold: ' + str(player.money), 1, (0,0,0))
    win.blit(goldText, (350, 20))
    
    enemy.draw(win)
    player.draw(win)

    while textShown:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
        # if down is pressed, textshown = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:
            textShown = False
            text = ''
        pygame.draw.rect(win, (255, 0, 0), (20, 20, SCREEN_WIDTH-40, 100), 2)
        #display text
        displayText(text)

    pygame.display.update()

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

# 1 make rec
def makeText(text, col = WHITE):
    box = (20, 20, SCREEN_WIDTH-40, 60)
    pygame.draw.rect(win, WHITE, box, 2)
    pygame.display.update()
    textFont = pygame.font.Font('assets/dragon-warrior-1.ttf',15)
    
def main():
    StartScreen()
    player = Player(200, 410, PlayerInput())
    enemy = Enemy(400, 410, 40, 40)
    textShown = False
    text = ''

    run = True
    while run:
        keys = pygame.key.get_pressed()
        win.blit(bg, (0,0))
        clock.tick(12)
        pygame.time.delay(10)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # player-enemy interaction
        if abs(player.x - enemy.x) < 20:
            # lift enemy by 20
            enemy.y = 390
            if keys[pygame.K_SPACE]:
                #display text
                textShown = True
                text = enemy.text
        
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

        redrawGameWindow(player,enemy, text, textShown)
        
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
