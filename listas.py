#Veamos las listas. Son una estructura de datos que nos permite almacenar gran cantidad de valores, (similares a los Arrays)
#En python las listas pueden guardar diferente tipos de valores, cosa que no ocurre en otros lenguajes.

videoJuegos=["Doom", "Fallout4", "Skyrim", "Diablo II", "The Last of Us Parte 1", "The Last of Us Parte 2", 55, 45.6, True]

print(videoJuegos)

def listavideojuegos():
    print(videoJuegos)

listavideojuegos() #Hemos creado una funcion que llame a la lista que hemos creado.

#Si queremos acceder a la posicion 3, escribiremos:

print(videoJuegos[3])
#Diablo II

#Si intentamos acceder a un elemento que no esta en la lista se producira una excepcion. Sin embargo, si introducimos
#un indice negativo, Python empieza a contar ese indice desde el final.

print(videoJuegos[-4])
#The Last of Us Parte 1

#Cuando tengamos listas muy largas es posible que queramos acceder a una porcion de una lista.

print(videoJuegos[0:3])
#['Doom', 'Fallout76', 'Skyrim']

#Para agregar elementos al final de la lista, usaremos lo siguiente:

videoJuegos.append("Elden Ring")

print(videoJuegos)
#['Doom', 'Fallout76', 'Skyrim', 'Diablo II', 'The Last of Us Parte 1', 'The Last of Us Parte 2', 55, 45.6, 'Elden Ring']

#Si queremos agregar un elemento en algun punto intermedio, podemos usar la siguiente instruccion:

videoJuegos.insert(3,"Lies of P")

#Le estamos diciendo: en el indice 3, agrega este elemento.

print(videoJuegos)
#['Doom', 'Fallout76', 'Skyrim', 'Lies of P', 'Diablo II', 'The Last of Us Parte 1', 'The Last of Us Parte 2', 55, 45.6, 'Elden Ring']

#Para agregar varios elementos, se utiliza:

videoJuegos.extend(["Uncharted", "Crash Bandicoot", "Dark Souls", "Starfield", "Metal Gear Solid"])

print(videoJuegos)
#['Doom', 'Fallout76', 'Skyrim', 'Lies of P', 'Diablo II', 'The Last of Us Parte 1', 'The Last of Us Parte 2', 55, 45.6, 'Elden Ring', 'Uncharted', 'Crash Bandicoot', 'Dark Souls']

#Para que Python nos devuelva el indice en el que se encuentra un elemento de la lista, haremos lo siguiente:

print(videoJuegos.index("Dark Souls"))
#12

#Comprobar si un elemento se encuentra o no en una lista:

print("Metal Gear Solid" in videoJuegos) #Devolvera True.

#Otra operacion es la eliminacion de elementos. Se utiliza remove.

videoJuegos.remove("Elden Ring")

print(videoJuegos)
#['Doom', 'Fallout76', 'Skyrim', 'Lies of P', 'Diablo II', 'The Last of Us Parte 1', 'The Last of Us Parte 2', 55, 45.6, True, 'Uncharted', 'Crash Bandicoot', 'Dark Souls', 'Starfield', 'Metal Gear Solid']

#Para eliminar el ultimo elemento agregado a la lista, se usa:

videoJuegos.pop()

print(videoJuegos)
#['Doom', 'Fallout76', 'Skyrim', 'Lies of P', 'Diablo II', 'The Last of Us Parte 1', 'The Last of Us Parte 2', 55, 45.6, True, 'Uncharted', 'Crash Bandicoot', 'Dark Souls', 'Starfield']

Retro=["Super Mario Bros", "Tetris", "Kirby", "Donkey Kong"]

#Para unir ambas listas se hace lo siguiente:

union=Retro+videoJuegos

print(union)

#El * funciona a modo de repetidor.

Retro=["Super Mario Bros", "Tetris", "Kirby", "Donkey Kong"] * 3
#['Super Mario Bros', 'Tetris', 'Kirby', 'Donkey Kong', 'Doom', 'Fallout4', 'Skyrim', 'Lies of P', 'Diablo II', 'The Last of Us Parte 1', 'The Last of Us Parte 2', 55, 45.6, True, 'Uncharted', 'Crash Bandicoot', 'Dark Souls', 'Starfield']







