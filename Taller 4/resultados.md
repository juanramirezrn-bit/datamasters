# Resultados de la medición

Computador: contenedor Linux (Ubuntu 24.04) usado para probar el código.
Versión de Python: 3.12.3

| Lado  | Celdas    | Tiempo (s) | Factor respecto a la anterior |
|-------|-----------|------------|--------------------------------|
| 250   | 62.500    | 0,0011     | -                              |
| 500   | 250.000   | 0,0046     | 4,10                           |
| 1.000 | 1.000.000 | 0,0197     | 4,29                           |

**Interpretación**

Al doblar el lado de la matriz, el tiempo de `suma()` se multiplicó por un
factor cercano a cuatro (4,10 y 4,29), tal como se esperaba.

Esto era de esperar porque `suma()` es O(f · c): al doblar el lado, las
celdas se multiplican por cuatro (250×250 = 62.500 y 500×500 = 250.000),
y como el costo depende directamente del número de celdas, el tiempo
también se multiplica por cuatro
