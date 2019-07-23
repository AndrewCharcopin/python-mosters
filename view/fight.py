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
	done = False
	run = True
	enemy.skill = random.randint(1,3)
	while run:
		#initialize screen
		screen.fill((30, 30, 30))
		#draw background image
		screen.blit(Bg(player.stage), (0,0))
		#draw player
		player.x = 20
		player.draw()
		player_hp_text = Font(12).render("HP: " + str(player.hp), True, BLACK)
		player_charge_text = Font(12).render("Attack: " + str(player.power * player.charge), True, BLACK)
		screen.blit(player_hp_text, (0, 50))
		screen.blit(player_charge_text, (0, 30))
		#draw enemy
		enemy.draw()
		if enemy.hp > 0:
			enemy_hp_text = Font(12).render("HP: " + str(enemy.hp), True, BLACK)
		else:
			enemy_hp_text = Font(12).render("enemy: DEAD", True, BLACK)
		enemy_hp_size = player_hp_text.get_rect()
		enemy_charge_text = Font(12).render("Attack: " + str(enemy.power * enemy.charge), True, BLACK)
		enemy_charge_size = enemy_charge_text.get_rect()
		screen.blit(enemy_hp_text, (SCREEN_WIDTH - enemy_hp_size.width, 50))
		screen.blit(enemy_charge_text, (SCREEN_WIDTH - enemy_charge_size.width, 30))
		#draw battle
		title_text = Font(20).render("Fight!!", True, BLACK)
		title_size = title_text.get_rect()
		screen.blit(title_text, (SCREEN_WIDTH/2 - title_size.width/2, 30))
		#player fight option
		select_dot = Font(16).render("-", True, BLACK)
		attack_text = Font(12).render("Attack", True, BLACK)
		barrier_text = Font(12).render("Barrier", True, BLACK)
		charge_text = Font(12).render("Charge", True, BLACK)
		screen.blit(attack_text, (20, SCREEN_HEIGHT/2 - 80))
		screen.blit(barrier_text, (20, SCREEN_HEIGHT/2 - 60))
		screen.blit(charge_text, (20, SCREEN_HEIGHT/2 - 40))
		screen.blit(select_dot, (0, SCREEN_HEIGHT/2 - select_dot_y))

		if (player.status == 1 and enemy.status == 0) or (player.status == 1 and enemy.skill == 2):
			if player.skill == 1:
				Attack(player)
			elif player.skill == 2:
				Barrier(player)
			elif player.skill == 3:
				Charge(player)
		elif enemy.status == 1:
			if enemy.skill == 1:
				Attack(enemy)
			elif enemy.skill == 2:
				Barrier(enemy)
			elif enemy.skill == 3:
				Charge(enemy)

		if enemy.hp <= 0:
			result_text = Font(16).render("congrats, you won!!", True, RED)
			result_size = result_text.get_rect()
			gold_text = Font(12).render("you got " + str(enemy.gold) + " gold", True, BLUE)
			gold_size = gold_text.get_rect()
			explain_text = Font(12).render("press space to go to the next map", True, BLACK)
			explain_size = explain_text.get_rect()
			screen.blit(result_text, (SCREEN_WIDTH/2 - result_size.width/2, SCREEN_HEIGHT/2 + 60))
			screen.blit(gold_text, (SCREEN_WIDTH/2 - gold_size.width/2, SCREEN_HEIGHT/2 + 80))
			screen.blit(explain_text, (SCREEN_WIDTH/2 - explain_size.width/2, SCREEN_HEIGHT/2 + 100))
			done = True
		elif player.hp <= 0:
			result_text = Font(16).render("Ohhh, you lost...", True, RED)
			result_size = result_text.get_rect()
			explain_text = Font(12).render("press space to try again", True, BLACK)
			explain_size = explain_text.get_rect()
			screen.blit(result_text, (SCREEN_WIDTH/2 - result_size.width/2, SCREEN_HEIGHT/2 + 60))
			screen.blit(explain_text, (SCREEN_WIDTH/2 - explain_size.width/2, SCREEN_HEIGHT/2 + 100))

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
			if event.type == pygame.KEYDOWN:
				#choose attack
				if player.status == 0 and enemy.status == 0 and player.hp >= 0 and enemy.hp >= 0:
					if event.key == pygame.K_UP and select_dot_y < 80:
						select_dot_y += 20
					elif event.key == pygame.K_DOWN and select_dot_y > 40:
						select_dot_y -= 20
					elif event.key == pygame.K_RETURN and select_dot_y == 80:
						player.skill = 1
						if enemy.skill == 2:
							enemy.status += 1
						else:
							player.status += 1
					elif event.key == pygame.K_RETURN and select_dot_y == 60:
						player.skill = 2
						if enemy.skill == 2:
							enemy.status += 1
						else:
							player.status += 1
					elif event.key == pygame.K_RETURN and select_dot_y == 40:
						player.skill = 3
						if enemy.skill == 2:
							enemy.status += 1
						else:
							player.status += 1
				elif player.status + enemy.status == 2:
					if event.key == pygame.K_RETURN:
						player.status = 0
						enemy.status = 0
						enemy.skill = random.randint(1,3)
				#check if enemy barriered
				elif player.status == 1 and enemy.status < 2:
					if event.key == pygame.K_RETURN:
						if enemy.skill == 1 and player.skill != 2:
							player.hp -= enemy.power * enemy.charge
							enemy.charge = 1
						elif enemy.skill == 1 and player.skill == 2:
							enemy.charge = 1
						elif enemy.skill == 2:
							enemy.status = 1
						elif enemy.skill == 3:
							enemy.charge = enemy.charge * 2
						if player.skill == 1:
							enemy.hp -= player.power * player.charge
							player.charge = 1
						elif player.skill == 3:
							player.charge = player.charge * 2
						enemy.status += 1
				elif enemy.status == 1 and player.status < 2:
					if event.key == pygame.K_RETURN:
						if enemy.skill == 1:
							player.hp -= enemy.power * enemy.charge
							enemy.charge = 1
						elif enemy.skill == 3:
							enemy.charge = enemy.charge * 2
						if player.skill == 3:
							player.charge = player.charge * 2
						elif player.skill == 1:
							player.charge = 1
						player.status += 1

				if event.key == pygame.K_SPACE and done == True:
					player.skill = 0
					player.gold += enemy.gold
					player.stage += 1
					player.status = 0
					player.charge = 1
					player.hp = 100
					return player

				if event.key == pygame.K_SPACE and player.hp <= 0:
					player.status = 0
					player.charge = 1
					player.hp = 100
					return player

		#reload screen
		pygame.display.flip()
		clock.tick(30)
