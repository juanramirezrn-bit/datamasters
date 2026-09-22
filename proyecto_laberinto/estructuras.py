
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class Pila:
    def __init__(self):
        self.cabeza = None
        self.tamano = 0

    def apilar(self, valor):
        nuevo_nodo = Nodo(valor)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo
        self.tamano += 1

    def desapilar(self):
        if self.esta_vacia():
            return None
        valor = self.cabeza.valor
        self.cabeza = self.cabeza.siguiente
        self.tamano -= 1
        return valor

    def esta_vacia(self):
        return self.tamano == 0

class Cola:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.tamano = 0

    def encolar(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.esta_vacia():
            self.primero = nuevo_nodo
            self.ultimo = nuevo_nodo
        else:
            self.ultimo.siguiente = nuevo_nodo
            self.ultimo = nuevo_nodo
        self.tamano += 1

    def desencolar(self):
        if self.esta_vacia():
            return None
        valor = self.primero.valor
        self.primero = self.primero.siguiente
        if self.primero is None:
            self.ultimo = None
        self.tamano -= 1
        return valor

    def esta_vacia(self):
        return self.tamano == 0
