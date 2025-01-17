import pygame
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
  elif num == 4:
    img = pygame.image.load("assets/images/items/back_castle.jpeg")
    return Transform(img, 500,500)
  elif num == 5:
    img = pygame.image.load("assets/images/items/hime_haikei.jpg")
    return Transform(img, 500,500)
  else:
    img = pygame.image.load("assets/images/items/bg.jpg")
    return Transform(img, 500,500)

def Transform(item, width, height):
  return pygame.transform.scale(item, (width, height))

def Write_csv(player):
  import csv, time
  now = time.ctime()
  cnvtime = time.strptime(now)
  time.strftime("%Y/%m/%d %H:%M", cnvtime)
  file_name = './record.csv'
  try:
    f = open(file_name)
  except IndexError:
    print ('Usage: %s TEXTFILE' % file_name)
  except IOError:
    print ('"%s" cannot be opened.' % file_name)
  else:
    with open(file_name,'a') as f:
      writer = csv.writer(f)
      writer.writerow([time.strftime("%Y/%m/%d %H:%M", cnvtime) , player.name, player.stage])
    f.close()
  finally:
    print ('n"%s" process end.' % file_name)


#setting others
clock = pygame.time.Clock()
keys = pygame.key.get_pressed()
pygame.display.set_caption("Python Monsters")

#path
enemy_path = "assets/images/enemies/"
