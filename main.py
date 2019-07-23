import pygame
from view.title import Title
from view.stage import Stage
from view.fight import Fight
from view.animation import StartScreen
from controller.character import Player

def main():
  StartScreen()
  player = Player(Title())
  while player.stage < 5:
    Stage(player)
    Fight(player)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

if __name__ == "__main__":
  main()
