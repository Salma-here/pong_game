import json
import pygame


class History:

    def __init__(self, pong_game):
        self.screen = pong_game.screen
        self.settings = pong_game.settings
        self.prefix_text = 'highest record: '
        self.postfix_text = ' seconds'
        self.highest_record = 0  # if no record exists
        self.filename = 'data.json'
        self.data_list = []  # saves record of how long previous games lasted

        # read from file
        # if file exists, show the highest previous record
        try:
            with open(self.filename) as f:
                self.data_list = json.load(f)
        except FileNotFoundError:
            pass
        else:
            sorted_list = sorted(self.data_list)
            self.highest_record = sorted_list[-1]

        self.text = self.prefix_text + str(self.highest_record) + self.postfix_text
        self.font = pygame.font.SysFont(self.settings.default_font, self.settings.default_font_size)
        self.position = (230, 30)

    def display_highest_record(self):
        self.screen.blit(self.font.render(self.text, True, self.settings.default_color), self.position)

    def log_data(self, new_data):
        # write to file
        # call from main
        self.data_list.append(new_data)
        try:
            with open(self.filename, 'w') as f:
                json.dump(self.data_list, f)
        except FileNotFoundError:
            pass
