import pygame
from view.title import Title
from view.stage import Stage
from view.fight import Fight
from controller.character import Player


def main():
  player = Player(Title())
  while player.stage < 5:
    Stage(player)
    Fight(player)

if __name__ == "__main__":
  main()