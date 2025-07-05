# scripts/jugador.py
# Nombre: Luis Miguel Montesino Cedeño
# Matrícula: 15-EISN-2-052
#Clase para controlar la nave por el jugador

import pygame
from scripts.bala import Bala #Importamos la clase bala

class NaveJugador(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        # Cargar la imagen de la nave
        self.imagen_original = pygame.image.load("assets/images/nave.png").convert_alpha()

        # Ajusta el tamaño de la nave
        self.imagen_original = pygame.transform.scale(self.imagen_original, (75,75))

        # Asigna la imagen actual a mostrar y su posición inicial
        self.image = self.imagen_original
        self.rect = self.image.get_rect(center=(x, y))

        # Grupo de sprite donde se guardan las balas disparadas
        self.balas = pygame.sprite.Group() 


    def update(self, teclas, mouse_pos):
        # Actualiza la posición de la nave para que siga al mouse
        self.rect.center = mouse_pos

        # Actualiza la posicion de todas las balas disparadas
        self.balas.update()##

    def disparar(self):
        # Crea una nueva bala en frente de la nave
        bala = Bala(self.rect.centerx, self.rect.top)
        self.balas.add(bala)

    def dibujar_balas(self, pantalla):
        # Dibuja todas las balas en la pantalla
        self.balas.draw(pantalla)

      
        
