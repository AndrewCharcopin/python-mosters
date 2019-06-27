import pygame
from setting import *

class Player():
  def __init__(self,name):
    self.name = name
    self.x = 20
    self.y = SCREEN_HEIGHT - 50
    self.speed = 10
    self.rect = pygame.image.load("assets/image_test/player.png").get_rect()
    self.gold = 0
    self.stage = 1
    self.hp = 100
    self.right = True
    self.left = False
    self.walkCount = 0

  def draw(self, screen):
    if self.walkCount + 1 >= 12:
      self.walkCount = 0
    if self.left:
      screen.blit(player_img[self.walkCount//3], (self.x, self.y))
      self.walkCount += 1
    elif self.right:
      screen.blit(pygame.transform.flip(player_img[self.walkCount//3], True, False), (self.x, self.y))
      self.walkCount += 1

class Enemy():
  def __init__(self):
    self.x = SCREEN_WIDTH - 50
    self.y = SCREEN_WIDTH - 50
    self.walkCount = 0

  def draw(self, screen):
    if self.walkCount + 1 >= 12:
      self.walkCount = 0
    screen.blit(self.images[self.walkCount//3], (self.x, self.y))
    self.walkCount += 1

class Slime(Enemy):
  def __init__(self):
    super().__init__()
    self.images = [pygame.image.load('assets/slime/slime-move-0.png'),pygame.image.load('assets/slime/slime-move-1.png'),pygame.image.load('assets/slime/slime-move-2.png'),pygame.image.load('assets/slime/slime-move-3.png')]
    self.hp = 50
    self.gold = 10

class Goblin(Enemy):
  def __init__(self):
    super().__init__()
    self.images = [pygame.image.load("assets/image_test/goblin.png"),pygame.image.load("assets/image_test/goblin.png"),pygame.image.load("assets/image_test/goblin.png"),pygame.image.load("assets/image_test/goblin.png")]
    self.hp = 60
    self.gold = 20

class Budda(Enemy):
  def __init__(self):
    super().__init__()
    self.images = [pygame.image.load("assets/image_test/budda.png"),pygame.image.load("assets/image_test/budda.png"),pygame.image.load("assets/image_test/budda.png"),pygame.image.load("assets/image_test/budda.png")]
    self.hp = 100
    self.gold = 30

class Fire():
  def __init__(self):
    self.name = "fire"
    self.damage = 10

class Thunder():
  def __init__(self):
    self.name = "thunder"
    self.damage = 15

class Aqua():
  def __init__(self):
    self.name = "aqua"
    self.damage = 9999