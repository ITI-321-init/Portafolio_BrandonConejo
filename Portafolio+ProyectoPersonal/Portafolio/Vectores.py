import random

numero = random.randint(15, 30)
vectores = [[0] * 3 for _ in range(4)]

for i in range(4):
    print(f"Llenando vector {i + 1}")
    for j in range(3):
        vectores[i][j] = int(input(f"Ingrese un valor para la posición {j + 1}: "))

suma_vectores = [sum(vector) for vector in vectores]
numeros_usados = set(num for vector in vectores for num in vector)
validacion_suma = all(suma == numero for suma in suma_vectores)
valores_no_repetidos = len(numeros_usados) == 12

print(f"Número generado: {numero}")
print(f"Suma de cada vector: {suma_vectores}")
print("La suma de los vectores es válida." if validacion_suma else "Error en la suma de los vectores.")
print("No hay números repetidos entre los vectores." if valores_no_repetidos else "Hay números repetidos entre los vectores.")
