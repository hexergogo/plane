# import pygame
import pygame,copy,random,time
from pygame.locals import *
#我方飞机
class MyPlane(pygame.sprite.Sprite):
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.image1 = pygame.image.load("images/plane007.png").convert_alpha()
        self.image2 = pygame.image.load("images/plane008.png").convert_alpha()
        self.destroy_images = []
        self.destroy_images.extend([\
            pygame.image.load("images/me_destroy_1.png").convert_alpha(), \
            pygame.image.load("images/me_destroy_2.png").convert_alpha(), \
            pygame.image.load("images/me_destroy_3.png").convert_alpha(), \
            pygame.image.load("images/me_destroy_4.png").convert_alpha() \
            ])
        self.rect = self.image1.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.rect.left, self.rect.top = \
                        (self.width - self.rect.width) // 2, \
                        self.height - self.rect.height - 60
        self.speed = 10
        self.active = True
        self.invincible = False
        self.mask = pygame.mask.from_surface(self.image1)

    def moveUp(self):
        if self.rect.top > 0:
            self.rect.top -= self.speed
        else:
            self.rect.top = 0

    def moveDown(self):
        if self.rect.bottom < self.height - 60:
            self.rect.top += self.speed
        else:
            self.rect.bottom = self.height - 60

    def moveLeft(self):
        if self.rect.left > 0:
            self.rect.left -= self.speed
        else:
            self.rect.left = 0

    def moveRight(self):
        if self.rect.right < self.width:
            self.rect.left += self.speed
        else:
            self.rect.right = self.width

    def reset(self):
        self.rect.left, self.rect.top = \
                        (self.width - self.rect.width) // 2, \
                        self.height - self.rect.height - 60
        self.active = True
        self.invincible = True


#Bos
class Base():
    def __init__(self,windows,x,y):
        self.x = x
        self.y = y
        self.windows=windows
        self.normalIndex=0
        self.bombIndex=0
        self.isBomb=False
        self.zdList=[]
    def draw(self):
        if self.isBomb==False:
            pic=pygame.image.load(self.normalImageList[self.normalIndex])
            self.screen.blit(pic,(self.x,self.y))
            self.normalIndex=(self.normalIndex+1)%len(self.normalImageList)
        else:
            if self.bombIndex==len(self.bombImageList):
                time.sleep(0.08888)
                exit(0)
            pic = pygame.image.load(self.bombImageList[self.bombIndex])
            self.windows.blit(pic, (self.x, self.y))
            self.bombIndex = (self.bombIndex + 1)
            time.sleep(0.08888)

class Bullet(Base):
    def __init__(self,windows,x,y,path,moveSize):
        super().__init__(windows,x,y)
        self.moveSize=moveSize
        self.pic = pygame.image.load(path)
    def draw(self):
        pass
        # self.windows.blit(self.pic,(self.x,self.y))
        # self.move()
    def move(self):
        self.y+=self.moveSize

class EnemyPalne(Base):
    energy = 30
    def __init__(self,windows,x,y):
        super().__init__(windows,x,y)
        self.normalImageList=['.\\img\\enemy1.png']
        self.bombImageList=['.\\img\\enemy1_down1.png','.\\img\\enemy1_down2.png',
                            '.\\img\\enemy1_down3.png','.\\img\\enemy1_down4.png']
        self.direct="右"
    def draw(self):
        # super().draw()
        self.move()
        self.fire()
        tempList=copy.copy(self.zdList)
        for zd in tempList:
            zd.draw()
            self.zdList.remove(zd) if zd.y>600 else""
    def fire(self):
        d=random.randint(1,100)
        if d==3 or d==69:
            one=Bullet(self.windows,self.x+69//2 -9//2,89,'.\\img\\bullet1.png',3)
            self.zdList.append(one)
    def move(self):
        if self.direct=="右":
            self.x+=2
            if self.x>480-69:
                self.direct="左"
        else:
            self.x-=2
            if self.x<=0:
                self.direct="右"
    def pzjc(self,zdList):
        tempList=zdList
        EnemyRect = Rect(self.x, self.y, 69, 89)
        for zd in tempList:
            zdRect=Rect(zd.x,zd.y,22,22)
            if zdRect.colliderect(EnemyRect):
                self.isBomb=True
                zdList.remove(zd)