"""Pruebas del TAD Agenda con pytest.

Solo se usa la interfaz publica: Agenda(), len(), contiene, telefono_de,
nombres, agregar y eliminar.

Se ejecutan con: python -m pytest -q
"""

import pytest
from agenda import Agenda


def test_agenda_nueva_esta_vacia():
    """Caso borde: una agenda recien creada no tiene contactos."""
    agenda = Agenda()

    assert len(agenda) == 0
    assert agenda.nombres() == []
    assert agenda.contiene("Ana") is False


def test_buscar_en_agenda_vacia_lanza_keyerror():
    """Caso borde: pedir un telefono en una agenda vacia falla."""
    agenda = Agenda()

    with pytest.raises(KeyError):
        agenda.telefono_de("Ana")


def test_agregar_y_consultar_un_contacto():
    agenda = Agenda()
    agenda.agregar("Ana", "3001112233")

    assert len(agenda) == 1
    assert agenda.contiene("Ana") is True
    assert agenda.telefono_de("Ana") == "3001112233"


def test_los_nombres_quedan_en_orden_alfabetico():
    agenda = Agenda()
    agenda.agregar("Sofia", "3")
    agenda.agregar("Ana", "1")
    agenda.agregar("Pedro", "2")

    assert agenda.nombres() == ["Ana", "Pedro", "Sofia"]


def test_nombre_repetido_actualiza_el_telefono():
    """Caso borde: el mismo nombre dos veces no se duplica."""
    agenda = Agenda()
    agenda.agregar("Ana", "111")
    agenda.agregar("Ana", "222")

    assert len(agenda) == 1
    assert agenda.telefono_de("Ana") == "222"
    assert agenda.nombres() == ["Ana"]


def test_buscar_algo_que_no_esta():
    """Caso borde: un nombre ausente devuelve falso y lanza KeyError."""
    agenda = Agenda()
    agenda.agregar("Ana", "111")
    agenda.agregar("Pedro", "222")

    assert agenda.contiene("Zulma") is False

    with pytest.raises(KeyError):
        agenda.telefono_de("Zulma")


def test_nombre_vacio_lanza_valueerror():
    """Caso borde: no se admite un nombre vacio."""
    agenda = Agenda()

    with pytest.raises(ValueError):
        agenda.agregar("", "111")

    assert len(agenda) == 0


def test_el_telefono_se_guarda_como_texto():
    agenda = Agenda()
    agenda.agregar("Ana", 3001112233)

    telefono = agenda.telefono_de("Ana")

    assert isinstance(telefono, str)
    assert telefono == "3001112233"


def test_eliminar_quita_solo_ese_contacto():
    agenda = Agenda()
    agenda.agregar("Ana", "111")
    agenda.agregar("Pedro", "222")
    agenda.agregar("Sofia", "333")

    agenda.eliminar("Pedro")

    assert len(agenda) == 2
    assert agenda.contiene("Pedro") is False
    assert agenda.nombres() == ["Ana", "Sofia"]


def test_eliminar_algo_que_no_esta_lanza_keyerror():
    """Caso borde: eliminar un nombre ausente falla."""
    agenda = Agenda()
    agenda.agregar("Ana", "111")

    with pytest.raises(KeyError):
        agenda.eliminar("Zulma")

    assert len(agenda) == 1


def test_mayusculas_y_tildes_son_contactos_distintos():
    agenda = Agenda()
    agenda.agregar("ana", "1")
    agenda.agregar("Ana", "2")
    agenda.agregar("Anibal", "3")
    agenda.agregar("Aníbal", "4")

    assert len(agenda) == 4
    assert agenda.telefono_de("ana") == "1"
    assert agenda.telefono_de("Ana") == "2"
    assert agenda.nombres() == ["Ana", "Anibal", "Aníbal", "ana"]


def test_la_lista_de_nombres_es_una_copia():
    agenda = Agenda()
    agenda.agregar("Ana", "111")

    lista = agenda.nombres()
    lista.append("Intruso")

    assert len(agenda) == 1
    assert agenda.nombres() == ["Ana"]


def test_muchos_contactos_se_mantienen_ordenados():
    agenda = Agenda()
    nombres_desordenados = ["pera", "kiwi", "uva", "banano", "mango", "fresa"]

    for posicion, nombre in enumerate(nombres_desordenados):
        agenda.agregar(nombre, str(posicion))

    assert len(agenda) == 6
    assert agenda.nombres() == ["banano", "fresa", "kiwi", "mango", "pera", "uva"]
    assert agenda.telefono_de("uva") == "2"