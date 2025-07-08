# Proyecto-parcial-IA

## Nombre: Luis Miguel montesino

## Matrícula: 15-EISN-2-052

## Proyecto: Astrox juego inspierado en Devil Zone

# ASTROX 

**Autor:** Mi Persona

## 🎮 Descripción


**Astrox** es un juego de naves espaciales con un estilo retro, una obra que nace tras días de profunda reflexión, meditación técnica y búsquedas existenciales en el universo de la inteligencia artificial...

Bueno, en realidad: el profesor me lo asignó.

Inspirado en el clásico Devil Zone (juego también asignado), Astrox nos lanza a una guerra intergaláctica donde el jugador debe eliminar enemigos.
⠀
Controlamos la nave con el mouse y disparamos con el clic izquierdo. Cada uno de los enemigos presenta un comportamiento distinto gracias a la implementación de **algoritmos A* y árboles de comportamiento**.
⠀
Aunque aún sigue en desarrollo, ya cuenta con **IA funcional, música, sonido, colisiones precisas, menú de reinicio y mucha dedicación... obligatoria.**


## 🧠 Inteligencia Artificial

### 🔹 Algoritmo A*
Utilizado por los enemigos tipo `MeteoritoAStar`, que calculan la ruta más corta hasta el jugador simulando inteligencia de persecución.

### 🔹 Árbol de Comportamiento
Utilizado por enemigos intermedios (`EnemigoArbol`) que esquivan balas y disparan desde la distancia. El árbol evalúa condiciones y ejecuta acciones según el estado del jugador.

---

## 🕹️ Controles
Solo el mouse **Profesor usar control hace injugable este juego de Precision**

## 🧪 Cómo ejecutar el juego

1. Asegúrate de tener Python instalado.
2. Instala las dependencias ejecutando:
pip install -r requirements.txt
3. Corre el juego con:
python main.py


## 🎵 Recursos y multimedia

- Música retro para el menú y el gameplay.
- Sonido de disparo personalizado.
- Sprites generados con estilo retro (IA + edición manual).

---

## 📁 Estructura del Proyecto

ASTROX/
│── main.py
├── scripts/
│ ├── arbol_comportamiento.py
│ ├── bala_enemiga.py
│ ├── bala.py
│ ├── enemigo_arbol.py
│ ├── enemigo_basico.py
│ ├── jugador.py
│ ├── menu.py
│ └── meteorito_astar.py
├── assets/
│ ├── images/
│ ├── sounds/
│ └── music/
├── requirements.txt
├── README.md
├── .gitignore

## 🗃️ Repositorio del Proyecto
https://github.com/luismiguel016/Astrox