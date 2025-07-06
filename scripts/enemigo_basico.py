# scripts/enemigo_basico.py
# Nombre: Luis Miguel Montesino Cedeño
# Matrícula: 15-EISN-2-052

import pygame
import math
import random

class EnemigoBasico(pygame.sprite.Sprite):
    def __init__(self, x, y, objetivo):
        super().__init__()
        self.image = pygame.image.load("assets/images/enemigo_basico.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect(center=(x, y))
        self.objetivo = objetivo
        self.velocidad = 4
        self.radio_colision = 20  

    def update(self):
        offset_x = random.randint(-40, 40)
        offset_y = random.randint(-40, 40)
        dx = (self.objetivo.rect.centerx + offset_x) - self.rect.centerx
        dy = (self.objetivo.rect.centery + offset_y) - self.rect.centery
        distancia = math.hypot(dx, dy)
        if distancia != 0:
            dx /= distancia
            dy /= distancia
        self.rect.x += dx * self.velocidad
        self.rect.y += dy * self.velocidad

    def obtener_centro(self):
        return self.rect.center
