import pygame
from setting import *

class Player():
  def __init__(self,name):
    self.name = name
    self.x = 20
    self.y = SCREEN_HEIGHT - 50
    self.speed = 10
    self.images = [pygame.image.load(enemy_path + 'slime/slime-move-0.png'),pygame.image.load(enemy_path + 'slime/slime-move-1.png'),pygame.image.load(enemy_path + 'slime/slime-move-2.png'),pygame.image.load(enemy_path + 'slime/slime-move-3.png')]
    self.rect = pygame.image.load(enemy_path + 'slime/slime-move-0.png').get_rect()
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
      screen.blit(self.images[self.walkCount//3], (self.x, self.y))
      self.walkCount += 1
    elif self.right:
      screen.blit(pygame.transform.flip(self.images[self.walkCount//3], True, False), (self.x, self.y))
      self.walkCount += 1

class Enemy():
  def __init__(self,rect):
    self.x = SCREEN_WIDTH - rect.width - 20
    self.y = SCREEN_WIDTH - rect.height - 20
    self.rect = rect
    self.walkCount = 0

  def draw(self, screen):
    if self.walkCount + 1 >= 12:
      self.walkCount = 0
    screen.blit(self.images[self.walkCount//3], (self.x, self.y))
    self.walkCount += 1

class Slime(Enemy):
  def __init__(self):
    rect = pygame.image.load(enemy_path + 'slime/slime-move-0.png').get_rect()
    super().__init__(rect)
    self.images = [pygame.image.load(enemy_path + 'slime/slime-move-0.png'),pygame.image.load(enemy_path + 'slime/slime-move-1.png'),pygame.image.load(enemy_path + 'slime/slime-move-2.png'),pygame.image.load(enemy_path + 'slime/slime-move-3.png')]
    self.rect = rect
    self.hp = 50
    self.gold = 10

class Dracula(Enemy):
  def __init__(self):
    rect = pygame.image.load(enemy_path + 'dracula/dracula-0.jpeg').get_rect()
    super().__init__(rect)
    self.images = [pygame.image.load(enemy_path + "dracula/dracula-0.jpeg"),pygame.image.load(enemy_path + "dracula/dracula-1.jpeg"),pygame.image.load(enemy_path + "dracula/dracula-2.jpeg"),pygame.image.load(enemy_path + "dracula/dracula-3.jpeg")]
    self.rect = rect
    self.hp = 60
    self.gold = 20

class Vampire(Enemy):
  def __init__(self):
    rect = pygame.image.load(enemy_path + 'vampire/vampire-0.png').get_rect()
    super().__init__(rect)
    self.images = [pygame.image.load(enemy_path + "vampire/vampire-0.png"),pygame.image.load(enemy_path + "vampire/vampire-1.png"),pygame.image.load(enemy_path + "vampire/vampire-2.png"),pygame.image.load(enemy_path + "vampire/vampire-3.png")]
    self.rect = pygame.image.load(enemy_path + 'vampire/vampire-0.png').get_rect()
    self.hp = 100
    self.gold = 30

class Wolf(Enemy):
  def __init__(self):
    rect = pygame.image.load(enemy_path + 'wolf/wolf-0.png').get_rect()
    super().__init__(rect)
    self.images = [pygame.image.load(enemy_path + "wolf/wolf-0.png"),pygame.image.load(enemy_path + "wolf/wolf-1.png"),pygame.image.load(enemy_path + "wolf/wolf-2.png"),pygame.image.load(enemy_path + "wolf/wolf-3.png")]
    self.rect = rect
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
    self.damage = 20