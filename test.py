import pygame
import time

textShown = False
WHITE = (255, 255, 255)

# def makeText(win, col = WHITE):
#     textShown = True

#     #if key pressed and text arr empty
#     #textShow = False

pygame.init()
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 480
win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
box = (20, 20, SCREEN_WIDTH-40, 100)

class TextBox(object):
    def __init__(self, text, win):
        self.textArr = list(text)
        self.box = (20, 20, SCREEN_WIDTH-40, 100)

    def makeBox(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_SPACE):
                    textShown = False

        pygame.draw.rect(win, (255, 0, 0), (20, 20, SCREEN_WIDTH-40, 100), 2)
        pygame.display.update()

    # def text_objects(textArr, font):
    #     # render(text, antialias, color, background=None) -> Surface
    #     # crete current text object
    #     textSurface = font.render(textArr[self.counter], True, (255,255,255)
    #     self.counter += 1
    #     return textSurface

    def text_display(self):
        makeBox()
        font = pygame.font.Font('assets/dragon-warrior-1.ttf',15)
        i = 0
        while(i<20):
            textSurface = font.render(self.textArr[i], True, (255,255,255)
            win.blit(textSurface, ((width/20)*i), 20)
            pygame.display.update()
            i += 1

  
textBox = TextBox("This is a sample text.")
print(textBox.dialog)

run = True
while run:
    for event in pygame.event.get():  
        if event.type == pygame.QUIT: 
            run = False  
    
    # Space TextShown
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        textShown = True
        textBox = TextBox("This is a sample text.")
        textBox.makeBox()
        # makeText(win)
    
    while textShown:
        textBox.text_display()

    win.fill((0,0,0))
    pygame.display.update()
    # print("updated")
    # pygame.display.update()

pygame.quit()
