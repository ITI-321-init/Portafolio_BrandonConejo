def es_numero_perfecto(numero):
    suma_divisores = sum(i for i in range(1, numero) if numero % i == 0)
    return suma_divisores == numero

numero = int(input("Ingrese un número entero: "))
if es_numero_perfecto(numero):
    print(f"El número {numero} es un número perfecto.")
else:
    print(f"El número {numero} no es un número perfecto.")
