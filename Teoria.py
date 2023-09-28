import numpy as np
#Ejemplo de uso transición con números complejos
ket = np.array([0.5+0.2j, 0.3-0.1j, 0.0 + 0.4j, 0.1+0.3j, 0.1-0.2j])
pos = 2
ket_inicial = np.array([0.2+0.3j, 0.1-0.4j, 0.0+0.5j, 0.3-0.2j])
ket_final = np.array([0.1-0.1j, 0.2+0.2j, 0.1-0.3j, 0.4+0.4j])

def calcula_probabilidad(ket, pos):
    amplitud = ket[pos]
    probabilidad = np.abs(amplitud)**2
    return probabilidad

def calcula_transicion(ket_inicial, ket_final):
    producto_interno = np.vdot(ket_inicial, ket_final)
    transicion = np.abs(producto_interno)**2
    return transicion

print("La probabilidad de encontrar la partícula en la posición {pos} es:", calcula_probabilidad(ket, pos))
print("La probabbilidad de transitar un vector ket al otro es: ", calcula_transicion(ket_inicial, ket_final))