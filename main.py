# main.py
# Nombre: Luis Miguel Montesino Cedeño
# Matrícula: 15-EISN-2-052
# Archivo Principal del Juego

import pygame
import sys


# Inicialización de Pygame
pygame.init()
pygame.mouse.set_visible(False)

# Tamaño de la ventana
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Astrox")
clock = pygame.time.Clock()

# Colores que usare en mi proyecto
NEGRO = (0, 0, 0)
BLANCO= (255, 255, 255)
AZUL = (64, 128, 255)

# Importa la función que muestra el menú principal del juego
from scripts.menu import mostrar_menu  


# Cargar imagen del menú completo y ajustarla al tamaño de la ventana
menu_original = pygame.image.load("assets/images/astrox_menu.png").convert()
menu_image = pygame.transform.scale(menu_original, (WIDTH, HEIGHT))


# Mostrar menú antes de iniciar el juego
mostrar_menu(screen, menu_image)

# Importar la clase de la nave del jugador desde jugador.py
from scripts.jugador import NaveJugador

# ===== ganas de llorar no me faltan ===========
# Crear la nave del jugador y el grupo de sprites
# ==============================================

# Instanciar la nave en el centro de la pantalla
nave = NaveJugador(WIDTH // 2, HEIGHT // 2)

# Crear un grupo de sprites y añadir la nave
grupo_naves = pygame.sprite.Group()
grupo_naves.add(nave)


# Bucle principal del juego

while True:
    # Manejo de eventos (salir del juego, etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        ##########################################################
 # Disparo con clic izquierdo del mouse
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # 1 = botón izquierdo
                nave.disparar()

    # Entrada del usuario (posiciones de teclado y mouse)
    teclas = pygame.key.get_pressed()
    mouse_pos = pygame.mouse.get_pos()

    # Actualizar la nave (y sus balas)
    grupo_naves.update(teclas, mouse_pos)

    # Dibujar fondo, nave y balas
    screen.fill(NEGRO)
    grupo_naves.draw(screen)
    nave.dibujar_balas(screen)  # Mostrar las balas disparadas

    # Actualizar pantalla
    pygame.display.flip()
    clock.tick(60)  # Limitar a 60 FPS



    # =============================
    # Entrada del jugador
    # =============================

    # Detectar teclas presionadas y posición del mouse
    teclas = pygame.key.get_pressed()
    mouse_pos = pygame.mouse.get_pos()

    # =============================
    # Actualización de la lógica del juego
    # =============================

    # Actualizar la posición y estado de la nave según la entrada
    grupo_naves.update(teclas, mouse_pos)

    # =============================
    # Dibujar elementos en pantalla
    # =============================

    # Limpiar la pantalla
    screen.fill(NEGRO)

    # Dibujar la nave
    grupo_naves.draw(screen)

    # Actualizar la pantalla
    pygame.display.flip()

    # Esperar para mantener 60 FPS
    clock.tick(60)


