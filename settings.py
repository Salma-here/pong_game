class Settings:

    def __init__(self):
        # screen settings
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (0, 0, 0)

        # paddle settings
        self.paddle_width = 200
        self.paddle_height = 20
        self.paddle_margin = 20
        self.paddle_color = (247, 37, 167)  # bright pink
        self.paddle_speed = 2.0

        # ball settings
        self.ball_color = (255, 255, 255)
        self.ball_radius = 15
        self.ball_speed = 0.5

        # timer settings
        self.timer_color = (247, 37, 167)  # bright pink
        self.timer_font = 'Consolas'
        self.timer_font_size = 30

        # color dictionary
        self.color_dict = {
            'light-blue': (37, 111, 247),
            'blue': (10, 16, 173),
            'light-green': (113, 214, 111),
            'lime-green': (111, 214, 190),
            'green': (8, 135, 29),
            'yellow': (208, 224, 31),
            'red': (224, 31, 31),
            'pink': (230, 110, 220),
            'purple': (125, 4, 115)
        }

