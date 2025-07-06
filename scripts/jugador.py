# scripts/jugador.py
# Nombre: Luis Miguel Montesino Cedeño
# Matrícula: 15-EISN-2-052
#Clase para controlar la nave por el jugador

import pygame
from scripts.bala import Bala

class NaveJugador(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.imagen_original = pygame.image.load("assets/images/nave.png").convert_alpha()
        self.imagen_original = pygame.transform.scale(self.imagen_original, (75, 75))
        self.image = self.imagen_original
        self.rect = self.image.get_rect(center=(x, y))
        self.mask = pygame.mask.from_surface(self.image)  # ✅ Máscara para colisión precisa

        self.balas = pygame.sprite.Group()

    def update(self, mouse_pos):
        self.rect.center = mouse_pos
        self.balas.update()

    def disparar(self):
        bala = Bala(self.rect.centerx, self.rect.top)
        self.balas.add(bala)

    def dibujar_balas(self, pantalla):
        self.balas.draw(pantalla)

      
        
