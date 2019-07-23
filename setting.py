import pygame, sys
from pygame.locals import*

pygame.init()

#setting screen size
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 480
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_WIDTH))

#setting font to use
def Font(num):
  return pygame.font.Font('assets/fonts/dragon-warrior-1.ttf', num)

#setting colors
BLACK = (0,0,0)
GREY = (180,180,180)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)

#bg
def Bg(num):
  if num == 1:
    img = pygame.image.load("assets/images/items/bg.jpg")
    return Transform(img, 500,500)
  elif num == 2:
    img = pygame.image.load("assets/images/items/castle_back.png")
    return Transform(img, 500,500)
  elif num == 3:
    img = pygame.image.load("assets/images/items/field_back.png")
    return Transform(img, 500,500)
  else:
    img = pygame.image.load("assets/images/items/bg.jpg")
    return Transform(img, 500,500)

def Transform(item, width, height):
  return pygame.transform.scale(item, (width, height))

def write_csv(name, stage):
  import csv, time
  now = time.ctime()
  cnvtime = time.strptime(now)
  time.strftime("%Y/%m/%d %H:%M", cnvtime) 
  with open('./record.csv','a') as f:
    writer = csv.writer(f)
    writer.writerow([time.strftime("%Y/%m/%d %H:%M", cnvtime) , name, stage])


#setting others
clock = pygame.time.Clock()
keys = pygame.key.get_pressed()
pygame.display.set_caption("Python Monsters")

#path
enemy_path = "assets/images/enemies/"
