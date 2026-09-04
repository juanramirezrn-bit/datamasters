from typing import List


class Agenda:

    def _init_(self):
        self._nombres: List[str] = []
        self._telefonos: List[str] = []

    def _len_(self):
        return len(self._nombres)

    def _posicion_de(self, nombre: str):
        izquierda = 0
        derecha = len(self._nombres) - 1

        while izquierda <= derecha:
            medio = (izquierda + derecha) // 2
            nombre_del_medio = self._nombres[medio]

            if nombre_del_medio == nombre:
                return medio
            if nombre_del_medio < nombre:
                izquierda = medio + 1
            else:
                derecha = medio - 1

        return izquierda

    def _existe_en(self, posicion: int, nombre: str):
        if posicion < 0 or posicion >= len(self._nombres):
            return False
        return self._nombres[posicion] == nombre

    def contiene(self, nombre: str):
        posicion = self._posicion_de(nombre)
        return self._existe_en(posicion, nombre)

    def telefono_de(self, nombre: str):
        posicion = self._posicion_de(nombre)
        if not self._existe_en(posicion, nombre):
            raise KeyError(nombre)
        return self._telefonos[posicion]

    def nombres(self):
        copia: List[str] = []
        for nombre in self._nombres:
            copia.append(nombre)
        return copia

    def agregar(self, nombre: str, telefono: str):
        if nombre == "":
            raise ValueError("El nombre no puede estar vacio")

        telefono_como_texto = str(telefono)
        posicion = self._posicion_de(nombre)

        if self._existe_en(posicion, nombre):
            self._telefonos[posicion] = telefono_como_texto
            return

        self._nombres.insert(posicion, nombre)
        self._telefonos.insert(posicion, telefono_como_texto)

    def eliminar(self, nombre: str):
        posicion = self._posicion_de(nombre)
        if not self._existe_en(posicion, nombre):
            raise KeyError(nombre)

        self._nombres.pop(posicion)
        self._telefonos.pop(posicion)
