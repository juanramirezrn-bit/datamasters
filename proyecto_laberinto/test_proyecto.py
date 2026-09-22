import unittest
from estructuras import Pila, Cola
from laberinto import Laberinto

class PruebasProyecto(unittest.TestCase):

    def test_pila_apilar_y_desapilar(self):
        pila = Pila()
        pila.apilar(10)
        pila.apilar(20)
        self.assertEqual(pila.desapilar(), 20)
        self.assertEqual(pila.desapilar(), 10)

    def test_cola_encolar_y_desencolar(self):
        cola = Cola()
        cola.encolar("A")
        cola.encolar("B")
        self.assertEqual(cola.desencolar(), "A")

    def test_resolver_laberinto_simple(self):
        matriz = [
            ['S', ' '],
            ['#', 'E']
        ]
        lab = Laberinto(matriz)
        camino = lab.resolver_bfs((0, 0), (1, 1))
        self.assertIsNotNone(camino)

if __name__ == '__main__':
    unittest.main()
