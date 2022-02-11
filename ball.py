from random import random, choice

import pygame


class Ball:

    def __init__(self, pong_game):
        self.screen = pong_game.screen
        self.screen_rect = pong_game.screen.get_rect()
        self.settings = pong_game.settings
        self.paddle_rect = pong_game.paddle.rect

        self.color = self.settings.ball_color
        self.position = (self.screen.get_width() / 2, 50.0)
        self.radius = self.settings.ball_radius

        self.x = float(self.position[0])
        self.y = float(self.position[1])
        self.x_speed = self.settings.ball_speed
        self.y_speed = self.settings.ball_speed

        self.catch_number = 0  # number of times ball was caught with paddle
        # set to True when ball bounces off a wall
        # only bounces off paddle when this value is true (only after a wall-bounce)
        self.just_bounced = True
        self.game_running = pong_game.running

    def draw_ball(self):
        pygame.draw.circle(self.screen, self.color, self.position, self.radius)

    def update(self):
        self._bounce_walls()
        catch = self._bounce_paddle()
        if catch:
            self._change_color()
            self.catch_number += 1
        self._update_position()

    def _bounce_walls(self):
        right = float(self.position[0] + self.radius)
        if right >= self.screen_rect.right:
            self.x_speed = -self.x_speed
            self.just_bounced = True
        left = float(self.position[0] - self.radius)
        if left <= 0:
            self.x_speed = -self.x_speed
            self.just_bounced = True
        top = float(self.position[1] - self.radius)
        if top <= 0:
            self.y_speed = -self.y_speed
            self.just_bounced = True

    def _bounce_paddle(self):
        paddle_start = self.paddle_rect.left  # x attribute of right side
        paddle_end = self.paddle_rect.right  # x attribute of left side
        paddle_top = self.paddle_rect.top
        bottom = float(self.position[1] + self.radius)
        if paddle_start < self.x < paddle_end and paddle_top <= bottom and self.just_bounced:
            self.y_speed = -self.y_speed
            self.just_bounced = False
            return True

    def _update_position(self):
        # giving speed in y-axis a random value
        rand = random() * 3
        if self.y_speed < 0:
            self.y_speed = -rand
        else:
            self.y_speed = rand
        # updating ball position
        self.x += self.x_speed
        self.y += self.y_speed
        self.position = (self.x, self.y)

    def _change_color(self):
        self.color = choice(list(self.settings.color_dict.values()))

    def miss_ball(self):
        # check if game is over
        bottom = float(self.position[1] + self.radius)
        if bottom > self.screen_rect.bottom + self.radius * 2:
            return True
        return False
