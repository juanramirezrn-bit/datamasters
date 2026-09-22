import time
from laberinto import Laberinto
from ordenamiento import ordenamiento_burbuja, quicksort

def comparar_tiempos_busqueda(matriz, inicio, fin):
    lab = Laberinto(matriz)
    
    t_inicio = time.time()
    camino_dfs = lab.resolver_dfs(inicio, fin)
    t_dfs = time.time() - t_inicio

    t_inicio = time.time()
    camino_bfs = lab.resolver_bfs(inicio, fin)
    t_bfs = time.time() - t_inicio

    print(f"Tiempo de ejecucion DFS: {t_dfs:.6f} segundos")
    print(f"Tiempo de ejecucion BFS: {t_bfs:.6f} segundos")
    
    return camino_dfs, camino_bfs

def comparar_ordenamiento(datos):
    t_inicio = time.time()
    ordenamiento_burbuja(datos)
    t_burbuja = time.time() - t_inicio

    t_inicio = time.time()
    quicksort(datos)
    t_quicksort = time.time() - t_inicio

    print(f"Burbuja: {t_burbuja:.6f} seg | Quicksort: {t_quicksort:.6f} seg")
