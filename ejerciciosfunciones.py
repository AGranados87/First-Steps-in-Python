""" Crea una función llamada devolver_distintos() que reciba 3 integers como parámetros.
Si la suma de los 3 numeros es mayor a 15, va a devolver el número mayor.
Si la suma de los 3 numeros es menor a 10, va a devolver el número menor.
Si la suma de los 3 números es un valor entre 10 y 15 (incluidos) va a devolver el número de valor intermedio. """


def devolverdistintos(num1, num2, num3):
    lista = [num1, num2, num3]
    suma = num1 + num2 + num3
    if suma > 15:
        for i in lista:
            maxValue = max(lista)
        return f'El resultado es {suma}, mayor que 15, y el numero mayor es {maxValue}.'
    elif suma < 10:
        minValue = min(lista)
        return f"El resultado es {suma}, menor que 10, y el numero de menor valor es {minValue}."
    elif 10 <= suma <= 15:
        lista.sort()
        return f"El resultado es {suma}, se encuentra entre 10 y 15, el valor intermedio es {lista[1]}"


print(devolverdistintos(12, 1, 2))

'''Escribe una función (puedes ponerle cualquier nombre que
quieras) que reciba cualquier palabra como parámetro, y que
devuelva todas sus letras únicas (sin repetir) pero en orden
alfabético.
Por ejemplo si al invocar esta función pasamos la palabra
"entretenido", debería devolver ['d', 'e', 'i', 'n', 'o', 'r', 't']'''


def palabrator(palabra):
    palabra = "".join(sorted(set(palabra)))
    print(palabra)


palabrator("somnoliento")

"""Escribe una función que requiera una cantidad indefinida de
argumentos. Lo que hará esta función es devolver True si en
algún momento se ha ingresado al numero cero repetido dos
veces consecutivas.
Por ejemplo:
(5,6,1,0,0,9,3,5) >>> True
(6,0,5,1,0,3,0,1) >>> False"""


def argumentos(*args):
    counter = 0
    for i in args:
        if i == 0:
            counter += 1
            if counter == 2:
                return True
        else:
            counter = 0
    return False


print(argumentos(1, 2, 3, 54, 6, 7, 0, 0, 9, 8, 7, 8, 6))
print(argumentos(1, 2, 5, 6, 43, 0, 5, 5, 6, 87, 8, 8, 6, 7, 8, 0))

"""Escribe una función llamada contar_primos() que requiera un
solo argumento numérico.
Esta función va a mostrar en pantalla
todos los números
primos existentes en el rango que va desde cero hasta ese
número incluido, y va a devolver la cantidad de números
primos que encontró.
Aclaración, por convención el 0 y el 1 no se consideran primos"""

def contar_primos(numero):

    primos = [2]
    iteracion = 3

    if numero < 2:
        return 0

    while iteracion <= numero:

        for i in range(3, iteracion, 2):
            if iteracion % i == 0:
                iteracion += 2
                break
        else:
            primos.append(iteracion)
            iteracion += 2
    print(primos)
    return len(primos)

print(contar_primos(50))



