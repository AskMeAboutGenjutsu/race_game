import pygame.font
from hearts import Heart
from pygame.sprite import Group


class Scores:

    def __init__(self, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_color = 0, 0, 0
        self.font = pygame.font.SysFont(None, 36)
        self.rendering_score()
        self.rendering_high_score()
        self.rendering_hearts()

    def rendering_score(self):
        self.score_img = self.font.render(f'Score: {self.stats.score}', True, self.text_color, (96, 96, 96))
        self.score_rect = self.score_img.get_rect()
        self.score_rect.centerx = self.screen_rect.centerx
        self.score_rect.top = 20

    def show_score(self):
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.high_score_img, self.high_score_rect)
        self.hearts.draw(self.screen)

    def rendering_high_score(self):
        self.high_score_img = self.font.render(f'High score: {self.stats.high_score}', True, self.text_color, (96, 96, 96))
        self.high_score_rect = self.high_score_img.get_rect()
        self.high_score_rect.right = self.screen_rect.right - 30
        self.high_score_rect.top = 20

    def rendering_hearts(self):
        self.hearts = Group()
        for heart_nmb in range(self.stats.user_car_left):
            heart = Heart(self.screen)
            heart.rect.x = 15 + heart_nmb * heart.rect.width
            heart.rect.y = 20
            self.hearts.add(heart)

