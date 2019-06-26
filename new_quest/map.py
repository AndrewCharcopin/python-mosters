import pygame
from setting import *
from character import Slime
from fight import *

def Stage1(player):
  pygame.init()
  #setting variables
  left = False
  right = False
  ready_fight_shown = False

  run = True
  while run:
    slime = Slime()
    #initialize screen
    screen.fill((30, 30, 30))
    #draw background image
    screen.blit(bg, (0,0))
    #draw player
    player_img = pygame.transform.flip(player.image, True, False) if right else player.image
    player_size = player_img.get_rect()
    screen.blit(player_img, (player.x, player.y))
    #draw enemy
    slime_img = slime.image
    screen.blit(slime_img, (slime.x, slime.y))
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
    if ready_fight_shown:
      explain_text = Font(14).render("press enter to start a fight ", True, BLACK)
      explain_size = explain_text.get_rect()
      screen.blit(explain_text, (SCREEN_WIDTH/2 - explain_size.width/2, SCREEN_HEIGHT/2))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
      if 0 < player.x and player.x:
        player.x -= player.speed
        left = True
        right = False
      else:
        player.x
    elif keys[pygame.K_RIGHT]:
      if player.x < SCREEN_WIDTH - player_size.width:
        player.x += player.speed
        right = True
        left = False
      else:
        player.x

    if abs(player.x - slime.x) < 50:
      ready_fight_shown = True
      if keys[pygame.K_RETURN]:
        Fight(player, slime)
    else:
      ready_fight_shown = False

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False

    #reload screen
    pygame.display.flip()
    clock.tick(60)
