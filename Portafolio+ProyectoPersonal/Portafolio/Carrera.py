import threading
import time
import random

class Competidor(threading.Thread):
    def __init__(self, nombre, color, fila):
        super().__init__()
        self.nombre = nombre
        self.color = color
        self.fila = fila
        self.posicion = 0

    def run(self):
        while self.posicion < 20:
            time.sleep(random.uniform(0.1, 0.5))
            self.posicion += 1
            self.mostrar_pista()

    def mostrar_pista(self):
        pista = "---|" * self.posicion + "(X)" + "---|" * (20 - self.posicion)
        print(f"\033[{self.color}m{self.nombre:10} {pista}\033[0m")

competidores = [
    Competidor("Pericles", "31", 1),  # Rojo
    Competidor("Morticia", "32", 2),  # Verde
    Competidor("Merlina", "33", 3),   # Amarillo
    Competidor("Fétido", "34", 4),    # Azul
    Competidor("Homero", "35", 5)     # Magenta
]

print("Pista de Carreras\n")
print("Salida" + " " * 65 + "Meta\n")

for competidor in competidores:
    competidor.start()

for competidor in competidores:
    competidor.join()

resultados = sorted(competidores, key=lambda x: x.posicion, reverse=True)
print("\nPodium de Ganadores:")
for i, competidor in enumerate(resultados[:3], 1):
    print(f"{i}. {competidor.nombre} con tiempo: {competidor.posicion:.2f} segundos")
