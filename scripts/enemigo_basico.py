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
        self.objetivo = objetivo  # La nave del jugador
        self.velocidad = 4

    def update(self):
    # Crear un pequeño desplazamiento aleatorio alrededor del jugador
     offset_x = random.randint(-50, 50)
     offset_y = random.randint(-50, 50)

    # Calcular la dirección hacia un punto cerca del jugador
     dx = (self.objetivo.rect.centerx + offset_x) - self.rect.centerx
     dy = (self.objetivo.rect.centery + offset_y) - self.rect.centery
     distancia = math.hypot(dx, dy)

     if distancia != 0:
        dx /= distancia
        dy /= distancia

    # Mover hacia el punto con desplazamiento
     self.rect.x += dx * self.velocidad
     self.rect.y += dy * self.velocidad
