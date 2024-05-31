nombre = input("Introduce tu nombre: ")

ventas = float(input("Dime las ventas que realizaste este mes: "))

comisiones = ventas * 13/100

print(f"Las comisiones para el empleado {nombre}, por un total de ventas de {ventas} euros, ascienden a {round(comisiones, 2)} euros.")