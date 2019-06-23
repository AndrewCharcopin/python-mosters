import pygame, sys, os

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 480

win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
stage = 0


def displayText(text, x=30, y=70):
    font = pygame.font.Font('assets/dragon-warrior-1.ttf',15)
    textSurface = font.render(text, True, (255,255,255), (0,0,0))
    win.blit(textSurface, (x, y))
    pygame.display.update()

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

def redrawGameWindow(player, enemy):
    font = pygame.font.Font('assets/dragon-warrior-1.ttf',15)
    ## display name and gold
    nameText = font.render(str(player.name), 1, (0,0,0))
    win.blit(nameText, (380, 5))
    goldText = font.render('Gold: ' + str(player.money), 1, (0,0,0))
    win.blit(goldText, (350, 20))
    stageText = font.render('Stage: ' + str(stage), 1, (0,0,0))
    win.blit(stageText, (350, 35))
    strengthPlayerText = font.render('HP: ' + str(player.strength), 1, (0,0,0))
    win.blit(strengthPlayerText, (350, 50))
    strengthEnemyText = font.render('HP: ' + str(enemy.strength), 1, (0,0,0))
    enemy.draw(win)
    player.draw(win)
    screen = pygame.display.get_surface()
    pygame.display.update()
    while enemy.textShown:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
        # if down is pressed, textshown = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:
            enemy.textShown = False
        elif keys[pygame.K_RETURN]:
            print(enemy.strength)
            enemy.strength -= 1
            win.blit(strengthEnemyText, (0, 50))
            enemy.textShown = False
            if enemy.strength == 0:
                enemy.textShown = False
        pygame.draw.rect(win, (255, 0, 0), (20, 60, SCREEN_WIDTH-40, 100), 2)
        #display text
        displayText(enemy.text)

def message_display(text, x = SCREEN_WIDTH//2, y = SCREEN_HEIGHT-100):
    textFont = pygame.font.Font('assets/dragon-warrior-1.ttf',15)
    TextSurf, TextRect = text_objects(text, textFont)
    TextRect.center = (x,y)
    win.blit(TextSurf, TextRect)
    pygame.display.update()

def get_enemy(enemies):
    if stage < 2:
        return enemies["slime"]
    elif stage >= 2 and stage < 5:
        return enemies["vampire"]
    else:
        return enemies["wolf"]