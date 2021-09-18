import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Класс, представляющий одного пришельца."""

    def __init__(self, ai_game):
        """Инициализирует пришельца и задает его начальную позицию."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
    # Загрузка изображения пришельца и назначение атрибута rect.
        self.image = pygame.image.load(r'C:\Users\maind\PycharmProjects\Pictures\Alien_2.png')
        self.image = pygame.transform.scale(self.image,(50,50))
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.top = self.screen_rect.top

    # Каждый новый пришелец появляется в левом верхнем углу экрана.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
# Сохранение точной горизонтальной позиции пришельца.
        self.x = float(self.rect.x)

    def update(self):
        """Перемещает пришельца вправо."""
        self.x += self.settings.alien_speed
        self.rect.x = self.x

    def blite_2(self):
        self.screen.blit(self.image,self.rect)