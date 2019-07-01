import pygame
from setting import *

def Title():
  pygame.init()

  #setting variables
  name = ''
  color_inactive = pygame.Color('lightskyblue3')
  color_active = pygame.Color('dodgerblue2')
  color = color_inactive
  active = False
  run = True

  while run:
    #initialize screen
    screen.fill((30, 30, 30))

    #draw title
    title_text = Font(14).render("What's your name?", True, GREY)
    title_size = title_text.get_rect()
    screen.blit(title_text, (SCREEN_WIDTH/2 - title_size.width/2, SCREEN_HEIGHT/2))

    #draw input form
    input_box = pygame.Rect(SCREEN_WIDTH/2 - 100, (SCREEN_HEIGHT/2) + 20, 200, 32)
    input_text = Font(14).render(name, True, color)
    width = max(200, input_text.get_width()+10)
    input_box.width = width
    screen.blit(input_text, (input_box.x+5, input_box.y+5))
    pygame.draw.rect(screen, color, input_box, 2)

    #reload screen
    pygame.display.flip()
    clock.tick(30)

    #keyboard click control
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False
      if event.type == pygame.MOUSEBUTTONDOWN:
        if input_box.collidepoint(event.pos):
          active = not active
        else:
          active = False
        color = color_active if active else color_inactive
      if event.type == pygame.KEYDOWN:
        if active:
          if event.key == pygame.K_RETURN:
            return name
          elif event.key == pygame.K_BACKSPACE:
            name = name[:-1]
          else:
            name += event.unicode
