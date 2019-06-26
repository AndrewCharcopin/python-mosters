import pygame
from setting import *

class Player():
  def __init__(self,name):
    self.name = name
    self.x = 20
    self.y = SCREEN_HEIGHT - 50
    self.speed = 3
    self.image = pygame.image.load("../assets/image_test/player.png")
    self.gold = 0
    self.stage = 1
    self.hp = 100



class Slime():
  def __init__(self):
    self.x = SCREEN_WIDTH - 50
    self.y = SCREEN_WIDTH - 50
    self.image = pygame.image.load("../assets/image_test/slime.png")
    self.hp = 50
    self.gold = 10

class Fire():
  def __init__(self):
    self.name = "fire"
    self.damage = 10
    self.image = pygame.image.load("../assets/image_test/skill.png")

class Thunder():
  def __init__(self):
    self.name = "thunder"
    self.damage = 15
    self.image = pygame.image.load("../assets/image_test/skill.png")

class Aqua():
  def __init__(self):
    self.name = "aqua"
    self.damage = 20
    self.image = pygame.image.load("../assets/image_test/skill.png")