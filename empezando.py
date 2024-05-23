#Un primer print, el famoso SYSTEM.OUT.PRINTLN
print("Hola alumnos")

#Cada instruccion debe ir en una linea, aunque es una practica desaconsejada incluir mas de una expresion por linea.
print("hola a todos, programamos en Python"), print("vamos alla")

#Python asigna el tipo de variable basandose en el contenido de la misma. Si es una cadena de texto se asignara como variable.
minombre = "Mi nombre es Alvaro"

print(minombre)

#Bucle for
a=0

for  i in range (5):
    a+=1
    print(a)

#Tipos de operadores, Sintaxis Basica 2

#El tipo de variable lo define el contenido, no el continente.

nuevonombre="Javier"
numero=5
decimal=4.5
mensaje="""Esto es un mensaje
con tres saltos
de linea"""

print(mensaje)

numero1=5
numero2=1

#Condicional
if numero1 > numero2:
    print("El numero 1 es mayor")
else:
    print("El numero 2 es mayor")

#Funciones en python: Son estructuras basicas en cualquier lenguaje de programacion. Se trata de un conjunto de lineas
#que funcionan como una unidad realizando una tarea especifica. Las funciones en python pueden devolver valores,
# tener parametros y argumentos, y tambien se conocen como metodos cuando se encuentran definidas dentro de las clases.

#La principal utilidad es poder reutilizar el codigo. La sintaxis es la siguiente:

def primerafuncion():
    print("hola")


def segundafuncion():
    print("a todos")


def mensaje(): #Declaracion
    print("Estamos aprendiendo python")
    print("Aprendiendo nociones basicas")
    print("Poco a poco iremos avanzando")

#Si en el futuro necesitamos que estas tres instrucciones se repitan varias veces a lo largo del programa,
#basta con una funcion. Una funcion no va a realizar el trabajo hasta que no se le llama.

mensaje() #Llamada

#Paso de parametros en funciones. Como podemos hacer que en cada llamada sume unos valores diferentes? Se utilizan parametros o argumentos.

def suma(numero1, numero2):

    print(numero1+numero2)
    print(numero1*numero2)

suma(5,7)

suma(2, 3)

suma(34,356)

#Podemos modificar el codigo de la funcion para que nos devuelva otras cosas.

def operacion(numero3, numero4):
    resultado=numero3*numero4
    return resultado

print(operacion(4,6))

almacena_resultado=operacion(5,8)

print(almacena_resultado)

#Nos permitiria ir utilizando lo que la funcion vaya devolviendo de forma diferente.

almacena_resultado = operacion(4,6)

print(almacena_resultado)










