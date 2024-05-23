#Las tuplas son estructuras parecidas a las listas con restricciones. Son listas que no cambian, inmutables. Es igual que
#una lista pero no se puede modificar. Hay que tener en cuenta que los metodos anteriores no tienen cabida con las tuplas.
#Si que permiten extraer fragmentos, por ejemplo. No permiten busquedas, pero si comprobar si un elemento se encuentra dentro.

#En general, las tuplas son mas rapidas, ocupan menos espacio, formatean Strings y pueden utilizarse como claves en un diccionario.
#La sintaxis es la siguiente:

miTupla=("Metallica", "Iron Maiden", "Gojira", "Mastodon")

miTupla.index("Gojira")

#Podemos convertir una tupla en lista, y viceversa, mediante el metodo list.

miLista=list(miTupla)

#Al reves, se usa el metodo tuple.

listaGrupos = ["Le Mur", "Rage Against the Machine"]

#Para contar cuantas veces se encuentra un elemento.

print(listaGrupos.count("Le Mur"))

#Para saber cuantos elementos hay

print(len(listaGrupos))

#Desempaquetado de tuplas.

nuevatupla=("Alvaro", 11,5,1987)
nombre, dia, mes, agno = nuevatupla

print(nombre, dia, mes, agno)