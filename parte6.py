""" Reescribir la función que convierte el laberinto de cadena a matriz para que en vez de usar un bucle, haga uso de la función map
Reescribir la función que lee el mapa usando la función readlines para leerlo todo en una sola operación, cargar las coordenadas y usar reduce para concatenar las filas leídas en una sola cadena, en otras palabras sustituir el bucle de lectura del mapa en forma de candena para usar la función reduce. """

import os
import random
from functools import reduce
from readchar import readkey

class Juego:
    def __init__(self, archivo_mapa):
        '''
        Se define la clase Juego. En el constructor (__init__), se guarda el nombre del archivo del mapa, se llama a la función leer_mapa_desde_archivo para cargar el mapa y las posiciones iniciales y finales.'''
        self.archivo_mapa = archivo_mapa
        self.game_map, self.initial_pos, self.final_pos = self.leer_mapa_desde_archivo()

    def leer_mapa_desde_archivo(self):
        '''
        Esta función se encarga de leer el mapa y las coordenadas desde el archivo. Abre el archivo en modo lectura ('r') utilizando un bloque with para asegurarse de que el archivo se cierre correctamente al final. Luego, se utiliza readlines() para leer todas las líneas del archivo y guardarlas en la variable lineas.'''
        with open(self.archivo_mapa, 'r') as archivo:
            lineas = archivo.readlines() #leer todas las lineas del archivo y almacenarlas en la lista lineas
        '''
        Aquí se procesan las líneas leídas del archivo. La primera línea contiene las dimensiones del mapa y se convierte en una tupla de enteros utilizando map(int, lineas[0].split()). Las siguientes líneas representan el mapa y se convierten en una lista de listas de caracteres utilizando map(list, lineas[1:dimensiones[0] + 1]). Luego, se obtienen las coordenadas iniciales y finales convirtiendo las líneas correspondientes en tuplas de enteros.'''
        dimensiones = tuple(map(int, lineas[0].split()))
        game_map = reduce(lambda x, y: x + y, lineas[1:], '')#concatenar las filas del mapa leidas en una sola cadena, la lambda devuelve su concatenacion
        initial_pos = tuple(map(int, lineas[dimensiones[0] + 1].split()))
        final_pos = tuple(map(int, lineas[dimensiones[0] + 2].split()))

        game_map = self.convert_map_string(game_map)
        return game_map, initial_pos, final_pos

    def clear_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def display_map(self):
        '''
        borra la terminal y muestra el mapa actual en la pantalla. Utiliza un bucle for para iterar sobre cada fila del game_map y "".join(row) para convertir la lista de caracteres en una cadena y luego imprimir la fila.'''
        self.clear_terminal()
        for row in self.game_map:
            print("".join(row))

    def main_loop(self):
        px, py = self.initial_pos
        fx, fy = self.final_pos

        while (px, py) != (fx, fy):
            self.display_map()
            key = readkey()

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
                    new_px < 0 or new_px >= len(self.game_map) or
                    new_py < 0 or new_py >= len(self.game_map[0]) or
                    self.game_map[new_px][new_py] == '#'
            ):
                continue

            self.game_map[px][py] = '.'
            px = new_px
            py = new_py
            self.game_map[px][py] = 'P'

        self.display_map()
        print("¡Felicidades, has llegado al final del laberinto!")

class JuegoArchivo(Juego):
    def __init__(self, carpeta_mapas):
        self.carpeta_mapas = carpeta_mapas
        archivo_mapa = self.seleccionar_mapa_aleatorio()
        super().__init__(archivo_mapa)

    def seleccionar_mapa_aleatorio(self):
        archivos_mapas = os.listdir(self.carpeta_mapas)
        archivo_mapa = random.choice(archivos_mapas)
        return os.path.join(self.carpeta_mapas, archivo_mapa)

def main():
    juego = JuegoArchivo('carpeta_de_mapas')
    juego.main_loop()
    print("¡Felicidades, has llegado al final del laberinto!")

if __name__ == "__main__":
    main()
