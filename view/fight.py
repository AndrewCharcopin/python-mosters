import pygame
from setting import *
from controller.character import *
import random

def Fight(player):
  pygame.init()

  if player.stage == 1:
    enemy = Slime()
  elif player.stage == 2:
    enemy = Dracula()
  elif player.stage == 3:
    enemy = Vampire()
  elif player.stage == 4:
    enemy = Wolf()

  pygame.mixer.init()
  pygame.mixer.music.load('assets/sounds/boss.mp3')
  pygame.mixer.music.play(-1)

  select_dot_y = 80
  fire = Fire()
  thunder = Thunder()
  aqua = Aqua()
  player_skill = 0
  done = False
  run = True
  while run:
    #initialize screen
    screen.fill((30, 30, 30))
    #draw background image
    screen.blit(Bg(player.stage), (0,0))
    #draw player
    player.x = 20
    player.draw()
    player_hp_text = Font(12).render("player HP: " + str(player.hp), True, BLACK)
    screen.blit(player_hp_text, (0, 50))
    #draw enemy
    enemy.draw()
    enemy_hp_text = Font(12).render("enemy HP: " + str(enemy.hp), True, BLACK)
    enemy_hp_size = player_hp_text.get_rect()
    screen.blit(enemy_hp_text, (SCREEN_WIDTH - enemy_hp_size.width, 50))
    #draw battle
    title_text = Font(20).render("Fight!!", True, BLACK)
    title_size = title_text.get_rect()
    screen.blit(title_text, (SCREEN_WIDTH/2 - title_size.width/2, 30))
    #player fight option
    select_dot = Font(16).render("-", True, BLACK)
    fire_text = Font(12).render(fire.name, True, BLACK)
    fire_damage = Font(12).render("damage: " + str(fire.damage), True, BLACK)
    thunder_text = Font(12).render(thunder.name, True, BLACK)
    thunder_damage = Font(12).render("damage: " + str(thunder.damage), True, BLACK)
    aqua_text = Font(12).render(aqua.name, True, BLACK)
    aqua_damage = Font(12).render("damage: " + str(aqua.damage), True, BLACK)
    screen.blit(fire_text, (20, SCREEN_HEIGHT/2 - 80))
    screen.blit(thunder_text, (20, SCREEN_HEIGHT/2 - 60))
    screen.blit(aqua_text, (20, SCREEN_HEIGHT/2 - 40))
    screen.blit(select_dot, (0, SCREEN_HEIGHT/2 - select_dot_y))

    fire_skill = Font(16).render(fire.name + "!!", True, BLACK)
    thunder_skill = Font(16).render(thunder.name + "!!", True, BLACK)
    aqua_skill = Font(16).render(aqua.name + "!!", True, BLACK)
    if player.status == 1:
      if player.skill == 1:
        player.attack()
      elif player_skill == 2:
        screen.blit(thunder_skill, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 80))
        screen.blit(thunder_damage, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 100))
      elif player_skill == 3:
        screen.blit(aqua_skill, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 80))
        screen.blit(aqua_damage, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 100))
    elif enemy.status == 1:
      if player_skill == 1:
        screen.blit(fire_skill, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 80))
        screen.blit(fire_damage, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 100))
      elif player_skill == 2:
        screen.blit(thunder_skill, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 80))
        screen.blit(thunder_damage, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 100))
      elif player_skill == 3:
        screen.blit(aqua_skill, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 80))
        screen.blit(aqua_damage, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 100))

    if enemy.hp == 0:
      result_text = Font(16).render("congrats, you won!!", True, RED)
      result_size = result_text.get_rect()
      gold_text = Font(12).render("you got " + str(enemy.gold) + " gold", True, BLUE)
      gold_size = gold_text.get_rect()
      explain_text = Font(12).render("press enter to go to the next map", True, BLACK)
      explain_size = explain_text.get_rect()
      screen.blit(result_text, (SCREEN_WIDTH/2 - result_size.width/2, SCREEN_HEIGHT/2 + 60))
      screen.blit(gold_text, (SCREEN_WIDTH/2 - gold_size.width/2, SCREEN_HEIGHT/2 + 80))
      screen.blit(explain_text, (SCREEN_WIDTH/2 - explain_size.width/2, SCREEN_HEIGHT/2 + 100))
      done = True
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False
      if event.type == pygame.KEYDOWN:
        if player.status == 1:
          if event.key == pygame.K_UP and select_dot_y < 80:
            select_dot_y += 20
          if event.key == pygame.K_DOWN and select_dot_y > 40:
            select_dot_y -= 20
          if event.key == pygame.K_RETURN and select_dot_y == 80:
            player.skill = 1
            if enemy.hp < fire.damage:
              enemy.hp = 0
            else:
              enemy.hp -= fire.damage
          if event.key == pygame.K_RETURN and select_dot_y == 60:
            player.skill = 2
            if enemy.hp < thunder.damage:
              enemy.hp = 0
            else:
              enemy.hp -= thunder.damage
          if event.key == pygame.K_RETURN and select_dot_y == 40:
            player.skill = 3
            if enemy.hp < aqua.damage:
              enemy.hp = 0
            else:
              enemy.hp -= aqua.damage
        elif enemy.status == 1:
          return

        if event.key == pygame.K_RETURN and done == True:
          player_skill = 0
          player.gold += enemy.gold
          player.stage += 1
          return player

    #reload screen
    pygame.display.flip()
    clock.tick(30)
