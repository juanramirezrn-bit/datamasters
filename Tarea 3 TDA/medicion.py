import platform
import random
import string
import time
from typing import Callable, List

from agenda import Agenda

random.seed(11)

TAMANOS: List[int] = [1_000, 10_000, 100_000]
LARGO_NOMBRE: int = 10
REPETICIONES: int = 7
NOMBRE_AL_PRINCIPIO: str = "A" * LARGO_NOMBRE
TELEFONO_DE_PRUEBA: str = "3000000000"


def nombre_aleatorio(longitud: int = LARGO_NOMBRE) -> str:
    return "".join(random.choice(string.ascii_lowercase) for _ in range(longitud))


def construir_agenda(tamano: int) -> Agenda:
    agenda = Agenda()
    while len(agenda) < tamano:
        nombre = nombre_aleatorio()
        if agenda.contiene(nombre):
            continue
        telefono = "".join(random.choice(string.digits) for _ in range(10))
        agenda.agregar(nombre, telefono)
    return agenda


def nombre_ausente(agenda: Agenda) -> str:
    while True:
        nombre = nombre_aleatorio()
        if not agenda.contiene(nombre):
            return nombre


def buscar_lineal(nombres: List[str], objetivo: str) -> bool:
    for nombre in nombres:
        if nombre == objetivo:
            return True
    return False


def mejor_tiempo(funcion: Callable[[], None], repeticiones: int = REPETICIONES) -> float:
    mejor = float("inf")
    for _ in range(repeticiones):
        inicio = time.perf_counter()
        funcion()
        fin = time.perf_counter()
        transcurrido = fin - inicio
        if transcurrido < mejor:
            mejor = transcurrido
    return mejor


def medir_busqueda_binaria(agenda: Agenda, objetivo: str) -> float:
    return mejor_tiempo(lambda: agenda.contiene(objetivo))


def medir_busqueda_lineal(nombres: List[str], objetivo: str) -> float:
    return mejor_tiempo(lambda: buscar_lineal(nombres, objetivo))


def medir_agregar_eliminar(agenda: Agenda) -> float:
    def agregar_y_eliminar() -> None:
        agenda.agregar(NOMBRE_AL_PRINCIPIO, TELEFONO_DE_PRUEBA)
        agenda.eliminar(NOMBRE_AL_PRINCIPIO)
    return mejor_tiempo(agregar_y_eliminar)


def formato_entero(numero: int) -> str:
    return f"{numero:,}".replace(",", ".")


def formato_microsegundos(segundos: float) -> str:
    microsegundos = segundos * 1_000_000
    return f"{microsegundos:.2f}".replace(".", ",")


def main() -> None:
    print(f"Python: {platform.python_version()}  |  Maquina: {platform.platform()}")
    print()
    encabezado = f"{'Contactos':>12} | {'contiene (bin)':>16} | {'lineal':>16} | {'agregar+eliminar':>18}"
    print(encabezado)
    print("-" * len(encabezado))

    filas = []
    for tamano in TAMANOS:
        agenda = construir_agenda(tamano)
        nombres = agenda.nombres()
        objetivo = nombre_ausente(agenda)

        t_binaria = medir_busqueda_binaria(agenda, objetivo)
        t_lineal = medir_busqueda_lineal(nombres, objetivo)
        t_agregar = medir_agregar_eliminar(agenda)

        filas.append((tamano, t_binaria, t_lineal, t_agregar))

        fila_texto = (
            f"{formato_entero(tamano):>12} | "
            f"{formato_microsegundos(t_binaria) + ' us':>16} | "
            f"{formato_microsegundos(t_lineal) + ' us':>16} | "
            f"{formato_microsegundos(t_agregar) + ' us':>18}"
        )
        print(fila_texto)

    print()
    if len(filas) >= 3:
        _, b10k, l10k, a10k = filas[1]
        _, b100k, l100k, a100k = filas[2]
        print("Al pasar de 10.000 a 100.000 contactos:")
        print(f"  contiene (binaria) se multiplico por {b100k / b10k:.2f}")
        print(f"  busqueda lineal    se multiplico por {l100k / l10k:.2f}")
        print(f"  agregar+eliminar   se multiplico por {a100k / a10k:.2f}")


if __name__ == "__main__":
    main()
