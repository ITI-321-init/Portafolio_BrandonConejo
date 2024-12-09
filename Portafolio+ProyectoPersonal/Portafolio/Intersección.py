def union_vectores(v1, v2):
    return list(set(v1) | set(v2))

def interseccion_vectores(v1, v2):
    return list(set(v1) & set(v2))

vector1 = list(map(int, input("Ingrese los elementos del vector 1 separados por espacios: ").split()))
vector2 = list(map(int, input("Ingrese los elementos del vector 2 separados por espacios: ").split()))

union = union_vectores(vector1, vector2)
interseccion = interseccion_vectores(vector1, vector2)

print(f"Unión: {union}")
print(f"Intersección: {interseccion}")
