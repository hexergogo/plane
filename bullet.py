import pygame
#子弹
class Bullet1(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("images/bullet1.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        self.speed = 12
        self.active = False
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        self.rect.top -= self.speed

        if self.rect.top < 0:
            self.active = False

    def reset(self, position):
        self.rect.left, self.rect.top = position
        self.active = True

class Bullet2(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("images/bullet2.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        self.speed = 14
        self.active = False
        self.mask = pygame.mask.from_surface(self.image)
    def move(self):
        self.rect.top -= self.speed

        if self.rect.top < 0:
            self.active = False

    def reset(self, position):
        self.rect.left, self.rect.top = position
        self.active = True
    

# class Bullet3(pygame.sprite.Sprite):
#     def __init__(self, position):
#         pygame.sprite.Sprite.__init__(self)
#
#         self.image = pygame.image.load("images/bullet-3.gif").convert_alpha()
#         self.rect = self.image.get_rect()
#         self.rect.left, self.rect.top = position
#         self.speed = 66
#         self.active = False
#         self.mask = pygame.mask.from_surface(self.image)
#     def move(self):
#         self.rect.top -= self.speed
#
#         if self.rect.top < 0:
#             self.active = False
#
#     def reset(self, position):
#         self.rect.left, self.rect.top = position
#         self.active = True