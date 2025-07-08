# main.py
# Nombre: Luis Miguel Montesino Cedeño
# Matrícula: 15-EISN-2-052
# Archivo Principal del Juego

import pygame
import sys
import random
import math
import os
from scripts.enemigo_basico import EnemigoBasico
from scripts.meteorito_astar import MeteoritoAStar


# Inicialización de Pygame
pygame.init()
pygame.mouse.set_visible(False)

# Inicializar el mezclador de sonido
pygame.mixer.init()

# Cargar sonido de disparo
sonido_disparo = pygame.mixer.Sound("assets/sounds/disparo_nave.mp3")
sonido_disparo.set_volume(0.4)                                               # Puedes ajustar el volumen si quieres

# Tamaño de la ventana
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN | pygame.SCALED)
pygame.display.set_caption("Astrox")
clock = pygame.time.Clock()

# Cargar imagen de fondo del juego y escalarla al tamaño de la ventana
fondo_juego = pygame.image.load("assets/images/fondo.png").convert()
fondo_juego = pygame.transform.scale(fondo_juego, (WIDTH, HEIGHT))

# Colores que usare en mi proyecto
NEGRO = (0, 0, 0)
BLANCO= (255, 255, 255)
AZUL = (64, 128, 255)

# Importa la función que muestra el menú principal del juego
from scripts.menu import mostrar_menu  

# Cargar imagen del menú completo y ajustarla al tamaño de la ventana
menu_original = pygame.image.load("assets/images/astrox_menu.png").convert()
menu_image = pygame.transform.scale(menu_original, (WIDTH, HEIGHT))

