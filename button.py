import pygame


class Button:
    def __init__(self, screen, message):
        self.screen = screen
        self.width = 200
        self.height = 100
        self.active_color = 185, 185, 185
        self.inactive_color = 223, 223, 223
        self.message = message
        self.get_message()

    def draw(self, x, y, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x < mouse[0] < x + self.width and y < mouse[1] < y + self.height:
            pygame.draw.rect(self.screen, self.active_color, (x, y, self.width, self.height))
            self.screen.blit(self.text, (x + 70, y + 40))
            if click[0] == 1 and action:
                action()
        else:
            pygame.draw.rect(self.screen, self.inactive_color, (x, y, self.width, self.height))
            self.screen.blit(self.text, (x + 70, y + 40))

    def get_message(self):
        font = pygame.font.SysFont(None, 36)
        self.text = font.render(f'{self.message}', True, (0, 0, 0))