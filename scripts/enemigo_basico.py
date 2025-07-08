# scripts/enemigo_basico.py
# Nombre: Luis Miguel Montesino Cedeño
# Matrícula: 15-EISN-2-052

import pygame
import math
import random

class EnemigoBasico(pygame.sprite.Sprite):
    def __init__(self, x, y, objetivo):
        super().__init__()

        # Cargar imagen del enemigo básico y escalarla a 50x50 px
        self.image = pygame.image.load("assets/images/enemigo_basico.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))

        # Establecer posición inicial
        self.rect = self.image.get_rect(center=(x, y))

        # Referencia al objetivo (jugador)
        self.objetivo = objetivo

        # Velocidad de movimiento hacia el jugador
        self.velocidad = 4

        # Radio para colisiones circulares (para detección más precisa)
        self.radio_colision = 20

    def update(self):
        """
        Lógica de movimiento:
        El enemigo se mueve hacia el jugador, pero con un poco de ruido (offset aleatorio)
        para que no siempre siga en línea recta exacta.
        """
        # Generar un pequeño desvío aleatorio en la persecución
        offset_x = random.randint(-40, 40)
        offset_y = random.randint(-40, 40)

        # Calcular vector de dirección hacia el jugador
        dx = (self.objetivo.rect.centerx + offset_x) - self.rect.centerx
        dy = (self.objetivo.rect.centery + offset_y) - self.rect.centery

        # Calcular la distancia para normalizar
        distancia = math.hypot(dx, dy)

        # Evitar división por 0 y normalizar vector
        if distancia != 0:
            dx /= distancia
            dy /= distancia

        # Actualizar posición del enemigo
        self.rect.x += dx * self.velocidad
        self.rect.y += dy * self.velocidad

    def obtener_centro(self):
        """
        Devuelve el centro del enemigo. 
        Útil para cálculos de colisión o IA.
        """
        return self.rect.center

