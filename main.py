# main.py
# Nombre: Luis Miguel Montesino Cedeño
# Matrícula: 15-EISN-2-052
# Archivo Principal del Juego

import pygame
import sys
import random
import math
from scripts.enemigo_basico import EnemigoBasico


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

# Crear grupo de enemigos
grupo_enemigos = pygame.sprite.Group()

def crear_enemigo():
    x = random.randint(50, WIDTH - 50)
    y = random.randint(-100, -40)
    return EnemigoBasico(x, y, objetivo=nave)


# Agregar enemigos desde arriba
for i in range(5):
    enemigo = EnemigoBasico(x=100 * i + 50, y=50, objetivo=nave)
    grupo_enemigos.add(enemigo)

# Bucle principal del juego

while True:
    # Manejo de eventos (salir del juego, etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
    # Disparo con clic izquierdo del mouse
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # 1 = botón izquierdo
                nave.disparar()

    # Entrada del usuario (posiciones de teclado y mouse)
    teclas = pygame.key.get_pressed()
    mouse_pos = pygame.mouse.get_pos()

    # =============================
    # Actualizar lógica del juego
    # =============================

    # Actualizar la nave y los enemigos
    grupo_naves.update(mouse_pos)
    grupo_enemigos.update()

   # Verificar colisiones: una bala solo destruye un enemigo
    for bala in nave.balas:
     enemigo_impactado = pygame.sprite.spritecollideany(bala, grupo_enemigos)
     if enemigo_impactado:
         bala.kill()  # Eliminar la bala si impacta
         enemigo_impactado.kill()     # Eliminar el enemigo
         nuevo = crear_enemigo()     # Crear uno nuevo
         grupo_enemigos.add(nuevo)   # Agregarlo al grupo

    # Verificar colisión precisa entre la nave y cada enemigo
    for enemigo in grupo_enemigos:
        distancia = math.hypot(
          enemigo.rect.centerx - nave.rect.centerx,
          enemigo.rect.centery - nave.rect.centery
    )

        if distancia < enemigo.radio_colision + 30:  # Ajusta el 30 si necesitas
            offset = (enemigo.rect.left - nave.rect.left, enemigo.rect.top - nave.rect.top)
            mask_enemigo = pygame.mask.from_surface(enemigo.image)
 
            if nave.mask.overlap(mask_enemigo, offset):
              print("¡Colisión real detectada!")
              pygame.quit()
              sys.exit()
    
    # Dibujar fondo, nave y balas
    screen.fill(NEGRO)
    grupo_naves.draw(screen)
    nave.dibujar_balas(screen)  # Mostrar las balas disparadas
    grupo_enemigos.draw(screen)

    # Actualizar pantalla
    pygame.display.flip()
    clock.tick(60)  # Limitar a 60 FPS


