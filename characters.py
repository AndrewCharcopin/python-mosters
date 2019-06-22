import pygame
walk = [pygame.image.load('assets/slime/slime-move-0.png'),pygame.image.load('assets/slime/slime-move-1.png'),pygame.image.load('assets/slime/slime-move-2.png'),pygame.image.load('assets/slime/slime-move-3.png')]
standing = [pygame.image.load('assets/slime/slime-idle-0.png'),pygame.image.load('assets/slime/slime-idle-1.png'),pygame.image.load('assets/slime/slime-idle-2.png'),pygame.image.load('assets/slime/slime-idle-3.png')]
class Player(object):
    def __init__(self, x,y, name):
        self.x = x
        self.y = y
        self.width = 64
        self.height = 64
        self.name = name
        self.vel = 15
        self.right = True
        self.left = False
        self.standing = False
        self.walkCount = 0
        self.money = 100

    def draw(self, win):
        # 3frame per image
        if self.walkCount + 1 >= 12:
            self.walkCount = 0
        if not(self.standing):
            if self.left:
                win.blit(walk[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(pygame.transform.flip(walk[self.walkCount//3], True, False), (self.x, self.y))
                self.walkCount += 1
        # if idle images facing front exist
        # else:
        #     win.blit(pygame.transform.flip(standing[self.walkCount//3], True, False), (self.x, self.y))
        #     self.walkCount += 1

        # pygame.draw.rect(win, (255,0,0), (self.x, self.y, self.width, self.height))

class Enemy(object):
    def __init__(self, x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x + 20, self.y, 28, 60)
        self.text = "Hello! Let's fight!"
        self.textShown = False
        self.images = self.getImages()
        self.walkCount = 0

    def getImages(self):
        images = [pygame.image.load('assets/enemies/0.jpeg'), pygame.image.load('assets/enemies/1.jpeg'), pygame.image.load('assets/enemies/2.jpeg'), pygame.image.load('assets/enemies/3.jpeg')]
        return images
        
    def draw(self, win):
        if self.walkCount + 1 >= 12:
            self.walkCount = 0
        win.blit(self.images[self.walkCount//3], (self.x, self.y))
        self.walkCount += 1
        # pygame.draw.rect(win, (255,255,0), (self.x, self.y, self.width, self.height))

