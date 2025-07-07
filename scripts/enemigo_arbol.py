
# scripts/enemigo_arbol.py
# Nombre: Luis Miguel Montesino Cedeño
# Matrícula: 15-EISN-2-052

import pygame
import random
import math
from scripts.bala_enemiga import BalaEnemiga
from scripts.arbol_comportamiento import Nodo, Selector, Secuencia, Accion, Invertir
 
 # Arbol de COMPORTAMIENTOOOOO

class EnemigoArbol(pygame.sprite.Sprite):
    def __init__(self, x, y, objetivo, width, heigth):
        super().__init__()
        self.WIDTH = width
        self.HEIGHT = heigth

        self.image = pygame.image.load("assets/images/enemigo_arbol.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect(midbottom=(x, y))

        self.objetivo = objetivo
        self.velocidad = 2
        self.rango_vision = 300  # Distancia a la que cambia de comportamiento
        self.rango_colision = 80  # Para persecución
        self.direccion_patrulla = random.choice([(1, 0), (-1, 0), (0, 1), (0, -1)])
        self.contador_patrulla = 0

        self.construir_arbol()

        self.balas = pygame.sprite.Group()
        self.cooldown_disparo = 60  # Cada cuanto segundo dispara
        self.contador_disparo = 0

        self.radio_colision = 30



    def construir_arbol(self):
        self.comportamiento = Selector()

        # Rama: jugador lejos → disparar
        secuencia_disparo = Secuencia()
        secuencia_disparo.agregar_hijo(Accion(self.jugador_lejos))
        secuencia_disparo.agregar_hijo(Accion(self.disparar))  # aun no dispara, solo print

        # Rama: jugador cerca → perseguir
        secuencia_perseguir = Secuencia()
        secuencia_perseguir.agregar_hijo(Accion(self.jugador_cerca))
        secuencia_perseguir.agregar_hijo(Accion(self.perseguir))

        # Rama: patrullar
        accion_patrulla = Accion(self.patrullar)

        self.comportamiento.agregar_hijo(secuencia_disparo)
        self.comportamiento.agregar_hijo(secuencia_perseguir)
        self.comportamiento.agregar_hijo(accion_patrulla)

    def mantener_en_pantalla(self):
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > self.WIDTH:
            self.rect.right = self.WIDTH
        if self.rect.top < -150:
            self.rect.top = -150
        if self.rect.bottom > self.HEIGHT:
            self.rect.bottom = self.HEIGHT

    
    def update(self):
        self.Actualizar()
        self.balas.update()
        self.mantener_en_pantalla()  # ← Agregado

    def Actualizar(self):
        self.comportamiento.ejecutar()

    # ===== CONDICIONES =====

    def jugador_cerca(self):
        return self.distancia_a_jugador() < self.rango_colision

    def jugador_lejos(self):
        return self.distancia_a_jugador() >= self.rango_colision

    def distancia_a_jugador(self):
        dx = self.objetivo.rect.centerx - self.rect.centerx
        dy = self.objetivo.rect.centery - self.rect.centery
        return math.hypot(dx, dy)

    # ===== ACCIONES =====

    def perseguir(self):
        dx = self.objetivo.rect.centerx - self.rect.centerx
        dy = self.objetivo.rect.centery - self.rect.centery
        distancia = math.hypot(dx, dy)
        if distancia != 0:
            dx /= distancia
            dy /= distancia
        self.rect.x += dx * self.velocidad
        self.rect.y += dy * self.velocidad
        return True

    def patrullar(self):
        if self.contador_patrulla <= 0:
            self.direccion_patrulla = random.choice([(1, 0), (-1, 0), (0, 1), (0, -1)])
            self.contador_patrulla = 60  # duración en frames

        dx, dy = self.direccion_patrulla
        self.rect.x += dx * self.velocidad
        self.rect.y += dy * self.velocidad
        self.contador_patrulla -= 1
        return True

    def disparar(self):
        if self.contador_disparo <= 0:
         bala = BalaEnemiga(self.rect.centerx, self.rect.bottom, self.objetivo)
         self.balas.add(bala)
         self.contador_disparo = self.cooldown_disparo
         return True
        else:
         self.contador_disparo -= 1
         return False
