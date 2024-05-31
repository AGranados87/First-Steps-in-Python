texto = input("Introduce un texto: ")
letra1 = input("Introduce una primera letra: ")
letra2 = input("Introduce una segunda letra: ")
letra3 = input("Introduce una tercera letra: ")

print("La primera letra se repite " + str(texto.count(letra1)) + " veces." +" La segunda: " + str(texto.count(letra2)) + " veces."+" y la tercera: " + str(texto.count(letra3)))

print("El texto tiene una longitud de " + str(len(texto.split())) + " palabras.")

print("La primera letra es " + texto[0] + ".")
print("La ultima letra es " + texto[-1] + ".")
reves = texto.split(" ")
reves.reverse()
print("Asi quedaria el texto en orden invertido: " + str(reves))

boolean = "Python" == texto

