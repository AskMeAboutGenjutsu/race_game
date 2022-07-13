import pygame
import random


def get_bot_color():
    colors = ('yellow', 'blue', 'green', 'pink')
    return random.choice(colors)


class Bot(pygame.sprite.Sprite):

    def __init__(self, screen):
        super(Bot, self).__init__()
        self.screen = screen
        self.image = pygame.image.load(f'images/bot_{get_bot_color()}_car.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = self.rect.x
        self.y = self.rect.y

    def rendering(self):
        self.screen.blit(self.image, self.rect)

    def update(self, speed):
        self.y += speed
        self.rect.y = self.y
