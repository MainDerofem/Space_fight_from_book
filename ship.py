import pygame

class Ship():
    """Класс для управления кораблем."""
    def __init__(self, ai_game):
        """Инициализирует корабль и задает его начальную позицию."""
        self.screen = ai_game.screen  # Экран присваевается атрибуту Ship.
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect() # Загружает изображение корабля и получает прямоугольник.

        self.image = pygame.image.load(r'C:\Users\maind\PycharmProjects\Pictures\Space_ship.bmp')
        self.image = pygame.transform.scale(self.image,(self.image.get_width()//30,self.image.get_height()//30))
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom # Каждый новый корабль появляется у нижнего края экрана.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.moving_right = False  # Флаг перемещения
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Обновляет позицию корабля с учетом флага."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        self.rect.x =self.x   # Обновление атрибута rect на основании self.x


        if self.moving_up:
            self.y -= self.settings.ship_speed
        if self.moving_down:
            self.y += self.settings.ship_speed
        self.rect.y = self.y  # Обновление атрибута rect на основании self.y

    def blitme(self):
        """Рисует корабль в текущей позиции."""
        self.screen.blit(self.image, self.rect) # Метод blit выводит изображеие на экран в позиции заданной self.rect




