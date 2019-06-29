import pygame
from setting import *
from controller.character import *

def Stage(player):
  pygame.init()
  #setting variables
  ready_fight_shown = False
  if player.stage == 1:
    enemy = Slime()
  elif player.stage == 2:
    enemy = Dracula()
  elif player.stage == 3:
    enemy = Wolf()
  run = True
  while run:
    #initialize screen
    screen.fill((30, 30, 30))
    #draw background image
    screen.blit(Bg(player.stage), (0,0))
    #draw player
    player.draw(screen)
    #draw enemy
    enemy.draw(screen)
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
        player.left = True
        player.right = False
      else:
        player.x
    elif keys[pygame.K_RIGHT]:
      if player.x < SCREEN_WIDTH - player.rect.width:
        player.x += player.speed
        player.right = True
        player.left = False
      else:
        player.x

    if abs(player.x - enemy.x) < 50:
      ready_fight_shown = True
      if keys[pygame.K_RETURN]:
        return player, enemy
    else:
      ready_fight_shown = False

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False

    #reload screen
    pygame.display.flip()
    clock.tick(30)