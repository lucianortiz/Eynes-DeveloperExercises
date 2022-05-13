from random import randint
from typing import List

# Carga la lista con 10 diccionarios, id empieza en 1 y la edad es un numero aleatorio entre 1 y 100
# :rtype: List
def generar_lista():
    lista= []
    for i in range(10):
        diccionario= { 'id': i+1, 'edad': randint(1,100)}
        lista.append(diccionario)
    
    return lista

# Ordena la lista por edad y hace el llamado a la funcion para mostrar ID de mayor y menor edad
# type lista: List | :rtype: List
def ordenar(lista):
    lista_ordenada= sorted(lista, key=lambda diccionario : diccionario['edad'], reverse=True)
    max_y_min_edad(lista_ordenada)
    return lista_ordenada

def max_y_min_edad(lista):
    print(f"ID de la persona mas joven -> {lista[-1]['id']}")
    print(f"ID de la persona mas vieja -> {lista[0]['id']}")

def mostrar(lista):
    print(lista)

def ejecutar():
    lista_de_diccionarios= generar_lista()
    print("\n--- Lista de diccionarios ---")
    mostrar(lista_de_diccionarios)

    lista_ordenada= ordenar(lista_de_diccionarios)
    print("\n--- Lista ordenada de diccionarios ---")
    mostrar(lista_ordenada)
    print("")

if __name__ == '__main__':
    ejecutar()
    