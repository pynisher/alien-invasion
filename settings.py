class Settings():

    def __init__(self):

        # Настройки экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)

        # Настройки корабля
        self.ship_limit = 3
        
        # Настройки пуль
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 6
        
        # Настройка пришельцев
        self.fleet_drop_speed = 20
        
        # Темп ускорения игры
        self.speedup_scale = 1.1
        self.score_scale = 1.5
        
        self.initialize_dynamic_setting()

    def initialize_dynamic_setting(self):
        self.ship_speed = 1
        self.bullet_speed = 1.5
        self.alien_speed = 0.5
        self.fleet_direction = 1
        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
