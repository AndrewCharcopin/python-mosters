import pygame
from title import Title
from map import Stage
from character import Player

def main():
  player = Player(Title())
  run = True
  while run:
    Stage(player)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False

if __name__ == "__main__":
  main()