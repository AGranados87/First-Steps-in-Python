# Veamos como podemos hacer que funciones interactuen entre ellas. Vamos a necesitar crear una lista inicial. Luego,
# una funcion que se encargue de mezclar los palos. Luego, otra funcion que pida al usuario que elija uno de los cuatro numeros.
# Y finalmente, otra funcion que compruebe el intento.

from random import *

# Lista inicial


palitos = ["-", "--", "---", "----"]

# mezclar palitos


def mezclar(lista):  # funcion para mezclar
    shuffle(lista)
    return lista


# pedirle intento

def intento():
    intento = ""
    while intento not in ["1", "2", "3", "4"]:
        intento = input("Elige un numero del 1 al 4: ")
        print(intento)
    return int(intento)


# comprobar intento
def checkintento(lista, intento):
    if lista [intento - 1] == "-":
        print("Perdiste")
    else:
        print("Esta vez te salvaste")

    print(f"Te ha tocado {lista[intento-1]}")


palitosmezclados = mezclar(palitos)
seleccion = intento()
checkintento(palitosmezclados, seleccion)

'''Práctica sobre Interacción entre Funciones 1

Crea una función (lanzar_dados) que arroje dos dados al azar y devuelva sus resultados:

    La función debe retornar dos valores resultado, que se encuentren entre 1 y 6).

    Dicha función no debe requerir argumentos para funcionar, sino que debe generar internamente los valores aleatorios.

Proporciona el resultado de estos dos dados a una función que se llame evaluar_jugada (es decir, esta segunda función debe recibir dos argumentos) y que retorne -sin imprimirlo- un mensaje según la suma de estos valores:

Si la suma es menor o igual a 6:

    "La suma de tus dados es {suma_dados}. Lamentable"

Si la suma es mayor a 6 y menor a 10:

    "La suma de tus dados es {suma_dados}. Tienes buenas chances"

Si la suma es mayor o igual a 10:

    "La suma de tus dados es {suma_dados}. Parece una jugada ganadora"

Pistas: utiliza el método choice o randint de la biblioteca random para elegir un valor al azar entre 1 y 6.'''


def lanzar_dados():
    dado1 = randint(1, 6)
    dado2 = randint(1, 6)
    return dado1, dado2


dado1, dado2 = lanzar_dados()


def evaluar_jugada(dado1, dado2):
    suma = dado1 + dado2
    if suma <= 6:
        return (f"La suma de tus dados es {suma}. Lamentable")
    elif 6 < suma < 10:
        return (f"La suma de tus dados es {suma}. Tienes buenas chances.")
    elif suma >= 10:
        return (f"La suma de tus dados es {suma}. Parece una jugada ganadora")


print(evaluar_jugada(dado1, dado2))




