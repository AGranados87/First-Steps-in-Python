#Ahora vamos a ver un poco mas sobre if, como es la instruccion else:

print("Verificacion de edad.")
edad = input("Introduce tu edad:")


def acceso(edad):
    edad > 18
    if edad < 18:
        print("Eres menor de edad. No puedes pasar.")
    elif edad>100:
        print("Introduce una edad real.")
    else:
        print("Puedes pasar, eres adulto.")


print(acceso(int(edad)))

#Vamos a ver otro ejemplo:

nota_alumno = int(input("Introduce la nota: "))

if nota_alumno < 5 and nota_alumno == 0:
    print("Estas suspenso.")
elif nota_alumno == 5:
    print("Aprobado suficiente.")
elif nota_alumno == 6 or nota_alumno <= 7:
    print("Has sacado un bien")
elif nota_alumno == 7 or nota_alumno == 8:
    print("Has sacado un notable.")
elif nota_alumno == 9 or nota_alumno <= 10:
    print("Sobresaliente.")
else:
    print("Nota incorrecta.")
