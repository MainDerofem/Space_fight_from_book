import sys
import pygame
from settings import Settings
from ship import Ship
#Формат PNG использовать где много однотонных областей, где потери не допустимы (тексты). Альфа канал для прозрачного фона.
#Формат JPEG если фотореалистичные изображения.
#Формат bmp родной формат для pygame.
class AlienInvasion():
    """Класс для управления ресурсами и поведением игры."""

    def __init__(self):
        """Инициализирует игру и создает игровые ресурсы."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_height, self.settings.screen_height))

        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)


    def run_game(self):
        """Запуск основного цикла игры"""
        while True:  # Отслеживание событий клавиатуры и мыши.
            self._check_events() # При каждом проходе цикла, перерисовывается экран.
            self._update_screen()
            self.ship.update()

    def _check_events(self):
        """Обрабатывает нажатия клавиш и события мыши."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type ==pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key ==pygame.K_LEFT:
                    self.ship.moving_left = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key ==pygame.K_LEFT:
                    self.ship.moving_left = False



    def _update_screen(self):
        """Обновляет изображения на экране и отображает новый экран."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        pygame.display.flip()

print(pygame.image.get_extended()) #Сообщает о том может ли данный комп. использовать изображения PNG и JPEG.

if __name__ == '__main__':
    # Создание экземпляра и запуск игры.
    ai = AlienInvasion()
    ai.run_game()
