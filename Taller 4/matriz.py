class Matriz:
    """Una matriz guardada en una sola lista, sin listas de listas."""

    def __init__(self, filas: int, columnas: int) -> None:
        """
        Crea una matriz de filas x columnas llena de ceros.

        Si filas o columnas no son positivas, lanza ValueError.

        Complejidad: O(f * c)
        """
        if filas <= 0 or columnas <= 0:
            raise ValueError("filas y columnas deben ser positivas")
        self._filas = filas
        self._columnas = columnas
        self._datos = [0] * (filas * columnas)

    def filas(self) -> int:
        """
        Devuelve cuántas filas tiene la matriz.

        Complejidad: O(1)
        """
        return self._filas

    def columnas(self) -> int:
        """
        Devuelve cuántas columnas tiene la matriz.

        Complejidad: O(1)
        """
        return self._columnas

    def _posicion(self, i: int, j: int) -> int:
        """
        Calcula la posición en la lista plana para la celda (i, j).

        Si la celda está fuera de la matriz, lanza IndexError.

        Complejidad: O(1)
        """
        if i < 0 or i >= self._filas or j < 0 or j >= self._columnas:
            raise IndexError("la celda esta fuera de la matriz")
        return i * self._columnas + j

    def obtener(self, i: int, j: int) -> float:
        """
        Devuelve el valor guardado en la celda (i, j).

        Si la celda está fuera de la matriz, lanza IndexError.

        Complejidad: O(1)
        """
        return self._datos[self._posicion(i, j)]

    def asignar(self, i: int, j: int, valor: float) -> None:
        """
        Escribe un valor en la celda (i, j).

        Si la celda está fuera de la matriz, lanza IndexError.

        Complejidad: O(1)
        """
        self._datos[self._posicion(i, j)] = valor

    def suma(self) -> float:
        """
        Suma todas las celdas de la matriz.

        Complejidad: O(f * c)
        """
        total = 0
        for valor in self._datos:
            total += valor
        return total
