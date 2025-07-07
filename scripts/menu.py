# scripts/menu.py
# Nombre: Luis Miguel Montesino Cedeño
# Matrícula: 15-EISN-2-052
# Pantalla principal del juego Astrox

# Muestra una imagen de menú y espera que el usuario presione ENTER o ESCAPE.

import pygame
import sys
import pygame.mixer

# Iniciar el mixer para audio
pygame.mixer.init()
pygame.mixer.music.load("assets/music/musica_menu.mp3")
pygame.mixer.music.play(-1)  # -1 para que se repita la musica

def mostrar_menu(screen, imagen_menu):
    """
    Muestra el menú principal, que es una imagen con el diseño del juego. 
    La imagen ya inccluye los textos "Presiona ENTER" y "Presiona ESC", por lo que no se gerena texto adcional desde el codigo.
    El progrema simplemente espera que el jugador presione ENTER o ESC para continuar o Salir.
    a continuancion crearmoos el evento necesario para estas acciones.
    """
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return  # Iniciar el juego
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        # Muestra la imagen del menú (ya escalada desde main.py)
        screen.blit(imagen_menu, (0, 0))

        pygame.display.flip()

