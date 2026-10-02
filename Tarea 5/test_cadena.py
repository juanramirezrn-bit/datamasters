import unittest

from cadena import Cadena, Doble


def cadena_con(datos):
    c = Cadena()
    for d in datos:
        c.agregar(d)
    return c


def doble_con(datos):
    d = Doble()
    for x in datos:
        d.agregar(x)
    return d


def nodos_de(estructura):
    nodos = []
    actual = estructura.primero
    while actual is not None:
        nodos.append(actual)
        actual = actual.siguiente
    return nodos


class PruebasCadena(unittest.TestCase):

    def test_agregar_conserva_el_orden_y_la_longitud(self):
        c = cadena_con([5, 3, 9, 1])
        self.assertEqual(c.a_lista(), [5, 3, 9, 1])
        self.assertEqual(len(c), 4)

    def test_borde_cadena_vacia(self):
        c = Cadena()
        self.assertEqual(len(c), 0)
        self.assertEqual(c.a_lista(), [])
        self.assertIsNone(c.medio_dos_pasadas())
        self.assertIsNone(c.medio())
        c.invertir()
        self.assertEqual(c.a_lista(), [])

    def test_borde_un_solo_nodo(self):
        c = cadena_con(["x"])
        self.assertEqual(c.medio_dos_pasadas(), "x")
        self.assertEqual(c.medio(), "x")
        c.invertir()
        self.assertEqual(c.a_lista(), ["x"])

    def test_medio_con_cantidad_impar(self):
        c = cadena_con([10, 20, 30, 40, 50])
        self.assertEqual(c.medio_dos_pasadas(), 30)
        self.assertEqual(c.medio(), 30)

    def test_medio_con_cantidad_par_es_el_primero_de_los_centrales(self):
        for n in (2, 4, 6, 10):
            c = cadena_con(range(n))
            esperado = (n - 1) // 2
            self.assertEqual(c.medio_dos_pasadas(), esperado)
            self.assertEqual(c.medio(), esperado)

    def test_las_dos_maneras_coinciden_para_todos_los_tamanos(self):
        for n in range(0, 60):
            c = cadena_con(range(n))
            self.assertEqual(c.medio_dos_pasadas(), c.medio())

    def test_invertir_voltea_el_orden(self):
        c = cadena_con([1, 2, 3, 4, 5])
        c.invertir()
        self.assertEqual(c.a_lista(), [5, 4, 3, 2, 1])
        self.assertEqual(len(c), 5)

    def test_agregar_funciona_despues_de_invertir(self):
        c = cadena_con([1, 2, 3])
        c.invertir()
        c.agregar(99)
        self.assertEqual(c.a_lista(), [3, 2, 1, 99])

    def test_invertir_no_crea_nodos_ni_mueve_datos(self):
        c = cadena_con(["a", "b", "c", "d"])
        antes = nodos_de(c)
        c.invertir()
        despues = nodos_de(c)
        self.assertEqual([id(n) for n in despues], [id(n) for n in reversed(antes)])
        self.assertEqual([n.dato for n in antes], ["a", "b", "c", "d"])

    def test_los_datos_no_se_guardan_en_una_estructura_de_python(self):
        c = cadena_con(range(5))
        d = doble_con(range(5))
        for estructura in (c, d):
            for valor in vars(estructura).values():
                self.assertNotIsInstance(valor, (list, tuple, dict, set))

    def test_pasos_medidos_para_1001_nodos(self):
        c = cadena_con(range(1001))
        c.medio_dos_pasadas()
        self.assertEqual(c.ultimos_pasos, 1501)
        c.medio()
        self.assertEqual(c.ultimos_pasos, 1500)


class PruebasDoble(unittest.TestCase):

    def test_agregar_enlaza_en_los_dos_sentidos(self):
        d = doble_con([1, 2, 3, 4])
        self.assertEqual(d.a_lista(), [1, 2, 3, 4])
        self.assertEqual(d.a_lista_al_reves(), [4, 3, 2, 1])
        self.assertEqual(len(d), 4)

    def test_borde_doble_vacia_y_de_un_nodo(self):
        d = Doble()
        self.assertEqual(d.a_lista(), [])
        self.assertEqual(d.a_lista_al_reves(), [])
        d.invertir()
        d.agregar(7)
        d.invertir()
        self.assertEqual(d.a_lista(), [7])
        self.assertEqual(d.a_lista_al_reves(), [7])

    def test_invertir_voltea_y_deja_los_dos_sentidos_coherentes(self):
        d = doble_con([1, 2, 3, 4, 5])
        d.invertir()
        self.assertEqual(d.a_lista(), [5, 4, 3, 2, 1])
        self.assertEqual(d.a_lista_al_reves(), [1, 2, 3, 4, 5])

    def test_agregar_funciona_despues_de_invertir(self):
        d = doble_con([1, 2, 3])
        d.invertir()
        d.agregar(99)
        self.assertEqual(d.a_lista(), [3, 2, 1, 99])
        self.assertEqual(d.a_lista_al_reves(), [99, 1, 2, 3])

    def test_invertir_dos_veces_deja_la_cadena_como_estaba(self):
        d = doble_con(range(6))
        d.invertir()
        d.invertir()
        self.assertEqual(d.a_lista(), [0, 1, 2, 3, 4, 5])
        self.assertEqual(d.a_lista_al_reves(), [5, 4, 3, 2, 1, 0])


if __name__ == "__main__":
    unittest.main()
