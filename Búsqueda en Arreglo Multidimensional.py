# busqueda_matriz.py

# Matriz 3x3 de ejemplo
matriz = [
    [3, 5, 7],
    [1, 9, 2],
    [8, 6, 4],
]

def buscar_valor(matriz, objetivo):
    """
    Recorre la matriz y devuelve (True, (fila, columna)) si encuentra el objetivo,
    o (False, None) en caso contrario.
    """
    for i, fila in enumerate(matriz):          # i = índice de fila
        for j, valor in enumerate(fila):       # j = índice de columna
            if valor == objetivo:
                return True, (i, j)
    return False, None

OBJETIVO = 7  # Cambiar este número para probar otros casos

encontrado, pos = buscar_valor(matriz, OBJETIVO)

if encontrado:
    print(f"Valor {OBJETIVO} encontrado en la posición (fila={pos}, columna={pos[1]}).")
else:
    print(f"Valor {OBJETIVO} no encontrado en la matriz.")
