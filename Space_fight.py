import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

# Формат PNG использовать где много однотонных областей, где потери не допустимы (тексты). Альфа канал для прозрачного фона.
# Формат JPEG если фотореалистичные изображения.
# Формат bmp родной формат для pygame.
class AlienInvasion():
    """Класс для управления ресурсами и поведением игры."""
    def __init__(self):
        """Инициализирует игру и создает игровые ресурсы."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_height, self.settings.screen_height))

        pygame.display.set_caption("Чертовы инопланетяне")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group() #Воспользуемся группой для прорисовки снарядов на экране при каждом
                                             #проходе основного цикла и обновления текущей позиции каждого снаряда.
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

        clock = pygame.time.Clock()
        FPS = 60
    def run_game(self):
        """Запуск основного цикла игры"""
        while True:  # Отслеживание событий клавиатуры и мыши.
            self._check_events()  # При каждом проходе цикла, перерисовывается экран.
            self.ship.update()
            self._update_screen()
            self._update_bullets()

        clock.tick(FPS)

    def _check_events(self):  #Обнаруживает важные события: нажатия и отпускания клавиш.
        """Обрабатывает нажатия клавиш и события мыши."""
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)


    def _check_keydown_events(self, event):
        """Реагирует на нажатие клавиш."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Реагирует на отпускание клавиш."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _fire_bullet(self):
        """Создание нового снаряда и включение его в группу bullets."""
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Обновляет позиции снарядов и уничтожает старые снаряды."""
        # Обновление позиций снарядов.
        self.bullets.update()  #Вызывает bullet.update() для каждого снаряда, включенного в группу bullets.
        # Удаление снарядов, вышедших за край экрана.
        for bullet in self.bullets.copy(): # Удаление снарядов, вышедших за край экрана.
            if bullet.rect.bottom <= 0: #Если снаряд пересек границу, он удаляется из bullets.
                self.bullets.remove(bullet)
            # print(len(self.bullets)) #Cообщает, сколько снарядов сейчас существует в игре; по выведенному значению
            # можно убедиться в том, что снаряды действительно удаляются при достижении
            # верхнего края экрана.

    def _create_fleet(self):
        """Создание флота вторжения."""
        # Создание пришельца и вычисление количества пришельцев в ряду
        # Интервал между соседними пришельцами равен ширине пришельца
        alien = Alien(self) # Создание пришельца.
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        """Определяет количество рядов, помещающихся на экране."""
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height -
                           (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        # Создание первого ряда пришельцев.
        for row_number in range(number_rows):

            for alien_number in range(number_aliens_x):
                # Создание пришельца и размещение его в ряду.
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        # alien_width = alien.rect.width
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _update_screen(self): #Перерисовывает экран при каждом проходе основного цикла.
        """Обновляет изображения на экране и отображает новый экран."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        pygame.display.flip()


# print(pygame.image.get_extended())  # Сообщает о том может ли данный комп. использовать изображения PNG и JPEG.

if __name__ == '__main__':
    # Создание экземпляра и запуск игры.
    ai = AlienInvasion()
    ai.run_game()
