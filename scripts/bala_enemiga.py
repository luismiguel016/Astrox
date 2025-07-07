# scripts/bala_enemiga.py
# Nombre: Luis Miguel Montesino Cedeño
# Matrícula: 15-EISN-2-052

import pygame
import math

class BalaEnemiga(pygame.sprite.Sprite):
    def __init__(self, x, y, objetivo, velocidad=6):
        super().__init__()
        self.image = pygame.Surface((5, 15))
        self.image.fill((255, 0, 0))  # Rojo
        self.rect = self.image.get_rect(center=(x, y))

        dx = objetivo.rect.centerx - x
        dy = objetivo.rect.centery - y
        distancia = math.hypot(dx, dy)
        if distancia == 0:
            distancia = 1
        self.vel_x = dx / distancia * velocidad
        self.vel_y = dy / distancia * velocidad

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        # Eliminar bala si se sale de pantalla
        if not (0 <= self.rect.x <= 800 and 0 <= self.rect.y <= 600):
            self.kill()
