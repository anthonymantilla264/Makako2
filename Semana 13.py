def promedios_ciudades(datos):
    # datos: {"Ciudad": [t_sem1, t_sem2, t_sem3, t_sem4], ...}
    return {ciudad: sum(temps) / len(temps) for ciudad, temps in datos.items()}

# 3 ciudades x 4 semanas
datos = {
    "Machala": [18.0, 19.5, 16.0, 21.8],
    "Pasaje": [21.2, 26.4, 25.9, 24.8],
    "El Cambio": [19.5, 20.1, 17.9, 19.3],
}

print(promedios_ciudades(datos))
