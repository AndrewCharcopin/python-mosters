import pygame, sys
import random
import time
from title import StartScreen, PlayerInput

BLACK = (0,0,0)
GREY = (180,180,180)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

pygame.init()

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 480
win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Slime Game")

walk = [pygame.image.load('assets/slime/slime-move-0.png'),pygame.image.load('assets/slime/slime-move-1.png'),pygame.image.load('assets/slime/slime-move-2.png'),pygame.image.load('assets/slime/slime-move-3.png')]
standing = [pygame.image.load('assets/slime/slime-idle-0.png'),pygame.image.load('assets/slime/slime-idle-1.png'),pygame.image.load('assets/slime/slime-idle-2.png'),pygame.image.load('assets/slime/slime-idle-3.png')]
bg = pygame.image.load('assets/bg.jpg')

clock = pygame.time.Clock()

class Player(object):
    def __init__(self, x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 15
        self.right = True
        self.left = False
        self.standing = False
        self.walkCount = 0
        self.money = 100

    def draw(self, win):
        # 3frame per image
        if self.walkCount + 1 >= 12:
            self.walkCount = 0
        if not(self.standing):
            if self.left:
                win.blit(walk[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(pygame.transform.flip(walk[self.walkCount//3], True, False), (self.x, self.y))
                self.walkCount += 1
        # if idle images facing front exist
        # else:
        #     win.blit(pygame.transform.flip(standing[self.walkCount//3], True, False), (self.x, self.y))
        #     self.walkCount += 1

        # pygame.draw.rect(win, (255,0,0), (self.x, self.y, self.width, self.height))

class Enemy(object):
    def __init__(self, x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x + 20, self.y, 28, 60)

    def draw(self, win):
        pygame.draw.rect(win, (255,255,0), (self.x, self.y, self.width, self.height))


textDisplayed = False
currentText = ""

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

## not used for now
class Room(object):
    # wall_list = None
    enemy_sprites = None
    def __init__(self):
        # self.wall_list = pygame.sprite.Group()
        self.enemy_sprites = pygame.sprite.Group()

##TODO Change room if player enter a door
def createRoom(stage):
    def __init__(self):
        super().__init__()
    room = Room()


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



def main():
    player = Player(200, 410, 64, 64)
    enemy = Enemy(400, 410, 40, 40)

    StartScreen()
    player.name = PlayerInput()

    run = True
    while run:
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
                message_display("catch me if you can!", enemy.x, enemy.y-enemy.height)
                enemy.x = random.randint(0, SCREEN_WIDTH)
                player.money += 100
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

if __name__ == "__main__":
    main()