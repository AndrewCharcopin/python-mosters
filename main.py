import pygame
from view.title import Title
from view.stage import Stage
from view.fight import Fight
from controller.character import Player
from view.animation import StartScreen, Prince, EndScreen
from setting import *

def main():
  StartScreen()
  player = Player(Title())
  while player.stage < 5:
    Stage(player)
    Fight(player)
  else:
    Write_csv(player)
    Prince(player)
    EndScreen()

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      quit()

if __name__ == "__main__":
  main()
