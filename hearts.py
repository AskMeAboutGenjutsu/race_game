import pygame


class Heart(pygame.sprite.Sprite):

    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load('images/live.png')
        self.rect = self.image.get_rect()
