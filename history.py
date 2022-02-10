import pygame


class History:

    def __init__(self, pong_game):
        self.screen = pong_game.screen
        self.settings = pong_game.settings
        self.prefix_text = 'highest record: '
        self.highest_record = 0
        self.text = self.prefix_text + str(self.highest_record)

        self.font = pygame.font.SysFont(self.settings.default_font, self.settings.default_font_size)
        self.position = (230, 30)

    def display_highest_record(self):
        self.screen.blit(self.font.render(self.text, True, self.settings.default_color), self.position)

