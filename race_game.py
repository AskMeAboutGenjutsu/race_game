import pygame
import controls
from user_car import UserCar
from stats import Stats
from pygame.sprite import Group
from scores import Scores
from button import Button
import sys
from time import time


def start_menu(message = None):
    pygame.init()
    screen = pygame.display.set_mode((700, 800))
    pygame.display.set_caption('Ultra Race')
    pygame.display.set_icon(pygame.image.load('images/icon.ico'))
    menu = pygame.image.load('images/menu.png')
    button_start = Button(screen, 'Play')
    clock = pygame.time.Clock()
    pygame.mixer.music.pause()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.blit(menu, (0, 0))
        button_start.draw(250, 350, action=run)

        if message:
            font = pygame.font.SysFont(None, 50)
            text = font.render(message, True, (255, 255, 255), (255, 0, 0))
            screen.blit(text, (235, 250))

        pygame.display.update()
        clock.tick(60)


def run():
    strt = time()
    screen = pygame.display.set_mode((700, 800))
    clock = pygame.time.Clock()
    bg_color = 96, 96, 96
    user_car = UserCar(screen)
    bots_car = Group()
    controls.create_bots(screen, bots_car)
    stats = Stats()
    score = Scores(screen, stats)
    sound_wheel = pygame.mixer.Sound('sounds/sound_wheel.wav')
    sound_acc = pygame.mixer.Sound('sounds/car_acc.wav')
    sound_death = pygame.mixer.Sound('sounds/death.wav')
    pygame.mixer.music.load('sounds/main_music.mp3')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.Sound.set_volume(sound_wheel, 0.2)
    pygame.mixer.Sound.set_volume(sound_acc, 0.2)

    while True:
        controls.events(user_car, sound_wheel, sound_acc)

        if stats.run_game:
            if time() - strt <= 10:
                user_car.update_position(speed=7)
                controls.update_bots(stats, screen, bots_car, user_car, speed=1, score=score, sound_death= sound_death)
            elif 10 < time() - strt <= 20:
                user_car.update_position(speed=10)
                controls.update_bots(stats, screen, bots_car, user_car, speed=2, score=score, sound_death= sound_death)
            elif 20 < time() - strt <= 30:
                user_car.update_position(speed=13)
                controls.update_bots(stats, screen, bots_car, user_car, speed=3, score=score, sound_death= sound_death)
            elif 30 < time() - strt <= 40:
                user_car.update_position(speed=15)
                controls.update_bots(stats, screen, bots_car, user_car, speed=5, score=score, sound_death= sound_death)
            else:
                user_car.update_position(speed=17)
                controls.update_bots(stats, screen, bots_car, user_car, speed=6, score=score, sound_death= sound_death)

            controls.update_screen(screen, bg_color, user_car, bots_car, score, clock)


if __name__ == '__main__':
    start_menu()
