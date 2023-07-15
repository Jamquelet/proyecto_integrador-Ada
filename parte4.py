#https://www.dcode.fr/maze-generator  => generar laberinto

"""laberinto = 
..###################
........#.......#...#
###.###.#.###.#####.#
#.#.#.....#...#...#.#
#.#.#.###.#######.#.#
#...#.#.....#.....#.#
#.#########.#.#.###.#
#.#.....#.#...#.....#
#.#.#.###.###.###.###
#.#.#.....#.#.#.....#
#.#.#######.#.#####.#
#.#.#.#.#.#.#.#.....#
#.#.#.#.#.#.#.#.#####
#.......#.....#.#.#.#
#####.#########.#.#.#
#.....#.............#
#.###########.###.#.#
#.#.#.#.....#...#.#.#
#.#.#.#.#.#########.#
#.......#.....#.....#
###################.#  
"""

import os

def convert_map_string(map_string):
    rows = map_string.strip().split("\n")
    map = [list(row) for row in rows]
    return map

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_map(map):
    clear_terminal()
    for row in map:
        print("".join(row))

def main_loop(map, initial_pos, final_pos):
    px, py = initial_pos

    while (px, py) != final_pos:
        display_map(map)

        key = input("Presiona una tecla (w, a, s, d): ")

        if key == 'w':
            new_px = px - 1
            new_py = py
        elif key == 'a':
            new_px = px
            new_py = py - 1
        elif key == 's':
            new_px = px + 1
            new_py = py
        elif key == 'd':
            new_px = px
            new_py = py + 1
        else:
            continue

        if (
            new_px < 0 or new_px >= len(map) or
            new_py < 0 or new_py >= len(map[0]) or
            map[new_px][new_py] == '#'
        ):
            continue

        map[px][py] = '.'
        px = new_px
        py = new_py
        map[px][py] = 'P'

    display_map(map)
    print("¡Felicidades, has llegado al final del laberinto!")

laberinto = """
..###################
........#.......#...#
###.###.#.###.#####.#
#.#.#.....#...#...#.#
#.#.#.###.#######.#.#
#...#.#.....#.....#.#
#.#########.#.#.###.#
#.#.....#.#...#.....#
#.#.#.###.###.###.###
#.#.#.....#.#.#.....#
#.#.#######.#.#####.#
#.#.#.#.#.#.#.#.....#
#.#.#.#.#.#.#.#.#####
#.......#.....#.#.#.#
#####.#########.#.#.#
#.....#.............#
#.###########.###.#.#
#.#.#.#.....#...#.#.#
#.#.#.#.#.#########.#
#.......#.....#.....#
###################.#  
"""

matriz = convert_map_string(laberinto)
matriz[0][0] = "P"

display_map(matriz)

matriz[1][0] = "P"
matriz[0][0] = "."

display_map(matriz)

initial_pos = (0, 0)
final_pos = (len(matriz)-1, len(matriz[0])-1)
main_loop(matriz, initial_pos, final_pos)

#coordenada 20 es el punto 19 es el eje vertical
#print(laberinto.split("\n"))
### Clase
""" matriz = []
for linea in laberinto.split("\n"):
    matriz.append(list(linea))

matriz[0][0] = "P"
#print(matriz)

def mostrar(mapa):
    #join en cadena investigar
    for fila in mapa:
        linea = ""
        for char in fila:
            linea += char
        print(fila)

mostrar(matriz)

matriz[1][0] = "P"
matriz[0][0] = "."
mostrar(matriz)
 """
#iterar 
""" mat = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(mat)
#estas son las cordenadas paso 4
[0][0]
[19][20]
print(mat[2][1]) """
#dibujo para que visualicemos como seria la matriz del laberint
""" (n-1) => x
(n+1) => y """

"""
Implementar una función que reciba el mapa de un laberinto en forma de cadena, y lo convierta a matriz de caracteres.
Para generar los laberintos, usar esta página: https://www.dcode.fr/maze-generator con las configuraciones
USE THIS CHARACTER FOR WALLS: #
USE THIS CHARACTER FOR PATHS: .
SINGLE CHARARACTER (MORE RECTANGULAR)
Completar los dos caracteres de paredes faltantes al final.
Los puntos inicial y final deben ser dados al crear el juego, usar las coordenadas (0,0) para el inicio y (end, end) para el final (Asegurarse que las coordenadas son caminos válidos)
Recuerdo: Para separar por filas usar split("\n") y para convertir una cadena a una lista de caracteres usar list(cadena).
Escribir una función que limpie la pantalla y muestre la matriz (recibe el mapa en forma de matriz)
Implementar el main loop en una función (recibe el mapa en forma de matriz)
recibir: mapa List[List[str]], posicion inicial Tuple[int, int], posicion final Tuple[int, int].
definir dos variavles px y py que contienen las coordenadas del jugador, iniciar como los valores de la posición incial
procesar mientras (px, py) no coincida con la coordenada final.
asignar el caracter P en el mapa a las coordenadas (px, py) en todo momento.
leer del teclado las teclas de flechas, antes de actualizar la posición, verificar si esta posición tentativa:
No se sale del mapa
No es una pared
Si la nueva posición es válida, actualizar (px, py), poner el caracter P en esta nueva coordenada y restaurar la anterior a .
mostrar    
"""
""" 
import os
import msvcrt

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_map(map):
    clear_terminal()
    for row in map:
        print("".join(row))

def main_loop(map, initial_pos, final_pos):
    px, py = initial_pos

    while (px, py) != final_pos:
        display_map(map)

        key = msvcrt.getch().decode('utf-8')

        if key == 'w':
            new_px = px - 1
            new_py = py
        elif key == 'a':
            new_px = px
            new_py = py - 1
        elif key == 's':
            new_px = px + 1
            new_py = py
        elif key == 'd':
            new_px = px
            new_py = py + 1
        else:
            continue

        if (
            new_px < 0 or new_px >= len(map) or
            new_py < 0 or new_py >= len(map[0]) or
            map[new_px][new_py] == '#'
        ):
            continue

        map[px][py] = '.'
        px = new_px
        py = new_py
        map[px][py] = 'P'

    display_map(map)
    print("¡Felicidades, has llegado al final del laberinto!")

def convert_map_string(map_string):
    rows = map_string.strip().split("\n")
    map = [list(row) for row in rows]
    return map

def create_maze_map(end):
    map_string = "##########\n#........#\n#.#.######\n#.#......#\n#.#.######\n#.#.######\n#........#\n##########"
    map_string += "#\n" * (end - 9)
    map_string += "##########"
    return map_string

def start_game():
    end = int(input("Ingrese el tamaño del laberinto (mayor o igual a 10): "))
    map_string = create_maze_map(end)
    map = convert_map_string(map_string)
    initial_pos = (0, 0)
    final_pos = (end, end)
    main_loop(map, initial_pos, final_pos)

if __name__ == "__main__":
    start_game()
 """