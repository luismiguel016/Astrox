# scripts/arbol_comportamiento.py
# Nombre: Luis Miguel Montesino Cedeño
# Matrícula: 15-EISN-2-052

# ============================
# NODO BASE DEL ÁRBOL
# ============================
class Nodo:
    def __init__(self):
        self.hijos = []  # Lista de nodos hijos

    def agregar_hijo(self, hijo):
        """Agrega un hijo al nodo."""
        self.hijos.append(hijo)

    def ejecutar(self):
        """Método base a sobreescribir."""
        pass


# ============================
# SELECTOR: Ejecuta hasta que uno tenga éxito
# ============================
class Selector(Nodo):
    def ejecutar(self):
        """
        Devuelve True si alguno de sus hijos tiene éxito.
        Ideal para decisiones tipo: '¿puedo hacer esto? sino haz esto otro'.
        """
        for hijo in self.hijos:
            if hijo.ejecutar():  # Si un hijo devuelve True, el selector tiene éxito
                return True
        return False  # Si ninguno funciona, el selector falla


# ============================
# SECUENCIA: Todos deben tener éxito
# ============================
class Secuencia(Nodo):
    def ejecutar(self):
        """
        Ejecuta todos sus hijos en orden. Si uno falla, la secuencia falla.
        Ideal para tareas encadenadas como: 'acércate, apunta, dispara'.
        """
        for hijo in self.hijos:
            if not hijo.ejecutar():  # Si uno falla, la secuencia falla
                return False
        return True  # Si todos tienen éxito, retorna True


# ============================
# ACCIÓN: Nodo hoja que ejecuta una función
# ============================
class Accion(Nodo):
    def __init__(self, accion):
        super().__init__()
        self.accion = accion  # Recibe una función como acción

    def ejecutar(self):
        """
        Ejecuta directamente la función que se pasó como acción.
        Debe retornar True o False según el éxito de la acción.
        """
        return self.accion()


# ============================
# INVERTIR: Invierte el resultado de su hijo
# ============================
class Invertir(Nodo):
    def __init__(self, accion):
        super().__init__()
        self.agregar_hijo(accion)

    def ejecutar(self):
        """
        Invierte el resultado de su único hijo.
        Si el hijo devuelve True, retorna False (y viceversa).
        Útil para condiciones negativas como 'si NO ve al jugador'.
        """
        return not self.hijos[0].ejecutar()


# ============================
# TIMER: Ejecuta su hijo cada cierto tiempo
# ============================
class Timer(Nodo):
    def __init__(self, tiempo):
        super().__init__()
        self.tiempo = tiempo  # Tiempo de espera entre ejecuciones
        self.tiempo_restante = tiempo  # Contador interno

    def ejecutar(self):
        """
        Espera una cantidad de tiempo antes de ejecutar su hijo.
        Solo ejecuta cuando el contador llega a 0, luego se reinicia.
        Útil para disparos con cooldown, etc.
        """
        if self.tiempo_restante > 0:
            self.tiempo_restante -= 1
            return False  # Aún no es tiempo de ejecutar
        else:
            self.tiempo_restante = self.tiempo  # Reinicia el contador
            self.hijos[0].ejecutar()  # Ejecuta el hijo
            return True
