import pygame
from view.title import Title
from view.stage import Stage
from view.fight import Fight
from controller.character import Player
from view.animation import StartScreen, Prince, EndScreen


def main():
  StartScreen()
  player = Player(Title())
  while player.stage < 5:
    Stage(player)
    Fight(player)
  else:
    Prince(player)
    EndScreen()

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

if __name__ == "__main__":
  main()
