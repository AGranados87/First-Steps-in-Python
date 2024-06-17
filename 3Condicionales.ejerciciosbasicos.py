"1. Escribe un programa que pida al usuario un número y determine si es par o impar."

numero = int(input("Dame un numero: "))

if numero % 2 == 0:
    print("Es par")
else:
    print("Es impar")

"2. Crea un programa que pida tres números al usuario y muestre el mayor de ellos."

num1 = int(input("Introduce un numero: "))
num2 = int(input("Introduce un segundo numero: "))
num3 = int(input("Introduce un tercer numero: "))

if num1 > num2 and num3:
    print(f"El numero mas alto de los introducidos es {num1}")
elif num2 > num1 and num3:
    print(f"El numero mas alto es {num2}")
elif num3 > num2 and num1:
    print(f"El numero mas alto es {num3}")
if num1 == num2 == num3:
    print(f"Es el mismo numero.")

"3. Escribe un programa que pida al usuario su edad y determine si es mayor de edad."

edad = int(input("Introduce tu edad: "))

if edad >= 18:
    print("Eres mayor de edad.")
elif edad < 18:
    print("Eres menor de edad.")

"4. Crea un programa que pida al usuario una contraseña y verifique si es correcta."

password = "melocoton"
clave = input("Introduce la contraseña: ")

if password != clave:
    print("Contraseña incorrecta.")
else:
    print("Contraseña correcta.")

"5. Escribe un programa que determine si un número ingresado por el usuario es divisible por 3 y por 5."

numero = int(input("Introduce un numero para saber si es divisible por tres o cinco: "))

if numero % 3 == 0:
    print("El numero es divisible por tres.")
elif numero % 5 == 0:
    print("El numero es divisible por 5")
else:
    print("El numero no es divisible por ninguno de los dos.")

"6. Crea un programa que determine si un año ingresado por el usuario es bisiesto."

anio = int(input("Introduce un año para saber si es bisiesto: "))

if anio % 4 == 0 and anio % 100 != 0:
    print(f"{anio} es bisiesto.")
else:
    print(f"{anio} no es bisiesto. ")

"7. Escribe un programa que pida al usuario una nota y muestre si está aprobado (nota >= 5)."

nota = int(input("Introduce la nota: "))

if nota >= 5:
    print("Aprobaste.")
else:
    print("Estas suspenso.")

"8. Crea un programa que pida al usuario dos números y determine si son iguales."

num1 = int(input("Introduce un numero: "))
num2 = int(input("Introduce otro numero: "))

if num1 == num2:
    print("Estos numeros son iguales.")
else:
    print("No son iguales.")

"9. Escribe un programa que pida al usuario un carácter y determine si es una vocal."

letra = input("Introduce una caracter: ")
vocales = ["a", "e", "i", "o", "u"]

if letra.isalpha():
    print("Es una letra.")
elif letra.isalnum():
    print("Es un numero.")
for i in vocales:
    if letra == i:
        print(f"Es una vocal, la {letra}")

"10. Crea un programa que pida al usuario tres números y los ordene de mayor a menor."

num1 = input("Introduce un numero: ")
num2 = input("Introduce otro numero: ")
num3 = input("Introduce un tercer numero: ")

ordenar = sorted([num1, num2, num3])

print(ordenar)


