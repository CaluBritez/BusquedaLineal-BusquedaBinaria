import time
import tracemalloc

def busqueda_lineal(lista, valor):
    for indice, elemento in enumerate(lista):
        if elemento == valor:
            return indice
    return -1
'''
# Ejemplo
lista = [3, 7, 2, 9, 5, 8]
objetivo = 9

resultado = busqueda_lineal(lista, objetivo)
if resultado != -1:
    print(f'Elemento encontrado en el índice {resultado}.')
else:
    print('Elemento no encontrado en la lista.')

'''
def busqueda_binaria(lista, objetivo):
    izquierda = 0
    derecha = len(lista) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return -1

'''
# Ejemplo de uso
lista_ordenada = [1, 3, 5, 7, 9, 11, 13, 15]
valor = 15

resultado = busqueda_binaria(lista_ordenada, valor)
if resultado != -1:
    print(f'Elemento encontrado en el índice {resultado}.')
else:
    print('Elemento no encontrado en la lista.')
'''
# Función para medir el tiempo de ejecución
def medir_tiempo(func, *args):
    inicio = time.time()
    resultado = func(*args)
    fin = time.time()
    return fin - inicio, resultado

# Función para medir el uso de memoria
def medir_memoria(func, *args):
    tracemalloc.start()
    resultado = func(*args)
    memoria_usada, pico = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return memoria_usada, pico, resultado

# Crear una lista grande para la prueba
lista = list(range(1000000))
objetivo = 999999

# Medir y comparar tiempos de ejecución
tiempo_lineal, _ = medir_tiempo(busqueda_lineal, lista, objetivo)
tiempo_binaria, _ = medir_tiempo(busqueda_binaria, lista, objetivo)
print(f"Tiempo de búsqueda lineal: {tiempo_lineal:.6f} segundos")
print(f"Tiempo de búsqueda binaria: {tiempo_binaria:.6f} segundos")

# Medir y comparar uso de memoria
memoria_lineal, pico_lineal, _ = medir_memoria(busqueda_lineal, lista, objetivo)
memoria_binaria, pico_binaria, _ = medir_memoria(busqueda_binaria, lista, objetivo)
print(f"Memoria utilizada en búsqueda lineal: {memoria_lineal} bytes (pico: {pico_lineal} bytes)")
print(f"Memoria utilizada en búsqueda binaria: {memoria_binaria} bytes (pico: {pico_binaria} bytes)")
