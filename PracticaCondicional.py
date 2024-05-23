# Crea un programa que pida dos números por teclado. El programa tendrá una función llamada “DevuelveMax” encargada
# de devolver el número más alto de los dos introducidos.

numero1 = input("Introduce un numero: ")
numero2 = input("Introduce un segundo numero: ")


def DevuelveMax():
    if numero1 > numero2:
        print("El numero mas alto es " + numero1)

    elif numero1 == numero2:
        print("Ambos numeros son iguales.")
    else:
        print("El numero mas alto es " + numero2)


DevuelveMax()

#Crea un programa que pida por teclado “Nombre”, “Dirección” y “Tfno”.
#Esos tres datos deberán ser almacenados en una lista y mostrar en consola el mensaje:
#Los datos personales son: nombre apellido teléfono”
#(Se mostrarán los datos introducidos por teclado).


nombre = input("Introduce tu nombre: ")
direccion = input("Introduce tu direccion: ")
Tfno = input("Introduce tu numero de telefono: ")

datospersonales = ["Nombre: ", "Direccion: ", "Telefono: "]
tupla = {datospersonales[0]: nombre, datospersonales[1]: direccion, datospersonales[2]: Tfno}

print("Tus datos personales son: " + str(tupla))

#Crea un programa que pida tres números por teclado. El programa imprime en consola la media aritmética de los números introducidos.

numero1 = int(input("Introduce un numero:"))
numero2 = int(input("Introduce un numero:"))
numero3 = int(input("Introduce un numero:"))

suma = numero1 + numero2 + numero3
aritmetica = suma/3

print(str(aritmetica))
