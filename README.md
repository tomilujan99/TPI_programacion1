# Gestión de Datos de Países en Python

Trabajo Práctico Integrador - Programación 1  
Tecnicatura Universitaria en Programación - UTN

## Integrantes
- Luján Tomás
- Mendizabal Gonzalo

## Descripción
Aplicación en Python que permite gestionar información sobre países
mediante un menú interactivo en consola. Lee y escribe datos desde
un archivo CSV, permitiendo realizar consultas, filtros, ordenamientos
y estadísticas sobre el dataset.

## Requisitos
- Python 3.x instalado
- No requiere librerías externas

## Cómo ejecutar
1. Clonar el repositorio:
   git clone https://github.com/tomilujan99/TPI_programacion1.git
2. Entrar a la carpeta del proyecto:
   cd TPI_programacion1
3. Ejecutar el programa:
   python main.py

## Funcionalidades
- **Agregar país**: permite ingresar un nuevo país con todos sus datos
- **Actualizar país**: modifica la población y superficie de un país existente
- **Buscar país**: búsqueda por nombre con coincidencia parcial
- **Filtrar países**: por continente, rango de población o rango de superficie
- **Ordenar países**: por nombre, población o superficie en forma ascendente o descendente
- **Estadísticas**: mayor y menor población, promedios y conteo por continente

## Estructura del proyecto
- main.py → código fuente principal
- paises.csv → dataset base con 20 países

## Ejemplos de uso

### Agregar un país
Elegí una opción: 1
Nombre del país: Italia
Población: 60317000
Superficie en km²: 301340
Continente: Europa
País 'Italia' agregado correctamente.

### Buscar un país
Elegí una opción: 3
Ingrese el nombre (o parte del nombre) a buscar: arg
Se encontraron 1 coincidencia(s):

Argentina | Continente: América | Población: 45376763 | Superficie: 2780400 km²

### Estadísticas
Elegí una opción: 6
ESTADÍSTICAS DEL DATASET
Mayor Población: China (1412600000 hab.)
Menor Población: Australia (25687041 hab.)
Promedio de Población: 245,678,432.00 hab.
Promedio de Superficie: 2,345,678.00 km²
Países por continente:

América: 3
Asia: 4
Europa: 3
África: 2
Oceanía: 1
==============================