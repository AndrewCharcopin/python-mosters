import pygame
from setting import *
from character import Slime, Goblin, Budda
from fight import *

class Stage():
  def __init__(self, player):
    pygame.init()
    player.left = False
    player.right = False
    self.bg = bg
    self.ready_fight_shown = False
    self.assign_Enemy_Bg(player)
    self.go(player)

  def assign_Enemy_Bg(self, player):
    if player.stage < 3:
      self.enemy = Slime()
    elif 3 <= player.stage and player.stage <6:
      self.bg = pygame.transform.scale(pygame.image.load("assets/images/field_bg.png") ,(SCREEN_WIDTH, SCREEN_HEIGHT))
      self.enemy = Goblin()
    else:
      self.bg = pygame.transform.scale(pygame.image.load("assets/images/castle_bg.png") ,(SCREEN_WIDTH, SCREEN_HEIGHT))
      self.enemy = Budda()


  def go(self, player):
    run = True
    while run:
      enemy = self.enemy
      #initialize screen
      screen.fill((30, 30, 30))
      #draw background image
      screen.blit(self.bg, (0,0))
      #draw player
      player_img = pygame.transform.flip(player.image, True, False) if player.right else player.image
      player_size = player_img.get_rect()
      screen.blit(player_img, (player.x, player.y))
      #draw enemy
      enemy_img = enemy.image
      screen.blit(enemy_img, (enemy.x, enemy.y))
      #draw status
      name_text = Font(14).render("player: " + player.name, True, BLACK)
      gold_text = Font(14).render("gold: " + str(player.gold), True, BLACK)
      stage_text = Font(14).render("stage: " + str(player.stage), True, BLACK)
      name_size = name_text.get_rect()
      gold_size = gold_text.get_rect()
      stage_size = stage_text.get_rect()
      screen.blit(name_text, (SCREEN_WIDTH - name_size.width, 0))
      screen.blit(gold_text, (SCREEN_WIDTH - gold_size.width, 20))
      screen.blit(stage_text, (SCREEN_WIDTH - stage_size.width, 40))
      #ready fight screen
      if self.ready_fight_shown:
        explain_text = Font(14).render("press enter to start a fight ", True, BLACK)
        explain_size = explain_text.get_rect()
        screen.blit(explain_text, (SCREEN_WIDTH/2 - explain_size.width/2, SCREEN_HEIGHT/2))

      keys = pygame.key.get_pressed()
      if keys[pygame.K_LEFT]:
        if 0 < player.x and player.x:
          player.x -= player.speed
          player.left = True
          player.right = False
        else:
          player.x
      elif keys[pygame.K_RIGHT]:
        if player.x < SCREEN_WIDTH - player_size.width:
          player.x += player.speed
          player.right = True
          player.left = False
        else:
          player.x

      if abs(player.x - enemy.x) < 50:
        self.ready_fight_shown = True
        if keys[pygame.K_RETURN]:
          Fight(player, enemy, self.bg)
          run = False
      else:
        self.ready_fight_shown = False

      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          run = False

      #reload screen
      pygame.display.flip()
      clock.tick(60)