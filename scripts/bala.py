# scripts/bala.py
# Nombre: Luis Miguel Montesino Cedeño
# Matrícula: 15-EISN-2-052

import pygame

class Bala(pygame.sprite.Sprite):  # Definimos la clase Bala que hereda de Sprite
    def __init__(self, x, y):
        super().__init__()  # Llama al constructor de la clase padre (Sprite)

        # Creamos una superficie pequeña (4 píxeles de ancho x 10 de alto)
        self.image = pygame.Surface((4, 10))  

        # Rellenamos la bala con un color azul (RGB)
        self.image.fill((64, 128, 255))  

        # Posicionamos la bala usando las coordenadas recibidas (x, y)
        self.rect = self.image.get_rect(center=(x, y))  

        # Velocidad vertical negativa para que la bala se mueva hacia arriba
        self.velocidad = -10  

    def update(self):
        # Mover la bala hacia arriba restando en el eje Y
        self.rect.y += self.velocidad  

        # Si la bala sale por la parte superior de la pantalla, se destruye
        if self.rect.bottom < 0:
            self.kill()  # Elimina la bala del grupo de sprites
