import pygame
from title import Title
from map import Stage1
from character import Player

def main():
  player = Player(Title())
  Stage1(player)

if __name__ == "__main__":
  main()