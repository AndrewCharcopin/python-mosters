import pygame,sys,os
from pygame.locals import*
import time

def playSong(songs, current_song):
    pygame.mixer.music.stop()
    pygame.mixer.init()
    pygame.mixer.music.set_volume(0.5)
    if pygame.mixer.music.get_busy() == False:
        fullname = os.path.join('assets/sounds/', songs[current_song])
        print(songs[current_song])
        pygame.mixer.music.load(fullname)
        pygame.mixer.music.play()

def updateSong(songs, current_song):
    pygame.mixer.music.stop()
    if pygame.mixer.music.get_busy() == False:
        fullname = os.path.join('assets/sounds/', songs[current_song])
        pygame.mixer.music.load(fullname)
        pygame.mixer.music.play()
        print("Update song to ", songs[current_song])

def StartScreen():
    LEFT_CLICK = (1,0,0)
    RIGHT_CLICK = (0,0,1)

    Display.fill(BLACK)
    Title = Font.render("Python Quest",True,WHITE)
    TitleRect = Title.get_rect()
    TitleRect.center = (SCREEN_WIDTH/2,SCREEN_HEIGHT/2 - TitleRect.height)
    Display.blit(Title,TitleRect)

    Coder = Font.render("by MASAKI",True,GREY)
    CoderRect = Coder.get_rect()
    CoderRect.center = (SCREEN_WIDTH/2,(SCREEN_HEIGHT/2))
    Display.blit(Coder,CoderRect)

    StartButton = Font.render("Start",True,WHITE)
    StartRect = StartButton.get_rect()
    StartRect.center = (SCREEN_WIDTH/2,(SCREEN_HEIGHT/2) + CoderRect.height + StartRect.height)
    Display.blit(StartButton,StartRect)

    Start = True

    PreviousClick = (0,0,0)

    pygame.display.update()
    pygame.time.Clock().tick(30) #30fps

    while Start:
        for event in pygame.event.get():
                if event.type == QUIT:
                        pygame.quit()
                        sys.exit()

                elif event.type == KEYDOWN:
                        if (event.key == K_RETURN):
                                        Start = False

                elif event.type == MOUSEBUTTONDOWN:
                        #left click
                        PreviousClick = pygame.mouse.get_pressed()
                        #if (pygame.mouse.get_pressed() == LEFT_CLICK):
                                #if(pygame.mouse.get_pos()[0] > StartRect.x and\
                                    #pygame.mouse.get_pos()[0] < StartRect.x + StartRect.width and\
                                    #pygame.mouse.get_pos()[1] > StartRect.y and\
                                    #pygame.mouse.get_pos()[1] < StartRect.y + StartRect.height):
                                        #Start = False
                                        
                elif event.type == MOUSEBUTTONUP:
                        if (PreviousClick == LEFT_CLICK):
                                if(pygame.mouse.get_pos()[0] > StartRect.x and\
                                    pygame.mouse.get_pos()[0] < StartRect.x + StartRect.width and\
                                    pygame.mouse.get_pos()[1] > StartRect.y and\
                                    pygame.mouse.get_pos()[1] < StartRect.y + StartRect.height):
                                        Start = False

def PlayerInput(songs, current_song):
    Display.fill(BLACK)
    Title = Font.render("Python Quest",True,WHITE)
    TitleRect = Title.get_rect()
    TitleRect.center = (SCREEN_WIDTH/2,SCREEN_HEIGHT/2 - TitleRect.height)
    Display.blit(Title,TitleRect)

    InputPrompt = Font.render("Please tell me your name",True,GREY)
    InputPromptRect = InputPrompt.get_rect()
    InputPromptRect.center = (SCREEN_WIDTH/2,(SCREEN_HEIGHT/2))
    Display.blit(InputPrompt,InputPromptRect)
    
    pygame.display.update()

    input_box = pygame.Rect(SCREEN_WIDTH/2 - 90, (SCREEN_HEIGHT/2) + InputPromptRect.height, 140, 32)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    done = False
    playerName = ""

    while not done:
        for event in pygame.event.get():
            # if event.type == pygame.QUIT:
            #     done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                else:
                    active = False
                # Change the current color of the input box.
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        current_song += 1
                        updateSong(songs, current_song)
                        return text
                        break
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        # Render the current text.
        txt_surface = Font.render(text, True, color)
        # Resize the box if the text is too long.
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        # Blit the text.
        Display.blit(txt_surface, (input_box.x+5, input_box.y+5))
        # Blit the input_box rect.
        pygame.draw.rect(Display, color, input_box, 2)

        pygame.display.flip()
        clock.tick(30)
    

BLACK = (0,0,0)
GREY = (180,180,180)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

pygame.init()
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 480
Display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# Font = pygame.font.Font('freesansbold.ttf',15)
Font = pygame.font.Font('assets/dragon-warrior-1.ttf',15)
pygame.display.set_caption("Python Quest")

# music = pygame.mixer.music.load('assets/music.mp3')
# pygame.mixer.music.play(-1)

clock = pygame.time.Clock()

def main():
    StartScreen()
    PlayerInput()

    pygame.display.update()
    #quit game
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()

