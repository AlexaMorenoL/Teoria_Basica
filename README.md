# Teoría cuántica básica, Observables y Medidas
## Autora

***Alexandra Moreno Latorre***

## Programas de simulación
El sistema consiste en una partícula confinada a un conjunto discreto de posiciones en una línea. El simulador debe permitir especificar el número de posiciones y un vector ket de estado asignando las amplitudes.
1. El sistema debe calcular la probabilidad de encontrarlo en una posición en particular.
2. El sistema si se le da otro vector Ket debe buscar la probabilidad de transitar del primer vector al segundo.

## Descripción de la librería
Este código implementa algunas operaciones básicas en mecánica cuántica, utilizando el paquete NumPy de Python.
1. Probabilidad de transición.
Esta función calcula el producto interno entre los dos estados, y luego toma el cuadrado del valor absoluto del resultado.
2. Media y varianza del observable.
La función calcular_media_varianza() primero verifica si la matriz del observable es hermitiana. Si lo es, entonces la media se calcula como el producto interno entre el estado y la matriz del observable, y la varianza se calcula como la media del cuadrado de la diferencia entre el estado y la media.
3. Valores propios y probabilidad de transición a vectores propios
La función calcular_valores_propios_probabilidad() primero verifica si la matriz del observable es hermitiana. Si lo es, entonces los valores propios y los vectores propios se pueden calcular utilizando la función np.linalg.eigh() de NumPy. La probabilidad de transición a un vector propio se calcula como el cuadrado del valor absoluto del producto interno entre el estado y el vector propio correspondiente.
4. Dinámica del sistema
Esta función calcula la evolución temporal del estado del sistema a través de una secuencia de matrices de operación. Cada matriz de operación representa una interacción o transformación que experimenta el sistema.
Ejemplos de uso.
El código incluye algunos ejemplos de uso de las funciones anteriores. En el ejemplo de uso, se calcula la probabilidad de transición entre dos estados, la media y la varianza de un observable, los valores propios y la probabilidad de transición a vectores propios de una matriz observable, y la evolución dinámica de un sistema.

## Contenido

### Archivos
- ***Teoria.py*** -> Es el archivo de librería con las funciones correspondientes para realizar cada experimento estudiado y diversos ejercicios para corroborrar el correcto funcionamiento de las funciones.
- ***.gitignore*** -> Es el archivo que excluye lo que no queremos que se suba al repositorio GITHUB.
- ***README.md*** -> Es el archivo de texto de la librería.

## Requisitos para usar el sistema

Debe de poseer una versión a ***Python*** superior a 3.5, la librería ***numpy*** y descargar el repositorio.
