# eOrdenación de Arreglo Multidimensional.py

# Matriz 3x3
matriz = [
    [9, 3, 7],
    [5, 8, 1],
    [4, 6, 2],
]

def ordenar_fila(m, i):
    # Bubble Sort in-place sobre la fila i
    fila = m[i]
    n = len(fila)
    for _ in range(n - 1):
        for j in range(n - 1):
            if fila[j] > fila[j + 1]:
                fila[j], fila[j + 1] = fila[j + 1], fila[j]

print("Matriz original:")
for f in matriz:
    print(f)

fila_objetivo = 1  # 0, 1 o 2
ordenar_fila(matriz, fila_objetivo)

print("\nMatriz con la fila ordenada (fila =", fila_objetivo, "):")
for f in matriz:
    print(f)
