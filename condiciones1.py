#Veamos las estructuras de control de flujo. Comenzamos por if. Vamos a introducir un codigo que nos va a permitir introducir informacion por teclado.
#Introduciremos la nota para que entre en el programa que se almacene en una variable.

print("Programa de Evaluacion de Notas de Alumnos.")

nota_alumno = input()


def evaluacion(nota):
    valoracion = "Aprobado"
    if nota < 5:
        valoracion = "Suspenso"
    return valoracion


#print(evaluacion(nota_alumno))

#Esto dara un error porque el valor que hemos introducido por teclado como un valor de texto, todo valor introducido como
#input sera texto. Lo que tenemos que hacer es decirle a nuestro programa que lo que introduzcamos en input sea un valor
#numerico, mediante la funcion int().

print(evaluacion(int(nota_alumno)))

#La funcion input puede admitir parametros. Por ejemplo, un mensaje.

print("Programa de Evaluacion de Notas de Alumnos.")

nota_alumno = input("Introduce la nota del alumno: ")


def evaluacion(nota):
    valoracion = "Aprobado"
    if nota < 5:
        valoracion = "Suspenso"
    return valoracion

print(evaluacion(int(nota_alumno)))