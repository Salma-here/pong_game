import pygame


class Timer:

    def __init__(self, pong_game):
        self.screen = pong_game.screen
        self.settings = pong_game.settings
        self.clock = pygame.time.Clock()
        pygame.time.set_timer(pygame.USEREVENT, 1000)

        self.counter = 0  # keeps count of passed seconds
        self.text = '00:00'
        self.font = pygame.font.SysFont(self.settings.timer_font, self.settings.timer_font_size)
        self.position = (30, 30)

    def draw_timer(self):
        self.screen.blit(self.font.render(self.text, True, self.settings.timer_color), self.position)

    def update(self):
        self.counter += 1  # add one second to our second-counter
        minute = self.counter // 60
        second = self.counter % 60
        # if minute or second is single-digit, add one zero to the left
        # for decoration reasons :)
        str_minute = str(minute) if minute >= 10 else f'0{minute}'
        str_second = str(second) if second >= 10 else f'0{second}'
        self.text = f'{str_minute}:{str_second}'
        self.clock.tick(60)
