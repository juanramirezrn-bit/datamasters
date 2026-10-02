class NodoSencillo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class NodoDoble:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None


class Cadena:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self._cantidad = 0
        self.ultimos_pasos = 0

    def agregar(self, dato):
        nodo = NodoSencillo(dato)
        if self.ultimo is None:
            self.primero = nodo
        else:
            self.ultimo.siguiente = nodo
        self.ultimo = nodo
        self._cantidad += 1

    def __len__(self):
        return self._cantidad

    def a_lista(self):
        datos = []
        actual = self.primero
        while actual is not None:
            datos.append(actual.dato)
            actual = actual.siguiente
        return datos

    def medio_dos_pasadas(self):
        pasos = 0
        n = 0
        actual = self.primero
        while actual is not None:
            n += 1
            actual = actual.siguiente
            pasos += 1

        if n == 0:
            self.ultimos_pasos = pasos
            return None

        actual = self.primero
        for _ in range((n - 1) // 2):
            actual = actual.siguiente
            pasos += 1

        self.ultimos_pasos = pasos
        return actual.dato

    def medio(self):
        pasos = 0
        tortuga = self.primero
        liebre = self.primero

        while liebre is not None and liebre.siguiente is not None \
                and liebre.siguiente.siguiente is not None:
            tortuga = tortuga.siguiente
            liebre = liebre.siguiente.siguiente
            pasos += 3

        self.ultimos_pasos = pasos
        if tortuga is None:
            return None
        return tortuga.dato

    def invertir(self):
        anterior = None
        actual = self.primero
        nuevo_ultimo = self.primero
        while actual is not None:
            siguiente = actual.siguiente
            actual.siguiente = anterior
            anterior = actual
            actual = siguiente
        self.primero = anterior
        self.ultimo = nuevo_ultimo


class Doble:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self._cantidad = 0

    def agregar(self, dato):
        nodo = NodoDoble(dato)
        if self.ultimo is None:
            self.primero = nodo
        else:
            nodo.anterior = self.ultimo
            self.ultimo.siguiente = nodo
        self.ultimo = nodo
        self._cantidad += 1

    def __len__(self):
        return self._cantidad

    def a_lista(self):
        datos = []
        actual = self.primero
        while actual is not None:
            datos.append(actual.dato)
            actual = actual.siguiente
        return datos

    def a_lista_al_reves(self):
        datos = []
        actual = self.ultimo
        while actual is not None:
            datos.append(actual.dato)
            actual = actual.anterior
        return datos

    def invertir(self):
        actual = self.primero
        while actual is not None:
            actual.siguiente, actual.anterior = actual.anterior, actual.siguiente
            actual = actual.anterior
        self.primero, self.ultimo = self.ultimo, self.primero


if __name__ == "__main__":
    def con_puntos(numero):
        return f"{numero:,}".replace(",", ".")

    print(f"{'n (nodos)':>10} {'Dos pasadas':>12} {'Liebre y tortuga':>17}")
    for n in (1001, 10001, 100001):
        cadena = Cadena()
        for i in range(n):
            cadena.agregar(i)

        dato_a = cadena.medio_dos_pasadas()
        pasos_a = cadena.ultimos_pasos
        dato_b = cadena.medio()
        pasos_b = cadena.ultimos_pasos

        assert dato_a == dato_b == (n - 1) // 2
        print(f"{con_puntos(n):>10} {con_puntos(pasos_a):>12} "
              f"{con_puntos(pasos_b):>17}")
