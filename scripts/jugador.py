# scripts/jugador.py
# Nombre: Luis Miguel Montesino Cedeño
# Matrícula: 15-EISN-2-052
# Clase para controlar la nave del jugador

import pygame
from scripts.bala import Bala  # Clase para crear balas disparadas por el jugador

class NaveJugador(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        # Cargar imagen original de la nave y escalarla a 75x75 px
        self.imagen_original = pygame.image.load("assets/images/nave.png").convert_alpha()
        self.imagen_original = pygame.transform.scale(self.imagen_original, (75, 75))
        self.image = self.imagen_original

        # Establecer la posición inicial del jugador
        self.rect = self.image.get_rect(center=(x, y))

        # Generar una máscara para colisiones precisas (pixel-perfect)
        self.mask = pygame.mask.from_surface(self.image)

        # Grupo de balas disparadas por el jugador
        self.balas = pygame.sprite.Group()

    def update(self, mouse_pos):
        """
        Actualiza la posición de la nave para que siga al mouse.
        También actualiza la posición de todas las balas activas.
        """
        self.rect.center = mouse_pos
        self.balas.update()

    def disparar(self):
        """
        Crea una nueva bala en la posición actual de la nave
        y la añade al grupo de balas.
        """
        bala = Bala(self.rect.centerx, self.rect.top)
        self.balas.add(bala)

    def dibujar_balas(self, pantalla):
        """
        Dibuja todas las balas activas en la pantalla.
        """
        self.balas.draw(pantalla)


      
        
