from estructuras import Pila, Cola

class Laberinto:
    def __init__(self, matriz):
        self.matriz = matriz
        self.filas = len(matriz)
        self.columnas = len(matriz[0]) if self.filas > 0 else 0

    def resolver_dfs(self, inicio, fin):
        pila = Pila()
        pila.apilar((inicio, [inicio]))
        visitados = set()

        while not pila.esta_vacia():
            pos_actual, camino = pila.desapilar()
            
            if pos_actual == fin:
                return camino

            if pos_actual in visitados:
                continue
            visitados.add(pos_actual)

            r, c = pos_actual
            movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dr, dc in movimientos:
                nr, nc = r + dr, c + dc
                if 0 <= nr < self.filas and 0 <= nc < self.columnas:
                    if self.matriz[nr][nc] != '#' and (nr, nc) not in visitados:
                        pila.apilar(((nr, nc), camino + [(nr, nc)]))

        return None

    def resolver_bfs(self, inicio, fin):
        cola = Cola()
        cola.encolar((inicio, [inicio]))
        visitados = set([inicio])

        while not cola.esta_vacia():
            pos_actual, camino = cola.desencolar()
            
            if pos_actual == fin:
                return camino

            r, c = pos_actual
            movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dr, dc in movimientos:
                nr, nc = r + dr, c + dc
                if 0 <= nr < self.filas and 0 <= nc < self.columnas:
                    if self.matriz[nr][nc] != '#' and (nr, nc) not in visitados:
                        visitados.add((nr, nc))
                        cola.encolar(((nr, nc), camino + [(nr, nc)]))

        return None
