Tarea 5 — Listas ligadas: sencilla y doble

Medición

Cifras obtenidas al ejecutar python cadena.py (cadenas cargadas con los enteros de 0 a n − 1):

| n (nodos) | Dos pasadas | Liebre y tortuga |
| --- | --- | --- |
| 1.001 | 1.501 | 1.500 |
| 10.001 | 15.001 | 15.000 |
| 100.001 | 150.001 | 150.000 |

Lectura

Las dos columnas dan casi lo mismo: en ambas crece en torno a 1,5 n, así que en cantidad de pasos la liebre y la tortuga no gana nada, lo que gana es que entra a la cadena una sola vez por el primer nodo, mientras que las dos pasadas entran dos veces, una para contar y otra para caminar hasta la mitad

Eso importa cuando recorrer no sale barato o no se puede repetir: nodos dispersos en memoria o en disco (cada recorrido completo vuelve a pagar los fallos de caché o las lecturas), datos que llegan como flujo y solo se pueden leer una vez, o cadenas que otro proceso puede modificar entre la primera pasada y la segunda (el conteo de la primera ya no sería válido en la segunda) con la cadena en memoria y quieta, como en esta medición, da igual cuál se use

Por qué en la sencilla hay que guardar el siguiente antes de pisarlo y en la doble no, al invertir la sencilla, actual.siguiente se redirige hacia atrás, si no se guardó antes el nodo que venía después, el resto de la cadena queda sin ningún puntero que llegue a él y se pierde en la doble, al intercambiar los dos punteros del nodo, el viejo siguiente queda guardado en actual.anterior, así que se puede seguir avanzando por ahí sin variable auxiliar
