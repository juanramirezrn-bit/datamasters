from laberinto import Laberinto
from cargador_datos import generar_laberinto_aleatorio
from pruebas_rendimiento import comparar_tiempos_busqueda

def mostrar_laberinto(matriz, camino=None):
    copia = [fila.copy() for fila in matriz]
    if camino:
        for r, c in camino:
            if copia[r][c] not in ['S', 'E']:
                copia[r][c] = '.'
    for fila in copia:
        print("".join(fila))

def main():
    print("========================================")
    print("   PROYECTO FINAL - RESOLVER LABERINTO ")
    print("========================================")
    
    #
    filas = 15
    columnas = 30
    
    laberinto_demo = generar_laberinto_aleatorio(filas, columnas, densidad_paredes=0.20)

    inicio = (1, 1)
    fin = (filas - 2, columnas - 2)

    print(f"\n[+] Laberinto aleatorio generado ({filas}x{columnas}):")
    mostrar_laberinto(laberinto_demo)

    print("\n[+] Ejecutando busqueda de caminos...")
    camino_dfs, camino_bfs = comparar_tiempos_busqueda(laberinto_demo, inicio, fin)

    print("\n[+] Resultado usando BFS (camino mas corto):")
    if camino_bfs:
        mostrar_laberinto(laberinto_demo, camino_bfs)
    else:
        print("No se encontro un camino valido (las paredes bloqueron el paso).")

if __name__ == '__main__':
    main()