# -*- coding: utf-8 -*-
"""Introducción a la Programación con Python - Parte II.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RzdhSIRvTaopTsxNSMCKfvUqs3KhLjQu

# **Introducción a la Programación con Python**
## *Parte 2*

### **Ciclo While**
"""

while (condicion): # Si la condicion se cumple, el ciclo se ejecuta
    # Bloque de codigo

contador = 0

while (contador <= 10):
    print(contador)
    contador = contador + 1 # contador += 1

contador = 10

while (contador > 0):
    print(contador)
    contador = contador - 1 # contador -= 1

contador = 0

while (contador <= 10):
    if (contador % 2 == 0):
        print(contador)
    contador = contador + 1

num = int(input('Ingrese un numero: '))

def esPrimo(num):
    if (num < 2):
        return False

    div = 2

    while (div < num):
        if (num % div == 0):
            return False
        div += 1
    return True

if esPrimo(num):
    print('El numero es primo')
else:
    print('El numero no es primo')

"""### **Ciclo For**"""

# Forma 1
# i = 0
# i < final
# i += 1
for i in range(final):
    # Codigo

for i in range(10):
    print(i)

# Forma 2
# i = inicial
# i < final
# i += 1
for i in range(inicial, final):
    # Bloque de codigo

for i in range(20, 30):
    print(i)

for i in range(20, 30):
    if (i % 2 == 0):
        print(i)

# Forma 3
# i = inicial
# i < final
# i += paso
for i in range(inicial, final, paso):

for i in range(5, 100, 5):
    print(i)

for i in range(20, 30, 2):
    print(i)

for i in range(0, 30, 5):
    print(i)

i = 2

for i in range(30):
    print(i)

for i in range(-30, 30, 5):
    print(i)

for i in range(30, 0, -5):
    print(i)

inicial = 0
final = 10
paso = 2

for i in range(inicial, final + 1, paso):
    print(i)

"""### Forma 4"""

cadena = 'Erick'

for c in cadena:
    print(c)

cadena = 'Erick'

# len(obj) -> contar la cantidad de elementos de una secuencia
for i in range(len(cadena)):
    print(cadena[i])

lista = [1, 2, 3, 4, 5, 6]

for num in lista:
    print(num)

tupla = (1, 2, 3, 4, 5, 6)

for num in tupla:
    print(num)

diccionario = {'Hello': 'Hola', 'One': 'Uno', 'Bird': 'Pajaro', 'Book': 'Libro'}

for valor in diccionario:
    print(valor)

diccionario = {'Hello': 'Hola', 'One': 'Uno', 'Bird': 'Pajaro', 'Book': 'Libro'}

for valor in diccionario.keys():
    print(valor)

diccionario = {'Hello': 'Hola', 'One': 'Uno', 'Bird': 'Pajaro', 'Book': 'Libro'}

for valor in diccionario.values():
    print(valor)

diccionario = {'Hello': 'Hola', 'One': 'Uno', 'Bird': 'Pajaro', 'Book': 'Libro'}

for valor in diccionario:
    print(valor, diccionario[valor])

diccionario = {'Hello': 'Hola', 'One': 'Uno', 'Bird': 'Pajaro', 'Book': 'Libro'}

for item in diccionario.items(): # Llave, valor
    print(item)

diccionario = {'Hello': 'Hola', 'One': 'Uno', 'Bird': 'Pajaro', 'Book': 'Libro'}

for (llave, valor) in diccionario.items(): # Llave, valor
    print(llave, valor)

"""# Tablas de multiplicar"""

for num1 in range(1, 12): # 
    for num2 in range(1, 10): # Termina ejecucion primero
        print(num1, 'x', num2, '=', num1 * num2)
    print()

"""# Excepciones"""

num = int(input('Ingrese un numero entero: '))

try:
    # Codigo que funciona
except ErrorEsperado:
    # Que hago si ocurre dicho error

try:
    num = int(input('Ingrese un numero entero: '))
except ValueError:
    print('Debe ingresar un numero entero')

"""# Continuando con la ejecución"""

while True:
    try:
        num = int(input('Ingrese un numero entero: '))
        print('Ingreso el numero:', num)
        break # Termina el ciclo abruptamente
    except ValueError:
        print('Debe ingresar un numero entero')

try:
    # indices 0  1  2  3  4
    lista =  [1, 2, 3, 4, 5]
    print(lista[5])
except IndexError:
    print('El indice no existe')

esCorrecto = False

while not esCorrecto:
    try:
        num = int(input('Ingrese un numero entero: '))
        print('Ingreso el numero:', num)
        esCorrecto = True
    except ValueError:
        print('Debe ingresar un numero entero')

try:
    # Codigo que funciona
except: # Tomando en cuenta todos los error
    # Que hacer cuando ocurre el error

try:
    # Codigo
except Error1:
    # Manejo error1
except Error2:
    # Manejo error2

lista = [1, 2, 3, 4, 5]

