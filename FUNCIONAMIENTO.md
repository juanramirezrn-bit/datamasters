
DOCUMENTO DE PROYECTO: SISTEMA DE RESOLUCIÓN Y ANÁLISIS DE LABERINTOS Y ESTRUCTURAS




1.	PROBLEMA QUE RESUELVE
Este proyecto aborda la navegación y resolución de laberintos mediante el uso de estructuras de datos lineales implementadas desde cero, utilizando memoria enlazada y memoria dinámica. El sistema permite comparar el rendimiento temporal entre algoritmos de búsqueda de rutas (DFS y BFS) y algoritmos de ordenamiento (Burbuja y Quicksort), sirviendo como una herramienta para analizar la complejidad computacional.
2.	COMPONENTES PRINCIPALES
•	Arquitectura modular: Separación de responsabilidades entre la interfaz, la lógica, las estructuras de datos y el manejo de archivos.
•	Estructuras propias: Implementación manual de nodos, pilas, colas y arreglos de tamaño variable con redimensionamiento automático.
•	Búsqueda de caminos:
o	DFS (Búsqueda en Profundidad): Usa una Pila (LIFO) para explorar rutas rápidamente.
o	BFS (Búsqueda en Anchura): Usa una Cola (FIFO) para garantizar la ruta más corta.
•	Entrada de datos: Generación de laberintos aleatorios de dimensiones N por M con obstáculos o carga de mapas desde archivos externos.
•	Evaluación de rendimiento: Módulo para medir y contrastar los tiempos de ejecución entre ordenamiento burbuja y Quicksort.
•	Verificación: Pruebas unitarias con el módulo unittest para validar las operaciones críticas.

3.	FUNCIONAMIENTO DEL SISTEMA
   
3.1. Inicialización y Entrada
El programa inicia en el archivo principal indicando las dimensiones del entorno. A través del cargador de datos, se genera un laberinto aleatorio con un punto de inicio, un punto final y obstáculos, o bien se lee un archivo externo.


3.2. Estructuras de Almacenamiento
Las operaciones de recorrido emplean nodos, pilas y colas. El arreglo dinámico gestiona el almacenamiento duplicando su espacio en memoria cuando alcanza su límite.

3.3. Proceso de Resolución
La clase encargada del laberinto procesa la matriz con los métodos de búsqueda. El método DFS explora pasillos en profundidad mediante una pila, mientras que el método BFS expande los nodos vecinos de manera uniforme hasta encontrar la ruta óptima.

3.4. Medición y Ordenamiento
El sistema utiliza funciones de tiempo para registrar y comparar la velocidad de los algoritmos de ordenamiento implementados.

3.5. Salida y Verificación
El programa muestra en la consola la matriz original y la solución encontrada. El comportamiento del código se comprueba mediante pruebas automáticas guiadas por las instrucciones del archivo README.

