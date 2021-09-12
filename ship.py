import pygame

class Ship():
    """Класс для управления кораблем."""
    def __init__(self, ai_game):
        """Инициализирует корабль и задает его начальную позицию."""
        self.screen = ai_game.screen  # Экран присваевается атрибуту Ship.
        self.screen_rect = ai_game.screen.get_rect()

        # Загружает изображение корабля и получает прямоугольник.
        self.image = pygame.image.load(r'C:\Users\maind\PycharmProjects\Pictures\Space_ship.bmp')
        self.image = pygame.transform.scale(self.image,(self.image.get_width()//20,self.image.get_height()//20))
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom # Каждый новый корабль появляется у нижнего края экрана.
        self.moving_right = False  # Флаг перемещения
        self.moving_left = False

    def update(self):
        """Обновляет позицию корабля с учетом флага."""
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1

    def blitme(self):
        """Рисует корабль в текущей позиции."""
        self.screen.blit(self.image, self.rect) # Метод blit выводитизображеие на экран в позиции заданной self.rect




