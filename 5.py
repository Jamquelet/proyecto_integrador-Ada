import os
import random
from readchar import readkey, key as k

class Juego:
    def __init__(self, mapa_filename):
        self.mapa_filename = mapa_filename
        self.mapa, self.initial_pos, self.final_pos = self.load_map()

    def load_map(self):
        with open(self.mapa_filename, 'r') as f:
            data = f.read().strip().split('\n')
            initial_pos = tuple(map(int, data[0].split(',')))
            final_pos = tuple(map(int, data[1].split(',')))
            mapa = data[2:]
        return mapa, initial_pos, final_pos

    def display_map(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        for row in self.mapa:
            print(row)

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
                new_px < 0 or new_px >= len(self.mapa) or
                new_py < 0 or new_py >= len(self.mapa[0]) or
                self.mapa[new_px][new_py] == '#'
            ):
                continue

            self.mapa[px] = self.mapa[px][:py] + '.' + self.mapa[px][py + 1:]
            px = new_px
            py = new_py
            self.mapa[px] = self.mapa[px][:py] + 'P' + self.mapa[px][py + 1:]

        self.display_map()
        print("¡Felicidades, has llegado al final del laberinto!")

mapa_filename = "mapa1.txt"
juego = Juego(mapa_filename)
juego.main_loop()
print("¡Felicidades, has llegado al final del laberinto!")
