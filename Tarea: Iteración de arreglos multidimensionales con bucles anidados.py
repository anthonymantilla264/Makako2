# Dimensiones
ciudades = ["Machala", "Pasaje", "El Guabo"]

# Días de la semana (solo como referencia para la estructura)
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

# Matriz 3D: temperaturas[ciudad][semana][día]
# Ejemplo con 2 semanas y 7 días por semana, valores ficticios en °C
temperaturas = [
    # Machala
    [
        [18.0, 17.5, 19.2, 18.6, 19.0, 17.8, 18.3],  # Semana 1
        [18.4, 18.1, 19.0, 18.7, 19.3, 18.0, 18.5],  # Semana 2
    ],
    # Pasaje
    [
        [22.1, 21.8, 22.5, 22.0, 21.7, 22.3, 21.9],  # Semana 1
        [22.4, 22.0, 22.6, 22.2, 22.1, 22.8, 22.3],  # Semana 2
    ],
    # El Guabo
    [
        [19.5, 19.2, 19.7, 19.4, 19.6, 19.3, 19.5],  # Semana 1
        [19.8, 19.6, 19.9, 19.7, 19.8, 19.6, 19.7],  # Semana 2
    ],
]

# Cálculo de promedios por ciudad y semana
for i_ciudad, ciudad in enumerate(ciudades):                 # 1er nivel: ciudades
    for i_semana, semana in enumerate(temperaturas[i_ciudad]):  # 2º nivel: semanas
        # 3er nivel: días (lista de 7 temperaturas)
        promedio = sum(semana) / len(semana)
        print(f"{ciudad} — Semana {i_semana + 1}: {promedio:.2f} °C")
