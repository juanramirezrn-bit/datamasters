import csv
import random

def cargar_laberinto_desde_archivo(ruta_archivo):
    matriz = []
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            for linea in archivo:
                fila = list(linea.strip())
                if fila:
                    matriz.append(fila)
    except FileNotFoundError:
        print(f"Error: No se encontro el archivo en la ruta '{ruta_archivo}'")
    return matriz

def generar_laberinto_aleatorio(filas, columnas, densidad_paredes=0.25):
    """Genera una matriz de laberinto aleatorio con borde cerrado."""
    matriz = [[' ' for _ in range(columnas)] for _ in range(filas)]
    
    for r in range(filas):
        for c in range(columnas):
            if r == 0 or r == filas - 1 or c == 0 or c == columnas - 1:
                matriz[r][c] = '#'
            elif random.random() < densidad_paredes:
                matriz[r][c] = '#'
                
    matriz[1][1] = 'S'
    matriz[filas - 2][columnas - 2] = 'E'
    
    return matriz