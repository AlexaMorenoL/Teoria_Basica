import numpy as np
#Ejemplo de uso transición con números complejos
ket = np.array([0.5+0.2j, 0.3-0.1j, 0.0 + 0.4j, 0.1+0.3j, 0.1-0.2j])
pos = 2
ket_inicial = np.array([0.2+0.3j, 0.1-0.4j, 0.0+0.5j, 0.3-0.2j])
ket_final = np.array([0.1-0.1j, 0.2+0.2j, 0.1-0.3j, 0.4+0.4j])

# 1. Calcular la probabilidad
def calcula_probabilidad(ket, pos):
    amplitud = ket[pos]
    probabilidad = np.abs(amplitud)**2
    return probabilidad

# 2. Calcular la probabilidad de transición
def calcula_transicion(ket_inicial, ket_final):
    producto_interno = np.vdot(ket_inicial, ket_final)
    transicion = np.abs(producto_interno)**2
    return transicion

print("La probabilidad de encontrar la partícula en la posición {pos} es:", calcula_probabilidad(ket, pos))
print("La probabbilidad de transitar un vector ket al otro es: ", calcula_transicion(ket_inicial, ket_final))

# 1. Amplitud de Transición
def amplitud_transicion(vector1, vector2):
    transicion = np.dot(np.conjugate(vector1), vector2)
    return np.abs(transicion)**2

# 2. Media y Varianza del Observable
def calcular_media_varianza(matriz_observable, estado):
    if np.allclose(matriz_observable, np.conjugate(np.transpose(matriz_observable))):
        media = np.dot(np.conjugate(estado), np.dot(matriz_observable, estado))
        varianza = np.dot(np.conjugate(estado), np.dot(matriz_observable**2, estado)) - np.abs(media)**2
        return media, varianza
    else:
        return "La matriz no es hermitiana"

# 3. Cálculo de Valores Propios y Probabilidad de Transición a Vectores Propios
def calcular_valores_propios_probabilidad(matriz_observable, estado):
    if np.allclose(matriz_observable, np.conjugate(np.transpose(matriz_observable))):
        valores_propios, vectores_propios = np.linalg.eigh(matriz_observable)
        probabilidad_transicion = np.abs(np.dot(np.conjugate(estado), vectores_propios))**2
        return valores_propios, probabilidad_transicion
    else:
        return "La matriz no es hermitiana"

# 4. Dinámica del Sistema
def evolucion_dinamica(matrices_operacion, estado_inicial):
    estado_actual = estado_inicial
    for matriz_operacion in matrices_operacion:
        estado_actual = np.dot(matriz_operacion, estado_actual)
    return estado_actual

# Ejemplos de uso
# Números complejos se representan como a + bi, donde a y b son números reales y i es la unidad imaginaria.

# Para los puntos 1, 2 y 3
vector1 = np.array([1 + 2j, 3 - 1j])
vector2 = np.array([2 - 1j, 1 + 2j])
matriz_observable = np.array([[1 + 1j, 2 - 1j],
                              [2 + 2j, 3 - 2j]])
estado = np.array([1 + 0j, 0 - 1j])

# Para el punto 4
matriz_operacion1 = np.array([[1 + 1j, 0],
                              [0, 1 - 1j]])
matriz_operacion2 = np.array([[1 - 1j, 2 + 1j],
                              [0, 1 + 2j]])
matrices_operacion = [matriz_operacion1, matriz_operacion2]

# Ejecutar las funciones
print("Probabilidad de transición:", amplitud_transicion(vector1, vector2))

media, varianza = calcular_media_varianza(matriz_observable, estado)
print("Media del observable:", media)
print("Varianza del observable:", varianza)

valores_propios, probabilidad_transicion_propios = calcular_valores_propios_probabilidad(matriz_observable, estado)
print("Valores propios del observable:", valores_propios)
print("Probabilidad de transición a vectores propios:", probabilidad_transicion_propios)

estado_final = evolucion_dinamica(matrices_operacion, estado)
print("Estado final después de la dinámica del sistema:", estado_final)
