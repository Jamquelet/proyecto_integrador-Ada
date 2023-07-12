###### PARTE 3 DEL PROYECTO INTEGRADOR 

"""
Iniciar con un número en 0, leer la tecla `n` del teclado en un bucle, por cada presionada, borrar la terminal y e imprimir el nuevo número hasta el número 50.

La operación de borrar la terminal e imprimir el nuevo número debe estar en su propia función.

Para borrar la terminal antes de imprimir nuevo contenido usar la instrucción: os.system('cls' if os.name=='nt' else 'clear'), para esto se debe importar la librería os
"""

import os

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    number = 0
    while number <= 50:
        clear_terminal()
        print(number)
        input("Presiona la tecla 'n' para continuar...")
        number += 1

if __name__ == "__main__":
    main()

""" La función clear_terminal() utiliza os.system() para borrar la terminal antes de imprimir el nuevo contenido. La instrucción 'cls' if os.name == 'nt' else 'clear' verifica si el sistema operativo es Windows (nt) y utiliza el comando cls para borrar la terminal, de lo contrario, utiliza el comando clear para sistemas operativos Unix.
La función main() inicia con el número en 0 y ejecuta un bucle while que se repite hasta que el número alcanza el valor de 50.
Dentro del bucle, se llama a clear_terminal() para borrar la terminal y luego se imprime el valor actual de number.
Después, se utiliza input() para esperar a que el usuario presione la tecla 'n' y continuar la ejecución del bucle.
Por último, se incrementa el valor de number en 1 en cada iteración del bucle.
Puedes ejecutar este código en tu terminal y presionar la tecla 'n' para ver cómo se borra la terminal y se imprime el nuevo número en cada iteración hasta llegar a 50. 
La línea de código if __name__ == "__main__": es una convención común en Python y se utiliza para determinar si el archivo actual está siendo ejecutado como un programa principal o si está siendo importado como un módulo en otro programa."""