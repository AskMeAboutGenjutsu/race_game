import pygame


class UserCar:

    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('images/user_car.png')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.bottom - 60
        self.move_right, self.move_left, self.move_up, self.move_down = False, False, False, False

    def rendering(self):
        self.screen.blit(self.image, self.rect)

    def update_position(self, speed):
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += speed
        if self.move_left and self.rect.left > 0:
            self.rect.centerx -= speed
        if self.move_up and self.rect.top > 450:
            self.rect.centery -= speed
        if self.move_down and self.rect.bottom < self.screen_rect.bottom - 10:
            self.rect.centery += speed

    def create_user_car(self):
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.bottom - 60
