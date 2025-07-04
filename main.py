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

from scripts.menu import mostrar_menu

# Cargar imagen del menú completo y ajustarla al tamaño de la ventana
menu_original = pygame.image.load("assets/images/astrox_menu.png").convert()
menu_image = pygame.transform.scale(menu_original, (WIDTH, HEIGHT))


# Mostrar menú antes de iniciar el juego
mostrar_menu(screen, menu_image)
