#encapsulamiento del juego
import os
import random
from readchar import readkey, key


class Juego:
    def __init__(self, archivo_mapa):
        '''
        constructor, el argumento a_m sera el nombre del archivo del mapa que queremos cargar'''

        self.archivo_mapa = archivo_mapa#se guarda el nombre del archivo en un atributo de la instancia
        self.game_map, self.initial_pos, self.final_pos = self.leer_mapa_desde_archivo()#se llama el metodo leer mapa para cargar el mapa y las posiciones iniciales y finales desde el archivo

    def leer_mapa_desde_archivo(self):
        '''
        lee el contenido del archivo y procesa las lineas para obtener el mapa y las coordenadas'''

        with open(self.archivo_mapa, "r") as archivo:
            '''
            abrimos el archivo en modo lectura'''
            contenido = archivo.read() #lee el contenido completo del archivo en la variable contenido

        lineas = contenido.strip().split('\n') #se divide el contenido en lineas, eliminando los espacios en blanco iniciales y finales con strip(), y con split('\n') para dividir en lineas individuales
        print("líneas leidas: ", lineas) 

        dimensiones = tuple(map(int, lineas[0].split()))#convierte la primera linea en una tupla de enteror, que representa las dimensiones del mapa
        print("Dimensiones: ",dimensiones)

        game_map = [list(row) for row in lineas[1:dimensiones[0]+1]]# crea la matriz del mapa, tomando las siguientes lineas despues de las dimensiones del mapa.Cada fila se convierte en una lista y luego todas las listas se agrupan en una lista mas grande
        print("Mapa del laberinto:", game_map)

        initial_pos = tuple(map(int, lineas[dimensiones[0]+1].split()))#convierte las coordenadas  iniciales de la siguiente linea en una tupla de enteros
        print("Posición inicial:", initial_pos)

        final_pos = tuple(map(int, lineas[dimensiones[0]+2].split()))#convierte las coordenadas finales de la ultima linea en una tupla de enteros
        print("Posición final:", final_pos)

        return game_map, initial_pos, final_pos #devuelve las variables que representan el mapa y las coordenadas
    
    def clear_terminal(self):
        '''
        metodo para limpiar la pantalla de la terminal.detecta si se esta en windows o en otros so'''
        os.system('cls' if os.name == 'nt' else 'clear')

    def display_map(self):
        '''
        metodo que muestra el mapa en la terminal, llama a clear terminal y luego itera sobre cada fila del mapa imprimiendo cada fila en la consola'''
        self.clear_terminal()
        for row in self.game_map:
            print("".join(row))

    def main_loop(self):
        '''
        Metodo principal del juego. Inicializa las coordenadas de inicio y fin. Luego en un bucle muestra el mapa, espera la entrada del user y actualiza la posicion del jugador segun la tecla presionada, el bucle continua hasta que el jugador llega a la posicion final'''
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
        print("¡Felicidades!")


class JuegoArchivo(Juego): #subclase que hereda de Juego
    def __init__(self, carpeta_mapas):
        '''
        constructor de la subclase. Toma un argumento carpeta mapas que representa la carpeta donde estan almacenados los archivos del mapa'''
        self.carpeta_mapas = carpeta_mapas #almacena la ruta de la carpeta en un atributo de la instancia
        archivo_mapa = self.seleccionar_mapa_aleatorio() # llama al metodo para elegir un archivo de mapa al azar de la carpeta
        super().__init__(archivo_mapa) # llama al constructor de la clase base Juego para inicializar el juego con el archivo de mapa seleccionado al azar

    def seleccionar_mapa_aleatorio(self):
        '''
        define el método que elige un archivo de mapa al azar'''
        archivos_mapas = os.listdir(self.carpeta_mapas) #Obtiene la lista de nombres de archivos de la carpeta de mapas
        archivo_mapa = random.choice(archivos_mapas) #elige un archivo al azar de la lista de archivos de mapas
        return os.path.join(self.carpeta_mapas, archivo_mapa) # combina la ruta de la carpeta con el nombre del archivo seleccionado al azar para obtener la ruta completa del archivo del mapa
    
def main():
    '''
    funcion principal que crea una instancia de JuegoArchivo y ejecuta el bucle principal del juego'''
    juego = JuegoArchivo('carpeta_de_mapas')
    juego.main_loop()
    print("¡Felicitaciones!")

if __name__=="__main__": #verifica si el archivo esta siendo ejecutado directamente(no importado como modulo), si es así, llama a la función main() para iniciar el juego
    main()

""" 5 5
#####
#P..#
#.###
#..F#
##### """


""" 7 7
#######
#P#...#
#.#.#.#
#.#.#.#
#.#.#.#
#.#.#.#
#..F..#
 """

"""  0 0 20 20
..###################
....#...............#
#.#.#####.#########.#
#.#...........#.#.#.#
#.#####.#.###.#.#.#.#
#...#.#.#.#.....#...#
#.#.#.#######.#.#####
#.#...#.....#.#...#.#
#####.#####.#.#.###.#
#.#.#.#.......#...#.#
#.#.#.#######.#####.#
#...#...#...#.#.#...#
###.#.#####.#.#.###.#
#.#...#.......#.....#
#.#.#.###.#.#.###.#.#
#...#.#...#.#.....#.#
###.#######.###.###.#
#.#.#.#.#.#...#.#...#
#.#.#.#.#.#.#.#.#.#.#
#.....#.....#.#.#.#.#
###################..
 """

"""  0 0 19 20
..###################
....#.#.#.....#.....#
###.#.#.#.#####.###.#
#.#.....#.#...#.#...#
#.###.###.###.#.#####
#...#...#.#.........#
#.#.###.#.###.#######
#.#.........#.#...#.#
#.#.#.#######.###.#.#
#.#.#.........#.....#
#.###.#.###########.#
#.#.#.#.#.#.#...#...#
#.#.#.###.#.#.#####.#
#.#...#.....#.......#
#.#.#####.#.#.#######
#.#...#.#.#...#.....#
###.###.#.###.#####.#
#.#.......#.......#.#
#.#######.#.###.###.#
#.........#.#.......#
###################.#
 """