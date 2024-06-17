import math

"1. Crea un programa que pida al usuario dos números y muestre la suma, resta, multiplicación y división de ellos."

num1 = int(input("Dame un numero: "))
num2 = int(input("Dame otro numero: "))

resultado = num1 + num2 , num1 - num2, num1 % num2, num1 * num2

print(resultado)

"2. Escribe un programa que calcule el área de un triángulo dado su base y altura proporcionados por el usuario."

def areatriangulo(altura, base):
    area = altura * base / 2
    print(area)
    return area

areatriangulo(6, 3)

"3. Crea un programa que convierta grados Celsius a Fahrenheit."

def conversor(fahrenheit):
    celsius = (fahrenheit - 32) * (5/9)
    print(round(celsius, 1))
    return celsius

conversor(80)

"4. Escribe un programa que calcule el perímetro de un rectángulo dados su largo y ancho"

def rectangulo(l, a):
    p = 2 * (l+a)
    print(p)
    return p

rectangulo(14, 8)

"5. Crea un programa que calcule la raíz cuadrada de un número ingresado por el usuario."

def raizcuadrada(n):
    res = n**0.5
    print(res)
    return res

raizcuadrada(25)

"6. Escribe un programa que determine si un número ingresado por el usuario es positivo, negativo o cero."

numero = int(input("Introduce el numero: "))

if numero > 0:
    print("Es positivo")
elif numero < 0:
    print("Es negativo")
else:
    print("Es cero")

"7. Crea un programa que pida al usuario el radio de un círculo y calcule su área."

def circulo(radio):
    area = math.pi * pow(radio, 2)
    print(round(area, 3))
    return area

circulo(5)

"8. Escribe un programa que calcule el volumen de una esfera dado su radio."

def esfera(r):
    v = 4/3 * math.pi * pow(r, 3)
    print(round(v, 2))
    return v

esfera(4)

"9. Crea un programa que determine el residuo de la división de dos números ingresados por el usuario."

def residuo(num1, num2):
    resultado = num1 % num2
    print(resultado)
    return resultado

residuo(26, 7)

"10. Escribe un programa que calcule la hipotenusa de un triángulo rectángulo dados los otros dos lados."

def hipotenusa(l1, l2):
    h = (pow(l1, 2) + pow(l2, 2)) ** 0.5
    print(round(h, 1))
    return h

hipotenusa(3, 4)













