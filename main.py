""" import readchar  """

name_player = input("Escribe el nombre para tú jugador: ")
print("Bienvenido", name_player, "diviertete en esta nueva aventura")

dificultad = input("En que nivel quieres empezar: -Dificil -Medio -Bajo --> ")
print("Tú modo de juego sera:", dificultad)

mundo = input("En que mundo te sientes mas comodo: -Ogrimmar -Entrañas -Ventormenta --> ")
print("Te esperan grandes aventuras en", mundo, ",", name_player, "se valiente y asegurate de equiparte. ")

#ejemplo 3 pero no tiene en cuenta las teclas hacia abajo y hacia los lados pero cumple
from readchar import readkey, key

while True:
    char = readkey()
    print("Tecla presionada: ", char)

    if char == key.UP:
        print("Se presionó la tecla ↑ (UP).")
        break

print("¡Fin del programa!")


#documentacion readchar
""" from readchar import readkey, key

while True:
  k = readkey()
  if k == "a":
    # do stuff
    if k == key.DOWN:
    # do stuff
      if k == key.ENTER:
        break """


#muestra por consola la tecla presionada ejemplo 1 el ciclo no se rompe al dar tecla hacia arriba
""" while True:
    char = readchar.readchar()
    print("Tecla presionada: ", char)

    #
    if char == '\x1b[A': #Código de tecla para UP ↑(arriba)
        break
print("Se presionó la tecla ↑. ¡Fin del programa!")

 """
#segunda solucion con error de ejecucion
""" # Leer y detectar la tecla "↑" (UP)
while True:
    key = readchar.readkey()
    char = readchar.key.key_to_escape_sequence(key)

    if char == '\x1b[A':
        print("Se presionó la tecla ↑ (UP).")
        break
    else:
        print("Carácter leído:", char)
 """


