# -*- coding: utf-8 -*-
"""03-Entrada y Salida de datos/Condicionales/Funciones.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hoyrb1gLNXhtFT9hzVeYjpRothDL_1Qx

# Entradas y Salidas
* input('Mensaje')
"""

lado = input('Valor del lado: ')

lado

lado * lado

lado = int(input('Valor del lado: '))

lado

lado * lado

lado = float(input('Lado: '))

lado

lado * lado

"""## Calcular area de un cuadrado"""

lado = float(input('Valor del lado: '))
area = lado * lado # lado ** 2
print('El area del cuadrado es', area)

num = 10

num = num + 5
num

num += 5
num

num -= 10
num

num *= 2
num

bin(100)

oct(10)

hex(10)

bin(100)

bin(100 << 2)

"h" in "hola"

"b" in "hola"

"H" in "hola"

"H" not in "hola"

a = 2
b = 3

a is b

var = 150

if var < 100:
    print('El valor es menor que 100')

var = 100

if var <= 100:
    print('El valor es menor o igual que 100')
else:
    print('El valor es mayor 100')

var = 150

if var < 100:
    print('El valor < 100')
elif var == 100:
    print('El valor es = 100')
else:
    print('El valor es > 100')

"""## Saber si un número es primo o no 1 <= x <= 10

* and
* or
* not
"""

num = int(input('Ingrese un numero entero: '))

if 1 <= num <= 10:
    if num == 2 or num == 3 or num == 5 or num == 7:
        print('Es primo')
    else:
        print('No es primo')
else:
    print('El numero debe estar entre 1 y 10, incluyendolos')

num = int(input('Ingrese un numero entero: '))

if 1 <= num <= 10:
    if num == 2 or num == 3 or num == 5 or num == 7:
        print('Es primo')
    else:
        print('No es primo')
else:
    print('El numero debe estar entre 1 y 10, incluyendolos')

"""$f(x) = x**2 + x + 1$"""

def f(x):
    print(x**2 + x + 1)

f(1)
f(2)
f(3)
f(4)

def esPrimo(num):
    if 1 <= num <= 10:
        if num == 2 or num == 3 or num == 5 or num == 7:
            print('Es primo')
        else:
            print('No es primo')
    else:
        print('El numero debe estar entre 1 y 10, incluyendolos')

num1 = int(input('Ingrese un numero entero: '))
num2 = int(input('Ingrese un numero entero: '))
num3 = int(input('Ingrese un numero entero: '))
num4 = int(input('Ingrese un numero entero: '))
num5 = int(input('Ingrese un numero entero: '))

esPrimo(num1)
esPrimo(num2)
esPrimo(num3)
esPrimo(num4)
esPrimo(num5)

def sumar(num1, num2):
    return num1 + num2

print(sumar(2, 3))
print(sumar(7, 9))

def cambiarNumero(num):
    print('numero antes de cambiar en la funcion', num)
    num = 5
    print('numero despues de cambiar en la funcion', num)

num = 10
print(num)
cambiarNumero(num)
print(num)

def cambiarLista(lista):
    print("Valor en la funcion antes del cambio:", lista)
    lista[2] = 50
    print("Valor en la funcion despues del cambio:", lista)

lista = [10,20,30]
cambiarLista(lista)
print("Valor fuera de la funcion:", lista)

def cambiarLista(lista):
    print("Valor en la funcion antes del cambio:", lista)
    lista = [10, 50]
    lista[1] = 100
    print("Valor en la funcion despues del cambio:", lista)
    return lista

lista = [10,20,30]
lista = cambiarLista(lista)
print("Valor fuera de la funcion:", lista)

"""# Parametros de la función

* Keyargs
"""

def funcion(**kargs):
    """Funcion
    args:
        - num1 - entero
        - num2 - entero
    """
    num1 = kargs['num1']
    num2 = kargs['num2']
    print(num1 + num2)

funcion(num1=2, num2=3)

"""* args"""

def sumarTodo(*args):
    print(sum(args))

sumarTodo(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)



def sumar(a, b=5, *args, **kargs):
    print(a * b, sum(args), kargs)

sumar(5, 3, 8, 5, 3, 6, 9, num=1, num2=5)

sumar(2, 3)

sumar(2)

"""# Validar si un numero es par o impar"""

def esPar(num):
    if num % 2 == 0:
        print('Es par')
    else:
        print('Es impar')

esPar(2)

esPar(3)
esPar(29478984395)
esPar(473984098248732492)

"""# Usar los valores de retorno de las funciones"""

def f(a, b):
    return a + b + b**2

def realizarOperacion(num1, num2):
    resultado = f(num1, num2)
    return [1] * resultado

realizarOperacion(2, 1)

def esPrimo(num):
    if num == 2 or num == 3 or num == 5 or num == 7:
        return True
    else:
        return False

def esPar(num):
    if num % 2 == 0:
        return True
    else:
        return False

def esParYPrimo(num):
    if esPar(num) and esPrimo(num):
        print('El numero es par y primo')
    elif esPar(num):
        print('El numero es par pero no primo')
    elif esPrimo(num):
        print('El numero es primo pero no par')
    else:
        print('El numero no es par ni primo al mismo tiempo')

esParYPrimo(2)