esCorrecto = True

while esCorrecto:
    try:
        indice = int(input('Ingrese el indice que desea mostrar: '))
        print('El valor en el indice', indice, 'es', lista[indice])
        esCorrecto = False
    except ValueError:
        print('Debe ingresar un numero')
    except IndexError:
        print('El indice no existe')

esCorrecto = True

# Redundante
if esCorrecto == False: # not esCorrecto
    print('Verdad')
else:
    print('False')

"""# Secuencias

## Listas

[Todos los métodos de la lista](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
"""

lista = [] # Vacia
lista = [1, 2, 3, 4] # Cuatro elementos
lista[0]

lista[-1]

lista[6]

lista[-10]

# Agrega un objeto a la lista, al final
lista.append(15)
lista

# Se agrega un objeto a la lista (pos, elemento)
lista.insert(0, 100)
lista

lista.insert(-1, 500)
lista

# len -> me da el tamaño de la lista
lista.insert(len(lista), 10000)
lista

# pop -> Elimina el elemento el posicion j: me devuelve el objeto
# lista.pop(j)
eliminado = lista.pop() # El ultimo
print(eliminado, lista)

eliminado = lista.pop(0) # El primero
print(eliminado, lista)

# lista.remove(obj) -> Elimina el obj
lista.remove(1)
lista

# lista.remove(obj) -> Elimina el obj
# Cuando hay repetido, elimina la primer aparicion
lista.remove(10) # No devuelve nada
lista

lista = [1, 2, 3, 4]
lista = []
lista

lista = [1, 2, 3, 4]
lista.clear() # Elimina todos los elementos de la lista
lista

# lista.count(obj) -> La cantidad de veces que aparece obj en la lista
lista = [1, 2, 3, 1, 1, 5, 7]
lista.count(1)

lista.count(7)

lista.count(1000)

# contar pares
lista = [1, 3, 6, 7, 7, 2, 5, 6]
cantidad = 0

for num in lista:
    if num % 2 == 0:
        cantidad += 1
cantidad

# lista.index(obj) -> Devuelve la posicion de primera aparicion de obj en la lista
lista = [1, 2, 3, 1, 1, 5, 7]
lista.index(1)

lista.index(7)

lista.index(10)

# lista.sort() -> Ordena la lista en forma asc
lista = [8, 2, 5, 1, 7, 4, 8]
lista.sort()
lista

# lista.sort(reverse=True) -> Ordena la lista en forma desc
lista = [8, 2, 5, 1, 7, 4, 8]
lista.sort(reverse=True)
lista

# sorted(seq) -> ordenada
lista = [8, 2, 5, 1, 7, 4, 8]
sorted(lista)

lista = sorted(lista)
lista

lista = [1, 2, 3, 4]
lista2 = lista
lista[0] = 1000
lista2

# lista.copy() -> Devuelve una copia de la lista
lista = [1, 2, 3, 4]
lista2 = lista.copy()
lista[0] = 1000
lista2

lista = [1, 2, 3, 4]
lista2 = lista[:] # lista[inicio:fin], lista[:fin], lista[inicio:], lista[:]
lista[0] = 1000
lista2

"""Más información sobre la librería [random](https://docs.python.org/3/library/random.html)"""

import random

lista = []

for i in range(10):
    # Numeros aleatorios entre 0 y 100
    lista.append(random.randint(0, 100))

lista

# lista[inicio:fin] -> desde inicio hasta un elemento antes de fin
lista[2:5]

# lista[:fin] -> desde la posicion 0 hasta un elemento antes de fin
lista[:6]

# lista[inicio:] -> desde inicio hasta un elemento antes el ultimo elemento
lista[4:]

# lista[:] -> todos los elementos
lista[:]

"""# Compresión de Listas

[más información](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)
"""

lista = [valor for valor in range(10)]
lista

lista = [valor for valor in range(10) if valor % 2 == 0]
lista

import random

lista = [random.randint(-10, 10) for _ in range(20)]
lista

# Valor absoluto de un numero
num = -10
abs(num)

num = -10
if num < 0:
    num = abs(num)

num

num = -10
num = num if num >= 0 else abs(num)
num

"""# Compresion de Listas anidadas"""

# Listas de listas o matrices
matriz = [[i * j  for i in range(10)] for j in range(20)]
matriz

matriz[i][j]

matriz[5][5]

matriz[2][3]

matriz[4]

matriz[2][3][0]

matriz[0].insert(0, 100)
matriz

matriz2 = matriz
matriz[0][0] = -1
matriz2

matriz3 = matriz[:]
matriz[0][0] = -10
matriz3

matriz4 = matriz.copy()
matriz[0][0] = 100
matriz4

matriz5 = matriz[:][:]
matriz[0][0] = -300
matriz5

matriz6 = [fila[:] for fila in matriz]
matriz[0][0] = 15
matriz6

"""# Tuplas"""

tupla = (1, 2, 4)

