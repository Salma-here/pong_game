class Settings:

    def __init__(self):
        # screen settings
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (0, 0, 0)

        # paddle settings
        self.paddle_width = 100
        self.paddle_height = 15
        self.paddle_margin = 15
        self.paddle_color = (255, 255, 255)
        self.paddle_speed = 1.0

        # ball settings
        self.ball_color = (255, 255, 255)
        self.ball_radius = 10
        self.ball_speed = 1.0
