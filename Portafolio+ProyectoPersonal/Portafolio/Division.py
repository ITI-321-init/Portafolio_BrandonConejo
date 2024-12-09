def division_entera(dividendo, divisor):
    cociente = 0
    while dividendo >= divisor:
        dividendo -= divisor
        cociente += 1
    return cociente, dividendo

dividendo = int(input("Ingrese el dividendo: "))
divisor = int(input("Ingrese el divisor: "))
cociente, residuo = division_entera(dividendo, divisor)
print(f"Cociente: {cociente}, Residuo: {residuo}")