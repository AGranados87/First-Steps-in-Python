"""Parte 1: Conceptos Básicos de Python
1.1 Impresión y Variables"""

"1.Escribe un programa que imprima ¡Hola, Mundo!"

print("Hola mundo")

"2. Declara dos variables, a y b, y asígnales los valores 5 y 10 respectivamente. Imprime sus valores."

a = 5
b = 10

print(a, b)

"3. Declara una variable nombre, asignale tu nombre y luego imprime Hola, tu nombre"

nombre = "Alvaro"

print("Hola " + nombre)

"4. Crea un programa que solicite al usuario su edad y luego imprima Tienes [edad] años."

edad = input("Dime tu edad: ")
print(f"Tienes {edad} años.")

"5. Declara dos variables, x y y, y asígnales valores numéricos. Imprime su suma."

x = 10
y = 20

suma = x + y

print(suma)

"6. Escribe un programa que solicite el nombre y la edad del usuario, y luego imprima un mensaje combinando estos datos."

nombre = input("Dime tu nombre: ")
edad = input("Dime tu edad: ")

print(f"Hola, {nombre}, tu edad es de {edad} años.")

"7. Crea un programa que pida al usuario dos números y luego imprima su producto."

num1 = int(input("Dame un numero: "))
num2 = int(input("Dame otro numero: "))

producto = num1 * num2

print(producto)

"8. Declara una variable mensaje con el valor ¡Buenos días! y luego imprímela."

mensaje = "¡Buenos dias!"

print(mensaje)

"9. Escribe un programa que intercambie los valores de dos variables y luego imprima los nuevos valores."

var1 = 10
var2 = 20

print(f"Valores de las var1 y var2 respectivamente: ", var1, var2)

var1, var2 = var2, var1

print(f"Nuevos valores de var1 y var 2: ", var1, var2)

"10. Declara tres variables con diferentes tipos de datos (int, float, str) e imprímelas en una sola línea."

a = 1
b = "hola"
c = 23.5

print("Valores: ", a,b,c)