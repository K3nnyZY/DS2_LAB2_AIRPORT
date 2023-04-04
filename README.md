# Vuelos Capitales Europeas


## Integrantes
- Kenny Zhu
- Juan Aragon
- Tomas Cervera

## Informacion
Este es un aplicativo web que permita a un usuario saber las distintas rutas de vuelos a las capitales 
del continente europeo, donde dada una distribución de vuelos (al menos lugar de inicio y de destino), 
y la distancia que hay entre ellos encontrar el camino de menor costo (distancia entre ellos) para 
que el usuario pueda llegar:
- A todos los lugares desde un punto inicial.
- A un destino en específico. 

## Funcionalidad
este software el cliente puede:
- seleccionar una ciudad origen y destino
- seleccionar una ciudad origen y a todos los ciudades destinos
- ver el camino de menor costo entre la ciudad origen y destino

## Diagrama UML
<img src = "uml/UML_Diagram.png">

## Como ejecutar
1. En el repositorio, presionar en la parte de code, para copiar el HTTPS.
2. Tener python instalado.
3. Ingresar a cualquier IDE como vscode y clonar el repositorio con:
```
git clone https://github.com/K3nnyZY/Data_Strucutures_Lab2.git
```
4. Instalar las librerias utilizadas:
```
pip3 install pandas
pip3 install flask
pip3 install folium
```
5. Ejecutar el codigo.