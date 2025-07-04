# main.py
# Nombre: Luis Miguel Montesino Cedeño
# Matrícula: 15-EISN-2-052
# Archivo Principal del Juego

import pygame
import sys

# Inicialización de Pygame
pygame.init()

# Tamaño de la ventana
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Astrox")
clock = pygame.time.Clock()

# Colores que usare en mi proyecto
NEGRO = (0, 0, 0)
BLANCO= (255, 255, 255)
AZUL = (64, 128, 255)