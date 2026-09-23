import random
import timeit
from matriz import Matriz


random.seed(11)


def llenar_matriz(lado: int) -> Matriz:
    m = Matriz(lado, lado)
    for i in range(lado):
        for j in range(lado):
            m.asignar(i, j, random.randint(0, 9))
    return m


def medir_suma(m: Matriz) -> float:
    # se cronometra solo suma(), la matriz ya está llena
    tiempos = timeit.repeat(lambda: m.suma(), number=1, repeat=5)
    return min(tiempos)


def main() -> None:
    lados = [250, 500, 1000]
    resultados = []

    for lado in lados:
        m = llenar_matriz(lado)
        tiempo = medir_suma(m)
        celdas = lado * lado
        resultados.append((lado, celdas, tiempo))

    print("lado\tceldas\ttiempo(s)\tfactor")
    tiempo_anterior = None
    for lado, celdas, tiempo in resultados:
        if tiempo_anterior is None:
            factor = "-"
        else:
            factor = f"{tiempo / tiempo_anterior:.2f}"
        print(f"{lado}\t{celdas}\t{tiempo:.4f}\t{factor}")
        tiempo_anterior = tiempo


if __name__ == "__main__":
    main()
