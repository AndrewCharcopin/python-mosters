import pygame,sys
import time

WHITE = (255, 255, 255)
pygame.init()
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 480
win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
box = (20, 20, SCREEN_WIDTH-40, 100)

run = True
textShown = False
font = pygame.font.Font('assets/dragon-warrior-1.ttf',15)

def displayText(text):
    textSurface = font.render(text, True, (255,255,255), (0,0,0))
    win.blit(textSurface, (30, 30))
    pygame.display.update()

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
        # if down is pressed, textshown = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:
            textShown = False
        pygame.draw.rect(win, (255, 0, 0), (20, 20, SCREEN_WIDTH-40, 100), 2)

        #display text
        text = "Hello"
        displayText(text)

    win.fill((0,0,0))
    pygame.display.update()

pygame.quit()
