class Settings():
    """Класс для хранения всех настроек игры Alien Invasion."""

    def __init__(self):
        """Инициализирует настройки игры."""

        self.screen_width = 700 # Параметры экрана
        self.screen_height = 650 # Параметры экрана
        self.bg_color = (230, 230, 230)
        self.ship_speed = 0.3
        self.bullet_speed = 0.7
        self.bullet_width = 4
        self.bullet_height = 7
        self.bullet_color = (0, 0, 0)
        self.bullet_allowed = 3
        self.alien_speed = 0.3
        self.fleet_drop_speed = 10
        # fleet_direction = 1 обозначает движение вправо; а -1 - влево.
        self.fleet_direction = 1
