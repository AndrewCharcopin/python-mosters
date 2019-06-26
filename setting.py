import pygame

pygame.init()

#setting screen size
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 480
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_WIDTH))

#setting font to use
def Font(num):
  return pygame.font.Font('assets/dragon-warrior-1.ttf', num)

#setting colors
BLACK = (0,0,0)
GREY = (180,180,180)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)

#setting images
bg = pygame.image.load("assets/images/bg.jpg")

#setting others
clock = pygame.time.Clock()
keys = pygame.key.get_pressed()
pygame.display.set_caption("Python Monsters") 