# Data_Strucutures_Lab2
- Kenny Zhu
- Juan Aragon
- Tomas Cervera
## Vuelos capitales
Se requiere crear un software que permita a un usuario saber las distintas rutas de vuelos a
las capitales del mundo (como un reto puede intentar trabajar con todas las capitales, pero
también es posible acotar el problema a un continente especifico, América debe ser
considerado como un solo continente). Para esto se le ha solicitado que desarrolle un sistema
que permita dada una distribución de vuelos (al menos lugar de inicio y de destino), y la
distancia que hay entre ellos encontrar el camino de menor costo para que el usuario pueda
llegar:
• A todos los lugares desde un punto inicial.
• A un destino en específico.
• Mirar los requerimientos mínimos.


2. Requerimientos mínimos
a. Desarrollar un programa en Java o Python que permita construir manualmente
un grafo, que utilice un mapa como imagen de fondo (la imagen únicamente
enriquece la interfaz visual del programa, pero no influye en la solución del
problema).
b. A medida que el usuario selecciona los puntos en la pantalla donde desea
agregar un edificio/lugar, el programa debe preguntar el nombre de este. (la
forma en cómo ingrese los datos puede ser diferente a la aquí propuesta con
tal de que siga cumpliendo el requerimiento).
c. Una vez ingresados todos los puntos de interés, el programa debe permitir
ingresar la adyacencia que hay entre cada par de lugares.
d. El programa debe permitir eliminar un edificio/lugar seleccionado (como se
seleccione queda a la imaginación de ustedes). Si se elimina un edificio/lugar,
se deben eliminar las aristas (entrada y salida) asociadas a este.
e. El programa no debe permitir agregar un lugar encima de otro (manejo de
colisiones).
f. Al finalizar de construir el grafo, el programa debe mostrar un botón para
ejecutar los recorridos BFS y DFS. Cada recorrido debe recibir como
parámetro de entrada inicial