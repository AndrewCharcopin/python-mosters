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
stage = 0
#count the wrap of stage
# stage = 0

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

def displayText(text, x=30, y=70):
    font = pygame.font.Font('assets/dragon-warrior-1.ttf',15)
    textSurface = font.render(text, True, (255,255,255), (0,0,0))
    win.blit(textSurface, (x, y))
    pygame.display.update()

# ---- draw!
def redrawGameWindow(player, enemy):
    font = pygame.font.Font('assets/dragon-warrior-1.ttf',15)
    ## display name and gold
    nameText = font.render(str(player.name), 1, (0,0,0))
    win.blit(nameText, (380, 5))
    goldText = font.render('Gold: ' + str(player.money), 1, (0,0,0))
    win.blit(goldText, (350, 20))
    stageText = font.render('Stage: ' + str(stage), 1, (0,0,0))
    win.blit(stageText, (350, 35))
    
    enemy.draw(win)
    player.draw(win)

    while enemy.textShown:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
        # if down is pressed, textshown = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:
            enemy.textShown = False
        pygame.draw.rect(win, (255, 0, 0), (20, 60, SCREEN_WIDTH-40, 100), 2)
        #display text
        displayText(enemy.text)

    pygame.display.update()

def message_display(text, x = SCREEN_WIDTH//2, y = SCREEN_HEIGHT-100):
    textFont = pygame.font.Font('assets/dragon-warrior-1.ttf',15)
    TextSurf, TextRect = text_objects(text, textFont)
    TextRect.center = (x,y)
    win.blit(TextSurf, TextRect)
    pygame.display.update()

#this is for getting an enemy at random
def cast_dice():
  return random.randint(1,6)

def get_enemy(enemies):
  if stage < 2:
    return enemies["slime"]
  elif stage >= 2 and stage < 5:
    if dice % 2 == 0:
      return enemies["slime"]
    else:
      return enemies["vampire"]
  else:
    if dice == 1 or dice == 2:
      return enemies["slime"]
    elif dice == 3 or dice == 4:
      return enemies["vampire"]
    else:
      return enemies["wolf"]
    
def main():
    # StartScreen()
    player = Player(PlayerInput(), 100)
    enemies = {"slime": Enemy("slime", 30), "vampire": Enemy("vampire", 60), "wolf": Enemy("wolf", 110)}
    global stage
    stage = 0

    textShown = False
    text = ''
    run = True
    
    while run:
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
            if keys[pygame.K_SPACE]:
              #display text, then fight
              enemy.textShown = True
              text = enemy.text
              fight_result = player.fight(enemy)
              print(fight_result)
              print(enemy.name)
              if fight_result:
                stage += 1
                player.x = player.startX
                displayText("win!!", 80, 100)
                global dice
                dice = cast_dice()
              else:
                displayText("lost!!", 80, 100)
                  
        else:
            textDisplayed = False
            enemy.y = 340
        
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
bg_images = ["bg.jpg", "back_field.jpeg", "back_castle.jpeg", "castle_back.png", "field_back.png"]



# bg = pygame.image.load('assets/images/bg.jpg')
clock = pygame.time.Clock()

if __name__ == "__main__":
    main()