#
def mostrar_menu_derrota(screen, fondo):
    fuente = pygame.font.Font(None, 50)
    texto = fuente.render("Perdiste. ¿Quieres reiniciar?", True, (255, 255, 255))
    reiniciar_texto = fuente.render("Presiona R para Reiniciar", True, (255, 255, 255))
    salir_texto = fuente.render("Presiona ESC para Salir", True, (255, 255, 255))

    while True:
        screen.blit(fondo, (0, 0))
        screen.blit(texto, (WIDTH // 2 - texto.get_width() // 2, HEIGHT // 2 - 80))
        screen.blit(reiniciar_texto, (WIDTH // 2 - reiniciar_texto.get_width() // 2, HEIGHT // 2))
        screen.blit(salir_texto, (WIDTH // 2 - salir_texto.get_width() // 2, HEIGHT // 2 + 60))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return True  # Reiniciar
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()


# Mostrar menú antes de iniciar el juego
mostrar_menu(screen, menu_image)

# Cambiar música: detiene la del menú y reproduce la del juego
pygame.mixer.music.stop()
pygame.mixer.music.load("assets/music/musica_juego.mp3")
pygame.mixer.music.play(-1)  # Se repite durante el juego
pygame.mixer.music.set_volume(0.6)                                   # musica del juego, ajustar volumen


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

# Crear grupo de enemigos
grupo_enemigos = pygame.sprite.Group()

def crear_enemigo():
    x = random.randint(50, WIDTH - 50)
    y = random.randint(-100, -40)
    return EnemigoBasico(x, y, objetivo=nave)


# Agregar enemigos desde arriba   
for i in range(3):                                                          # Cantidad de enemigos
    enemigo = EnemigoBasico(x=100 * i + 50, y=50, objetivo=nave)
    grupo_enemigos.add(enemigo)

from scripts.enemigo_arbol import EnemigoArbol

def crear_enemigo_arbol():
    x = random.randint(50, WIDTH - 50)
    y = random.randint(-100, -40)
    return EnemigoArbol(x, y, nave, WIDTH, HEIGHT)


def crear_meteorito_astar():
    x = random.randint(50, WIDTH - 50)
    y = random.randint(-150, -50)
    return MeteoritoAStar(x, y, nave)


# Crea enemigos con árbol
for _ in range(3):                                                         # Cantidad de enemigos
    grupo_enemigos.add(crear_enemigo_arbol())

# Crea meteorito 
for _ in range(2):  # o 3, dependiendo del nivel de dificultad
    grupo_enemigos.add(crear_meteorito_astar())

contador_meteorito = 0
cooldown_meteorito = 600  # tiempo en frames (300 = 5 segundos si estás a 60 FPS)


# Bucle principal del juego
while True:
    # Manejo de eventos (salir del juego, etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Clic izquierdo
                nave.disparar()
                sonido_disparo.play()

    # Entrada del usuario
    teclas = pygame.key.get_pressed()
    mouse_pos = pygame.mouse.get_pos()

    # =============================
    # Actualizar lógica del juego
    # =============================

    grupo_naves.update(mouse_pos)
    grupo_enemigos.update()

    # Cooldown para aparición de meteoritos A*
    contador_meteorito += 1
    if contador_meteorito >= cooldown_meteorito:                            
        grupo_enemigos.add(crear_meteorito_astar())
        contador_meteorito = 0  # reiniciar contador


    # Verificar si una bala enemiga golpea al jugador
    for enemigo in grupo_enemigos:
        if hasattr(enemigo, "balas"):
            for bala in enemigo.balas:
                if nave.rect.colliderect(bala.rect):
                    print("¡El jugador fue alcanzado por una bala enemiga!")
                    if mostrar_menu_derrota(screen, fondo_juego):
                        os.execl(sys.executable, sys.executable, *sys.argv) 


    # Verificar si una bala del jugador impacta a un enemigo
    for bala in nave.balas:
        enemigo_impactado = pygame.sprite.spritecollideany(bala, grupo_enemigos)
        if enemigo_impactado:
            bala.kill()
            enemigo_impactado.kill()

            # Reponer enemigo del mismo tipo
            if isinstance(enemigo_impactado, EnemigoArbol):
                grupo_enemigos.add(crear_enemigo_arbol())
            else:
                grupo_enemigos.add(crear_enemigo())

    # Colisiones precisas entre jugador y enemigos
    for enemigo in grupo_enemigos:
        distancia = math.hypot(
            enemigo.rect.centerx - nave.rect.centerx,
            enemigo.rect.centery - nave.rect.centery
        )
        if distancia < enemigo.radio_colision + 30:
            offset = (enemigo.rect.left - nave.rect.left, enemigo.rect.top - nave.rect.top)
            mask_enemigo = pygame.mask.from_surface(enemigo.image)

            if nave.mask.overlap(mask_enemigo, offset):
                print("¡Colisión detectada!")
                if mostrar_menu_derrota(screen, fondo_juego):
                    os.execl(sys.executable, sys.executable,*sys.argv)

    # Verificar colisión precisa con meteorito (colisión circular)
    for enemigo in grupo_enemigos:
        if isinstance(enemigo, MeteoritoAStar):
            dx = enemigo.rect.centerx - nave.rect.centerx
            dy = enemigo.rect.centery - nave.rect.centery
            distancia = math.hypot(dx, dy)
            if distancia < enemigo.radio_colision + 30:  # Ajusta el 30 si quieres más precisión
                print("¡Colisión con meteorito!")
                if mostrar_menu_derrota(screen, fondo_juego):
                    os.execl(sys.executable, sys.executable, *sys.argv)
            

    # ====================
    # Dibujar todo
    # ====================
    screen.blit(fondo_juego, (0, 0))           # Fondo
    grupo_naves.draw(screen)                   # Nave
    nave.dibujar_balas(screen)                 # Balas del jugador
    grupo_enemigos.draw(screen)                # Enemigos

    # Dibujar balas de enemigos tipo árbol
    for enemigo in grupo_enemigos:
        if hasattr(enemigo, "balas"):
            enemigo.balas.draw(screen)

    pygame.display.flip()
    clock.tick(60)
