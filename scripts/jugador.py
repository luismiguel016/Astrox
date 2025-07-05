# scripts/jugador.py
# Nombre: Luis Miguel Montesino Cedeño
# Matrícula: 15-EISN-2-052
#Clase para controlar la nave por el jugador

import pygame

class NaveJugador(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        # Cargar imagen de la nave y establecer transparencia
        self.imagen_original = pygame.image.load("assets/images/nave.png").convert_alpha()

        # Ajusta este tamaño de la nave
        self.imagen_original = pygame.transform.scale(self.imagen_original, (75,75))

        self.image = self.imagen_original
        self.rect = self.image.get_rect(center=(x, y))

    def update(self, teclas, mouse_pos):
        # Actualizar la posición de la nave para que siga al mouse
        self.rect.center = mouse_pos