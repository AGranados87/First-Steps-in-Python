#Vamos a evaluar el salario de unos empleados de la empresa.

salario_presidente=int(input("Introduce el salario del presidente: "))
print("Salario del presidente: " + str(salario_presidente))

salario_director=int(input("Introduce el salario del director: "))
print("Salario del director: " + str(salario_director))

salario_jefe_area=int(input("Introduce el salario del jefe de area: "))
print("Salario del jefe de area: " + str(salario_jefe_area))

salario_administrativo=int(input("Introduce el salario del administrativo: "))
print("Salario del administrativo: " + str(salario_administrativo))

if salario_administrativo < salario_jefe_area < salario_director < salario_presidente: #Concatenacion de operadores de comparacion.
    print("Todo funciona correctamente.")
else:
    print("Hay un error")

#Vamos a crear un programa que evalue si un alumno tiene derecho a beca o no.

print("Programa de Becas 2024")

#Lo que va a evaluar es la distancia a la que vive el alumno del colegio, el numero de hermanos y el salario familiar.

distancia_colegio = int(input("Introduce la distancia a la que vives del centro: (en Km) "))
numero_hermanos = int(input("Introduce el numero de hermanos: "))
salario_familiar = int(input("Introduce el salario familiar total (en euros): "))

if distancia_colegio > 40 and numero_hermanos > 2 and salario_familiar < 20000: #Operador comparativo and
    print("Enhorabuena, puedes acceder a beca")

else:
    print("No puedes acceder a beca")

#Veamos el operador in (permite evaluar varias condiciones a la vez):

print("Seleccion de Asignaturas Optativas 2024")

print("Asignaturas disponibles: Informatica Grafica - Pruebas de Software - Usabilidad y Accesibilidad")

opcion = input("Escribe la asignatura escogida: ")

asignatura = opcion.lower() #Si se escribe por teclado en minuscula, dara igual porque todo se transformara en minuscula.

if asignatura in ("informatica grafica", "pruebas de software", "usabilidad y accesibilidad"):
    print("Matricula aceptada. Asignatura escogida: " + asignatura)
else:
    print("La asignatura escogida no esta aceptada.")







