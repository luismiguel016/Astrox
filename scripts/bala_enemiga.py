# scripts/bala_enemiga.py
# Nombre: Luis Miguel Montesino Cedeño
# Matrícula: 15-EISN-2-052

import pygame
import math

class BalaEnemiga(pygame.sprite.Sprite):
    def __init__(self, x, y, objetivo, velocidad=6):
        super().__init__()

        # Crear superficie de la bala (rectángulo rojo)
        self.image = pygame.Surface((5, 15))
        self.image.fill((255, 0, 0))  # Color rojo

        # Posición inicial de la bala (centrada en x, y)
        self.rect = self.image.get_rect(center=(x, y))

        # Calcular dirección hacia el objetivo (jugador)
        dx = objetivo.rect.centerx - x
        dy = objetivo.rect.centery - y

        # Calcular distancia (hipotenusa)
        distancia = math.hypot(dx, dy)
        if distancia == 0:
            distancia = 1  # Evitar división entre cero

        # Calcular velocidad en X e Y normalizada
        self.vel_x = dx / distancia * velocidad
        self.vel_y = dy / distancia * velocidad

    def update(self):
        """
        Mueve la bala hacia su dirección
        y la elimina si sale de la pantalla.
        """
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        # Eliminar si sale fuera del área visible (pantalla 800x600)
        if not (0 <= self.rect.x <= 800 and 0 <= self.rect.y <= 600):
            self.kill()
