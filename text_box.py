import pygame,sys
import time

WHITE = (255, 255, 255)

pygame.init()
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 480
win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
box = (20, 20, SCREEN_WIDTH-40, 100)

class TextBox(object):
    def __init__(self, text, win):
        self.textArr = list(text)
        self.box = (20, 20, SCREEN_WIDTH-40, 100)
        self.textShown = False

    def makeBox(self):
        self.textShown = True
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_SPACE):
                    textShown = False
        while self.textShown:
            pygame.draw.rect(win, (255, 0, 0), (20, 20, SCREEN_WIDTH-40, 100), 2)
            pygame.display.update()

    def text_display(self):
        makeBox()
        font = pygame.font.Font('assets/dragon-warrior-1.ttf',15)
        i = 0
        while(i<20):
            textSurface = font.render(self.textArr[i], True, (255,255,255))
            win.blit(textSurface, ((width/20)*i), 20)
            pygame.display.update()
            i += 1

run = True
textShown = False
font = pygame.font.Font('assets/dragon-warrior-1.ttf',15)
while run:
    for event in pygame.event.get():  
        if event.type == pygame.QUIT: 
            run = False  
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        textShown = True
    
    while textShown:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
        if keys[pygame.K_SPACE]:
            textShown = True
        pygame.draw.rect(win, (255, 0, 0), (20, 20, SCREEN_WIDTH-40, 100), 2)
        pygame.display.update()

    win.fill((0,0,0))
    pygame.display.update()

pygame.quit()
