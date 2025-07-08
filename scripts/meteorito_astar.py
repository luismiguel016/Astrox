# scripts/meteorito_astar.py
# Nombre: Luis Miguel Montesino Cedeño
# Matrícula: 15-EISN-2-052

import pygame
import math
import heapq

# Constante: tamaño del grid en píxeles (para convertir coordenadas de pantalla a celdas)
TAMANO_CELDA = 40

# ============================
# CLASE: Nodo del mapa (grid)
# ============================
class NodoMapa:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        # Compara si dos nodos tienen la misma posición
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        # Permite usar el nodo en conjuntos y diccionarios
        return hash((self.x, self.y))

    def vecinos(self):
        # Retorna los vecinos (arriba, abajo, izquierda, derecha)
        movimientos = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        return [NodoMapa(self.x + dx, self.y + dy) for dx, dy in movimientos]

    def Costo(self, objetivo):
        # Heurística de A*: distancia Manhattan entre este nodo y el objetivo
        return abs(self.x - objetivo.x) + abs(self.y - objetivo.y)

# ============================
# CLASE: Nodo usado por A*
# ============================
class NodoAStar:
    def __init__(self, dato, padre, costo):
        self.dato = dato      # Nodo del mapa
        self.padre = padre    # Nodo anterior (para reconstruir el camino)
        self.costo = costo    # Costo total (g + h)

    def __lt__(self, other):
        # Permite ordenar nodos por su costo en la cola de prioridad
        return self.costo < other.costo

# ============================
# FUNCIÓN: Algoritmo A*
# ============================
def Astar(inicio, objetivo):
    """
    Implementación de A* sobre un grid.
    Retorna el camino desde 'inicio' hasta 'objetivo'.
    """
    abiertos = []  # Cola de prioridad de nodos a visitar
    visitados = set()  # Conjunto de nodos ya visitados

    nodo_inicio = NodoAStar(inicio, None, inicio.Costo(objetivo))
    heapq.heappush(abiertos, nodo_inicio)

    while abiertos:
        actual = heapq.heappop(abiertos)

        if actual.dato == objetivo:
            # Si llegamos al objetivo, reconstruimos el camino
            camino = []
            while actual:
                camino.append(actual.dato)
                actual = actual.padre
            camino.reverse()
            return camino

        visitados.add(actual.dato)

        # Explorar vecinos
        for vecino in actual.dato.vecinos():
            if vecino in visitados:
                continue
            nodo = NodoAStar(vecino, actual, vecino.Costo(objetivo))
            heapq.heappush(abiertos, nodo)

    return []  # No se encontró camino

# ============================
# CLASE: Meteorito con A*
# ============================
class MeteoritoAStar(pygame.sprite.Sprite):
    def __init__(self, x, y, objetivo):
        super().__init__()

        # Cargar y escalar imagen
        self.image = pygame.image.load("assets/images/meteorito_star.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect(center=(x, y))

        # Datos de IA
        self.objetivo = objetivo
        self.velocidad = 2
        self.radio_colision = 25  # Para colisión circular

        # Posición en el grid
        self.grid_x = self.rect.centerx // TAMANO_CELDA
        self.grid_y = self.rect.centery // TAMANO_CELDA

        # Ruta a seguir
        self.camino = []
        self.paso_actual = 0

        # Calcular primer camino
        self.recalcular_camino()

    def recalcular_camino(self):
        """
        Convierte las coordenadas del meteorito y del jugador al grid
        y recalcula el camino usando A*.
        """
        inicio = NodoMapa(self.rect.centerx // TAMANO_CELDA, self.rect.centery // TAMANO_CELDA)
        destino = NodoMapa(self.objetivo.rect.centerx // TAMANO_CELDA, self.objetivo.rect.centery // TAMANO_CELDA)
        self.camino = Astar(inicio, destino)
        self.paso_actual = 0

    def update(self):
        """
        Mueve el meteorito a lo largo del camino calculado por A*.
        Si termina el camino, recalcula uno nuevo.
        """
        if self.paso_actual < len(self.camino):
            nodo = self.camino[self.paso_actual]
            objetivo_px = (nodo.x * TAMANO_CELDA + TAMANO_CELDA // 2,
                           nodo.y * TAMANO_CELDA + TAMANO_CELDA // 2)

            dx = objetivo_px[0] - self.rect.centerx
            dy = objetivo_px[1] - self.rect.centery
            distancia = math.hypot(dx, dy)

            if distancia < self.velocidad:
                # Si llegó al nodo, pasa al siguiente
                self.rect.center = objetivo_px
                self.paso_actual += 1
            else:
                # Movimiento hacia el siguiente nodo
                dx /= distancia
                dy /= distancia
                self.rect.centerx += dx * self.velocidad
                self.rect.centery += dy * self.velocidad
        else:
            # Si terminó el camino, recalcula otro
            self.recalcular_camino()

    def get_mask(self):
        """
        Devuelve la máscara de colisión del meteorito
        (para colisiones pixel-perfect si se desea).
        """
        return pygame.mask.from_surface(self.image)

