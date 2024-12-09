matriz1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matriz2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

matriz_suma = [[matriz1[i][j] + matriz2[i][j] for j in range(len(matriz1[0]))] for i in range(len(matriz1))]
matriz_resultados = [[matriz_suma[i][j] * 2 for j in range(len(matriz_suma[0]))] for i in range(len(matriz_suma))]

print("Matriz 1:")
for fila in matriz1:
    print(fila)

print("Matriz 2:")
for fila in matriz2:
    print(fila)

print("Matriz Suma:")
for fila in matriz_suma:
    print(fila)

print("Matriz Resultados:")
for fila in matriz_resultados:
    print(fila)
