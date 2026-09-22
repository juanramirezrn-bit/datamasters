
class ArregloDinamico:
    def __init__(self, capacidad_inicial=10):
        self.capacidad = capacidad_inicial
        self.tamano = 0
        self.datos = [None] * self.capacidad

    def agregar(self, elemento):
        if self.tamano == self.capacidad:
            self._redimensionar()
        self.datos[self.tamano] = elemento
        self.tamano += 1

    def _redimensionar(self):
        nueva_capacidad = self.capacidad * 2
        nuevos_datos = [None] * nueva_capacidad
        for i in range(self.tamano):
            nuevos_datos[i] = self.datos[i]
        self.datos = nuevos_datos
        self.capacidad = nueva_capacidad

    def obtener(self, indice):
        if 0 <= indice < self.tamano:
            return self.datos[indice]
        raise IndexError("El indice esta fuera del rango valido")

    def __len__(self):
        return self.tamano
