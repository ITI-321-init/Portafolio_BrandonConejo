n = int(input("Ingrese la cantidad de estudiantes encuestados: "))

tabla = {
    "Mucho": [0] * 7,
    "Mediano": [0] * 7,
    "Poco": [0] * 7
}

for i in range(n):
    respuesta = input("Ingrese el nivel de consumo (Mucho, Mediano, Poco): ").capitalize()
    dia = int(input("Ingrese el día de la semana (1-7): "))
    if respuesta in tabla and 1 <= dia <= 7:
        tabla[respuesta][dia - 1] += 1

print("Resultados de la encuesta:")
print("Días:     ", "  ".join(map(str, range(1, 8))))
for categoria, valores in tabla.items():
    print(f"{categoria:10}", "  ".join(map(str, valores)))
