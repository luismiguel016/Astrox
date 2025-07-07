# scripts/meteorito_astar.py
# Nombre: Luis Miguel Montesino Cedeño
# Matrícula: 15-EISN-2-052

import pygame
import math
import heapq

TAMANO_CELDA = 40  # tamaño de las celdas del grid

class NodoMapa:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def vecinos(self):
        movimientos = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        return [NodoMapa(self.x + dx, self.y + dy) for dx, dy in movimientos]

    def Costo(self, objetivo):
        # Usamos distancia Manhattan
        return abs(self.x - objetivo.x) + abs(self.y - objetivo.y)

class NodoAStar:
    def __init__(self, dato, padre, costo):
        self.dato = dato
        self.padre = padre
        self.costo = costo

    def __lt__(self, other):
        return self.costo < other.costo

# Funcion 

def Astar(inicio, objetivo):
    abiertos = []
    visitados = set()
    nodo_inicio = NodoAStar(inicio, None, inicio.Costo(objetivo))
    heapq.heappush(abiertos, nodo_inicio)

    while abiertos:
        actual = heapq.heappop(abiertos)

        if actual.dato == objetivo:
            camino = []
            while actual:
                camino.append(actual.dato)
                actual = actual.padre
            camino.reverse()
            return camino

        visitados.add(actual.dato)

        for vecino in actual.dato.vecinos():
            if vecino in visitados:
                continue
            nodo = NodoAStar(vecino, actual, vecino.Costo(objetivo))
            heapq.heappush(abiertos, nodo)

    return []  # no se encontró camino

class MeteoritoAStar(pygame.sprite.Sprite):
    def __init__(self, x, y, objetivo):
        super().__init__()
        self.image = pygame.image.load("assets/images/meteorito_star.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect(center=(x, y))
        
        self.objetivo = objetivo
        self.velocidad = 2
        self.radio_colision = 25  # para colisión circular

        self.grid_x = self.rect.centerx // TAMANO_CELDA
        self.grid_y = self.rect.centery // TAMANO_CELDA

        self.camino = []
        self.paso_actual = 0
        self.recalcular_camino()

    def recalcular_camino(self):
        inicio = NodoMapa(self.rect.centerx // TAMANO_CELDA, self.rect.centery // TAMANO_CELDA)
        destino = NodoMapa(self.objetivo.rect.centerx // TAMANO_CELDA, self.objetivo.rect.centery // TAMANO_CELDA)
        self.camino = Astar(inicio, destino)
        self.paso_actual = 0

    def update(self):
        if self.paso_actual < len(self.camino):
            nodo = self.camino[self.paso_actual]
            objetivo_px = (nodo.x * TAMANO_CELDA + TAMANO_CELDA // 2, nodo.y * TAMANO_CELDA + TAMANO_CELDA // 2)
            dx = objetivo_px[0] - self.rect.centerx
            dy = objetivo_px[1] - self.rect.centery
            distancia = math.hypot(dx, dy)

            if distancia < self.velocidad:
                self.rect.center = objetivo_px
                self.paso_actual += 1
            else:
                dx /= distancia
                dy /= distancia
                self.rect.centerx += dx * self.velocidad
                self.rect.centery += dy * self.velocidad
        else:
            self.recalcular_camino()

    def get_mask(self):
        return pygame.mask.from_surface(self.image)
