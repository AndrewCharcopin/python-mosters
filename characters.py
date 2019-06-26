import pygame, os
import random
# walk = [pygame.image.load('assets/slime/slime-move-0.png'),pygame.image.load('assets/slime/slime-move-1.png'),pygame.image.load('assets/slime/slime-move-2.png'),pygame.image.load('assets/slime/slime-move-3.png')]
# standing = [pygame.image.load('assets/slime/slime-idle-0.png'),pygame.image.load('assets/slime/slime-idle-1.png'),pygame.image.load('assets/slime/slime-idle-2.png'),pygame.image.load('assets/slime/slime-idle-3.png')]
class Player(object):
    def __init__(self,name, x,y=380):
        self.x = x
        self.y = y
        self.startX = x
        self.width = 64
        self.height = 64
        self.name = name
        self.vel = 15
        self.right = True
        self.left = False
        self.standing = False
        self.walkCount = 0
        self.money = 100
        self.strength = 20
        self.hp = 120
        self.images = self.getImages()

    def getImages(self):
        images = []
        # Need 4 images!!
        for i in range(4):
            # e.g.) assets/images/enemies/wolf-0.png
            fullname = os.path.join('assets/images/enemies/', 'slime-%s.png' %(i))
            images.append(pygame.transform.scale(pygame.image.load(fullname), (self.width, self.height)))
        return images

    def draw(self, win):
        # 3frame per image
        if self.walkCount + 1 >= 12:
            self.walkCount = 0
        if not(self.standing):
            if self.left:
                win.blit(self.images[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(pygame.transform.flip(self.images[self.walkCount//3], True, False), (self.x, self.y))
                self.walkCount += 1
        # if idle images facing front exist
        # else:
        #     win.blit(pygame.transform.flip(standing[self.walkCount//3], True, False), (self.x, self.y))
        #     self.walkCount += 1

        # pygame.draw.rect(win, (255,0,0), (self.x, self.y, self.width, self.height))

    def fight(self, enemy):
      if self.strength > enemy.strength:
        self.money += enemy.reward
        return True
      else:
        return False

class Enemy(object):
    def __init__(self):
        self.x = 400
        self.y = 330
        self.width = 100
        self.height = 100
        self.hitbox = (self.x + 20, self.y, 28, 60)
        self.text = "Hello!, It's "+ self.name +"! Let's fight!"
        self.textShown = False
        self.walkCount = 0
        self.images = self.getImages()

    def getImages(self):
        images = []
        # Need 4 images!!
        for i in range(4):
            # e.g.) assets/images/enemies/wolf-0.png
            fullname = os.path.join('assets/images/enemies/', '%s-%s.png' %(self.name, i))
            images.append(pygame.transform.scale(pygame.image.load(fullname), (self.width, self.height)))
        return images

    def draw(self, win):
        if self.walkCount + 1 >= 12:
            self.walkCount = 0
        win.blit(self.images[self.walkCount//3], (self.x, self.y))
        self.walkCount = self.walkCount + 1
        # pygame.draw.rect(win, (255,255,0), (self.x, self.y, self.width, self.height))


class Slime(Enemy):
    def __init__(self):
        self.name = "slime"
        self.strength = 10
        self.hp = 40
        self.reward = 10
        super().__init__()

        

        
class Vampire(Enemy):
    def __init__(self):
        self.name = "vampire"
        self.strength = 15
        self.hp = 60
        self.reward = 20
        super().__init__()

class Wolf(Enemy):
    def __init__(self):
        self.name = "Wolf"
        self.strength = 20
        self.hp = 80
        self.reward = 30
        super().__init__()

