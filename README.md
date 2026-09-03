Agenda — Tarea 3
--------------------------------------------------
Agenda es un tipo abstracto de datos que guarda contactos (un nombre y un teléfono cada
uno), los mantiene siempre ordenados por nombre y no admite nombres repetidos. Por
dentro se apoya en dos listas de Python alineadas por posición y la búsqueda binaria está
escrita a mano, así que consultar un contacto cuesta O(log n) mientras agregar o eliminar
cuesta O(n).
El proyecto tiene tres archivos de código, y los tres van en la misma carpeta para que from
agenda import Agenda funcione: agenda.py con la clase y sus siete operaciones,
test_agenda.py con las pruebas de pytest, y medicion.py con el programa que cronometra
las tres agendas de mil, diez mil y cien mil contactos. Se necesita Python 3.9 o superior.
Para usar la agenda se importa la clase y se llaman sus siete operaciones: Agenda(),
len(agenda), contiene(nombre), telefono_de(nombre), nombres(), agregar(nombre,
telefono) y eliminar(nombre).
Las pruebas se ejecutan desde esa misma carpeta con python -m pytest -q. Pytest se instala
una sola vez con pip install pytest.
La medición se corre con python medicion.py, que imprime la tabla de tiempos por consola;
esos tiempos y su interpretación quedaron recogidos en resultados.md. El reparto del
trabajo entre los integrantes está en REPARTO.md.
