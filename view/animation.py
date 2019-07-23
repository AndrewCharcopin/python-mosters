from setting import *
from pygame.locals import*

def StartScreen():
    # title_font = Font(25)
    LEFT_CLICK = (1,0,0)
    RIGHT_CLICK = (0,0,1)
    title_y = -40

    # music
    pygame.mixer.init()
    pygame.mixer.music.load('assets/sounds/title.mp3')
    pygame.mixer.music.play(-1)

    # display objects
    Title = Font(25).render("Python Monsters",True,WHITE)
    TitleRect = Title.get_rect()

    Coder = Font(15).render("by Python Monsters Association",True,GREY)
    CoderRect = Coder.get_rect()

    StartButton = Font(30).render("START",True,WHITE)
    StartRect = StartButton.get_rect()
    StartRect.center = (SCREEN_WIDTH/2,(SCREEN_HEIGHT/2) + CoderRect.height + StartRect.height)

    Move = True
    while Move:
        for event in pygame.event.get():
            if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
        screen.fill(BLACK)
        TitleRect.center = (SCREEN_WIDTH/2, title_y - TitleRect.height)
        screen.blit(Title,TitleRect)
        CoderRect.center = (SCREEN_WIDTH/2,title_y)
        screen.blit(Coder,CoderRect)
        pygame.display.flip()
        pygame.time.Clock().tick(30)
        title_y += 1
        if (title_y > (SCREEN_HEIGHT/2)):
            screen.blit(StartButton,StartRect)
            pygame.display.flip()
            Move = False

    PreviousClick = (0,0,0)
    Start = True
    while Start:
        for event in pygame.event.get():
                if event.type == QUIT:
                        pygame.quit()
                        sys.exit()

                elif event.type == KEYDOWN:
                        if (event.key == K_RETURN):
                                        Start = False

                elif event.type == MOUSEBUTTONDOWN:
                        PreviousClick = pygame.mouse.get_pressed()
                        
                                        
                elif event.type == MOUSEBUTTONUP:
                        if (PreviousClick == LEFT_CLICK):
                                if(pygame.mouse.get_pos()[0] > StartRect.x and\
                                    pygame.mouse.get_pos()[0] < StartRect.x + StartRect.width and\
                                    pygame.mouse.get_pos()[1] > StartRect.y and\
                                    pygame.mouse.get_pos()[1] < StartRect.y + StartRect.height):
                                        Start = False