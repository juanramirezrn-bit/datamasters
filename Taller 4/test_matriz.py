import pytest
from matriz import Matriz


def test_matriz_nueva_esta_en_ceros():
    m = Matriz(2, 3)
    assert m.obtener(0, 0) == 0
    assert m.obtener(1, 2) == 0


def test_filas_y_columnas():
    m = Matriz(4, 5)
    assert m.filas() == 4
    assert m.columnas() == 5


def test_asignar_y_obtener():
    m = Matriz(3, 3)
    m.asignar(1, 2, 7)
    assert m.obtener(1, 2) == 7
    # las demás celdas siguen en cero
    assert m.obtener(0, 0) == 0


def test_suma():
    m = Matriz(2, 2)
    m.asignar(0, 0, 1)
    m.asignar(0, 1, 2)
    m.asignar(1, 0, 3)
    m.asignar(1, 1, 4)
    assert m.suma() == 10


def test_filas_o_columnas_no_positivas_lanza_error():
    with pytest.raises(ValueError):
        Matriz(0, 3)
    with pytest.raises(ValueError):
        Matriz(3, -1)


def test_matriz_de_una_sola_celda():
    # caso borde: la matriz más pequeña posible
    m = Matriz(1, 1)
    assert m.obtener(0, 0) == 0
    m.asignar(0, 0, 9)
    assert m.obtener(0, 0) == 9
    assert m.suma() == 9


def test_coordenadas_fuera_de_rango():
    # caso borde: acceder fuera de la matriz
    m = Matriz(2, 2)
    with pytest.raises(IndexError):
        m.obtener(2, 0)
    with pytest.raises(IndexError):
        m.asignar(0, 2, 5)
    with pytest.raises(IndexError):
        m.obtener(-1,0)
