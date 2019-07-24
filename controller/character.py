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
    self.hp = 200
    self.right = True
    self.left = False
    self.walkCount = 0
    self.status = 0
    self.skill = 0
    self.charge = 1
    self.power = self.charge * 40

  def draw(self):
    if self.walkCount + 1 >= 12:
      self.walkCount = 0
    if self.left:
      screen.blit(self.images[self.walkCount//3], (self.x, self.y))
      self.walkCount += 1
    elif self.right:
      screen.blit(pygame.transform.flip(self.images[self.walkCount//3], True, False), (self.x, self.y))
      self.walkCount += 1

  def attack(self):
    text = Font(14).render("Attack: " + str(self.stage * 10), True, BLACK)
    screen.blit(text, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 80))
    self.skill = 1

  def barrier(self):
    text = Font(14).render("Barrier!", True, BLACK)
    screen.blit(text, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 80))
    self.skill = 2

  def charge(self):
    text = Font(14).render("Charge!", True, BLACK)
    screen.blit(text, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 80))
    self.skill = 3

class Enemy():
  def __init__(self,rect):
    self.x = SCREEN_WIDTH - rect.width - 20
    self.y = SCREEN_WIDTH - rect.height - 20
    self.rect = rect
    self.walkCount = 0
    self.status = 0
    self.skill = 0
    self.charge = 1

  def draw(self):
    if self.walkCount + 1 >= 12:
      self.walkCount = 0
    screen.blit(self.images[self.walkCount//3], (self.x, self.y))
    self.walkCount += 1

class Slime(Enemy):
  def __init__(self):
    rect = pygame.image.load(enemy_path + 'slime/slime-move-0.png').get_rect()
    super().__init__(rect)
    self.name = "Slime"
    self.images = [pygame.image.load(enemy_path + 'slime/slime-move-0.png'),pygame.image.load(enemy_path + 'slime/slime-move-1.png'),pygame.image.load(enemy_path + 'slime/slime-move-2.png'),pygame.image.load(enemy_path + 'slime/slime-move-3.png')]
    self.rect = rect
    self.hp = 50
    self.gold = 10
    self.power = 10

class Dracula(Enemy):
  def __init__(self):
    rect = pygame.image.load(enemy_path + 'dracula/dracula-0.jpeg').get_rect()
    super().__init__(rect)
    self.name = "Dracula"
    self.images = [pygame.image.load(enemy_path + "dracula/dracula-0.jpeg"),pygame.image.load(enemy_path + "dracula/dracula-1.jpeg"),pygame.image.load(enemy_path + "dracula/dracula-2.jpeg"),pygame.image.load(enemy_path + "dracula/dracula-3.jpeg")]
    self.rect = rect
    self.hp = 80
    self.gold = 20
    self.power = 20

class Vampire(Enemy):
  def __init__(self):
    rect = pygame.image.load(enemy_path + 'vampire/vampire-0.png').get_rect()
    super().__init__(rect)
    self.name = "Vampire"
    self.images = [pygame.image.load(enemy_path + "vampire/vampire-0.png"),pygame.image.load(enemy_path + "vampire/vampire-1.png"),pygame.image.load(enemy_path + "vampire/vampire-2.png"),pygame.image.load(enemy_path + "vampire/vampire-3.png")]
    self.rect = pygame.image.load(enemy_path + 'vampire/vampire-0.png').get_rect()
    self.hp = 100
    self.gold = 30
    self.power = 30

class Wolf(Enemy):
  def __init__(self):
    rect = pygame.image.load(enemy_path + 'wolf/wolf-0.png').get_rect()
    super().__init__(rect)
    self.name = "Wolf"
    self.images = [pygame.image.load(enemy_path + "wolf/wolf-0.png"),pygame.image.load(enemy_path + "wolf/wolf-1.png"),pygame.image.load(enemy_path + "wolf/wolf-2.png"),pygame.image.load(enemy_path + "wolf/wolf-3.png")]
    self.rect = rect
    self.hp = 200
    self.gold = 30
    self.power = 30

def Attack(obj):
  text = Font(14).render(obj.name + ": Attack! ", True, BLACK)
  sub_text = Font(12).render(str(obj.power * obj.charge) + " damage!", True, BLACK)
  screen.blit(text, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 80))
  screen.blit(sub_text, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 60))

def Barrier(obj):
  text = Font(14).render(str(obj.name) + ": Barrier!", True, BLACK)
  screen.blit(text, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 80))

def Charge(obj):
  text = Font(14).render(str(obj.name) + ": Charge! ", True, BLACK)
  screen.blit(text, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 80))