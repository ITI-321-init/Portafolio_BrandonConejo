import threading
import time
import random

class Cajero(threading.Thread):
    def __init__(self, nombre, lista_compras, color):
        super().__init__()
        self.nombre = nombre
        self.lista_compras = lista_compras
        self.color = color

    def run(self):
        total = 0
        for producto, precio in self.lista_compras.items():
            time.sleep(random.uniform(0.5, 1.5))
            total += precio
            print(f"\033[{self.color}m{self.nombre:10} Procesó: {producto} - ₡{precio:.2f}\033[0m")
        print(f"\033[{self.color}m{self.nombre:10} Total: ₡{total:.2f}\033[0m")

lista_compras = {
    "Manzanas": 1500,
    "Leche": 900,
    "Huevos": 1800,
    "Pan": 1000,
    "Jugo": 1200
}

cajeros = [
    Cajero("Cajero 1", lista_compras, "31"),  # Rojo
    Cajero("Cajero 2", lista_compras, "32"),  # Verde
    Cajero("Cajero 3", lista_compras, "36")   # Celeste
]

for cajero in cajeros:
    cajero.start()

for cajero in cajeros:
    cajero.join()