len(tupla)

tupla[0] = 10

tupla = tupla + (1,)

tupla

tupla = (-1,) + tupla
tupla

tupla = tupla[:2] + (15,) + tupla[2:]

tupla

list(tupla)

a, b, c, d, e, f = tupla

print(a, b, c, d, e, f)

"""# Diccionarios

[más información](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
"""

diccionario = {}

diccionario[key] = value

diccionario = {llave1: valor1, llave2: valor2, ..., llaven: valorn}

diccionario = {'hola': 0, 'adios': 5, 'gato': 20, 'perro': 10}
diccionario

diccionario.keys()

diccionario.values()

diccionario.items()

del diccionario['hola']
diccionario

diccionario['hola'] = 300
diccionario

diccionario['hola'] = 1000
diccionario

diccionario['adios']

diccionario['kinder']

"""# Compresion de diccionarios"""

diccionario = {i: i**2 for i in range(10)}
diccionario

llaves = [0, 1, 2, 3, 4]
valores = [0, 1, 4, 9, 16]

# zip -> [(itemLista, itemLista2)]
diccionario = {llave: valor for llave, valor in zip(llaves, valores)}
diccionario

diccionario['hola'] = [1, 2, 3]
diccionario

diccionario['hola'].append(10)

diccionario

"""# Cadenas

[Todos los métodos](https://docs.python.org/3/library/stdtypes.html#string-methods)
"""

cadena = '' # = ""
# cadena = ' '

cadena = '123'
cadena

int(cadena)

cadena = '1h12b'
int(cadena)

cadena = '1h12b'
cadena.isnumeric()

cadena = '112'
cadena.isnumeric()

'ajhfhfkd'.upper()

'KSFKSFJKS'.lower()

'dkjkfsk'.capitalize()

'ajsfhsa'.isupper()

'HsjISJF'.isupper()

'ASIFHFF'.isupper()

'ajsfhsa'.islower()

num1 = 6
num2 = 5
suma = num1 + num2
formato = '{} + {} = {}'.format(num1, num2, suma)
print(formato)

sorted('hola') # Ordena por codigo ASCII

sorted('Hola')

''.join(sorted('hola'))

'--'.join(sorted('hola'))

'adios'.join(sorted('hola'))

sorted(['erick', 'ana', 'andres', 'danny', 'samuel'])

"""# Recursividad o Recursion

$\sum_{i=0}^{n}{i} = 0 + 1 + 2 + 3 + ... + n$
"""

"""
sumatoria(5)
5 + sumatoria(4)
5 + 4 + sumatoria(3)
5 + 4 + 3 + sumatoria(2)
5 + 4 + 3 + 2 + sumatoria(1)
5 + 4 + 3 + 2 + 1 + sumatoria(0)
5 + 4 + 3 + 2 + 1 + 0
5 + 4 + 3 + 2 + 1
5 + 4 + 3 + 3
5 + 4 + 6
5 + 10
15

>>> 15
"""
def sumatoria(num):
    print(num)
    if num == 0:
        return 0
    return num + sumatoria(num - 1)

sumatoria(5)

"""
crearSequencia(3)
[3] + crearSequencia(2)
[3] + [2] + crearSequencia(1)
[3] + [2] + [1] + crearSequencia(0)
[3] + [2] + [1] + [0]
[3] + [2] + [1, 0]
[3] + [2, 1, 0]
[3, 2, 1, 0]
"""
def crearSequencia(num):
    if (num == 0):
        return [0]
    return [num] + crearSequencia(num - 1)

crearSequencia(3)

def crearSequencia(num):
    if (num == 0):
        return [0]
    return crearSequencia(num - 1) + [num]

crearSequencia(3)

import random

def crearFila(cols):
    if (cols == 0):
        return []
    return crearFila(cols - 1) + [random.randint(0, 9)]

def crearMatriz(filas, cols):
    if filas == 0:
        return []
    else:
        return [crearFila(cols)] + crearMatriz(filas - 1, cols)

"""
crearMatriz(2, 3)
[crearFila(3)] + crearMatriz(1, 3)
[crearFila(2) + [3]] + crearMatriz(1, 3)
[crearFila(1) + [4] + [3]] + crearMatriz(1, 3)
[crearFila(0) + [4] + [4] + [3]] + crearMatriz(1, 3)
[[] + [4] + [4] + [3]] + crearMatriz(1, 3)
[[4, 4, 3]] + crearMatriz(1, 3)
[[4, 4, 3]] + [crearFila(3)] + crearMatriz(0, 3)
[[4, 4, 3]] + [[5, 2, 1]] + crearMatriz(0, 3)
[[4, 4, 3]] + [[5, 2, 1]] + []
[[4, 4, 3]] + [[5, 2, 1]]
[[4, 4, 3], [5, 2, 1]]
>>> [[4, 4, 3], [5, 2, 1]]
"""
crearMatriz(2, 3)

"""# Recursividad de Cola"""

