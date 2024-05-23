#Diccionarios. Es una estructura de datos que, a la hora de almacenar los datos, se hace a traves de una asociacion
#clave/valor para cada elemento almacenado. A cada valor se le asigna una clave unica. El tipo de dato que puede almacenar
#un diccionario, incluso se pueden almacenar tuplas, listas, u otro diccionario.

#La sintaxis es simple:

diccionario = {"Noruega": "Oslo", "Alemania": "Berlin", "Rumania": "Bucarest", "Reino Unido": "Londres",
               "Rusia": "Moscu"}

#La clave que se le asocie a cada valor puede ser cualquier tipo: texto, valor numerico etc. Aqui seran de tipo texto.
#Como se puede acceder a los valores? A traves de la clave.

print(diccionario["Rusia"])

#Se pueden hacer muchas cosas. Por ejemplo, agregar mas elementos.

diccionario["Italia"]="Varsovia"
print(diccionario)

#Para modificar un valor para una clave, se haria asi:

diccionario["Italia"]="Roma"
print(diccionario)

#Como podemos eliminar un elemento:

del diccionario ["Alemania"]
print(diccionario)

#Vamos a ver un diccionario donde hay una mezcla en cuanto a tipos.

diccionario={"Alemania":"Berlin", 23:"Jordan", "Metallica":4}
print(diccionario)

#Otra cosa es usar una tupla para asignar las claves a cada uno de los valores.

nuevaTupla=["Espana", "Francia", "Reino Unido", "Alemania"]
nuevoDiccionario={nuevaTupla[0]:"Madrid", nuevaTupla[1]:"Paris", nuevaTupla[2]:"Londres", nuevaTupla[3]:"Berlin"}
print(nuevoDiccionario)
print(nuevoDiccionario["Alemania"])

#Como podemos hacer para que un diccionario almacene una tupla.

otroDiccionario={23:"Jordan", "Nombre": "Michael", "Equipo": "Chicago Bulls", "Anillos": [1991,1992,1996,1997,1998]}
print(otroDiccionario)
print(otroDiccionario["Equipo"])
print(otroDiccionario["Anillos"])

#Por ultimo, podemos guardar un diccionario en otro diccionario.
otroDiccionario={23:"Jordan", "Nombre": "Michael", "Equipo": "Chicago Bulls", "Anillos": {"Temporadas":[1991,1992,1996,1997,1998]}}
print(otroDiccionario)

#Unos cuantos metodos interesantes que se pueden usar con un diccionario son: keys, values, lenght.

print(otroDiccionario.keys()) #Da las claves que pertecen a ese diccionario.
print(otroDiccionario.values())# Da los valores que pertecen a esas claves.
print(len(otroDiccionario)) #La longitud del diccionario.





