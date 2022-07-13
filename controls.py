import pygame
from bots import Bot
import random
import time
from race_game import start_menu
import sys


def events(user_car, sound_wheel, sound_acc):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                user_car.move_right = True
                pygame.mixer.Sound.play(sound_wheel)
            if event.key == pygame.K_a:
                user_car.move_left = True
                pygame.mixer.Sound.play(sound_wheel)
            if event.key == pygame.K_w:
                user_car.move_up = True
                pygame.mixer.Sound.play(sound_acc)
            if event.key == pygame.K_s:
                user_car.move_down = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                user_car.move_right = False
            if event.key == pygame.K_a:
                user_car.move_left = False
            if event.key == pygame.K_w:
                user_car.move_up = False
            if event.key == pygame.K_s:
                user_car.move_down = False


def update_screen(screen, bg_color, user_car, bots_car, score, clock):
    screen.fill(bg_color)
    score.show_score()
    score.rendering_hearts()
    user_car.rendering()
    bots_car.draw(screen)
    pygame.display.flip()
    clock.tick(60)


def user_kill(stats, screen, user_car, bots_car, score, sound_death):
    if stats.user_car_left > 1:
        stats.user_car_left -= 1
        score.rendering_score()
        bots_car.empty()
        create_bots(screen, bots_car)
        user_car.create_user_car()
        time.sleep(1)
        pygame.mixer.Sound.play(sound_death)
        time.sleep(1)
    else:
        stats.run_game = False
        start_menu(message='You are dead! ')


def update_bots(stats, screen, bots_car, user_car, speed, score, sound_death):
    bots_car.update(speed)
    if pygame.sprite.spritecollideany(user_car, bots_car):
        user_kill(stats, screen, user_car, bots_car, score, sound_death)
    bots_check(screen, bots_car, stats, score)


def bots_check(screen, bots_car, stats, score):
    screen_rect = screen.get_rect()
    for bot in bots_car.sprites():
        if bot.rect.bottom >= screen_rect.bottom:
            bots_car.remove(bot)
            stats.score += 10
            score.rendering_score()
            check_high_score(stats, score)

    if len(bots_car) < 11:
        create_bots(screen, bots_car, 1)


def create_bots(screen, bots_car, count_bot_y=None):
    bot = Bot(screen)
    bot_height = bot.rect.height
    bot_width = bot.rect.width
    count_bot_x = 11
    if not count_bot_y:
        count_bot_y = 2

    for row_number in range(count_bot_y):
        random_count = random.randrange(1, 11)
        for bot_number in range(count_bot_x):
            if bot_number == random_count:
                continue
            elif bot_number == random_count + 1:
                continue
            elif bot_number == random_count - 1:
                continue
            else:
                bot = Bot(screen)
                bot.x = bot_width * bot_number
                bot.x = bot_width * bot_number * 1.05
                bot.y = bot_height + 3.5 * bot_height * row_number
                bot.rect.x = bot.x
                bot.rect.y = bot.rect.height // 2 * row_number
                bots_car.add(bot)


def check_high_score(stats, score):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        score.rendering_high_score()
        with open('high_score.txt', 'w') as f:
            f.write(f'{stats.high_score}')

