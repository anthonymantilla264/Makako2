# Paso 1: Crear el diccionario con datos básicos
informacion = {
    "nombre": "Tatiana",
    "edad": 32,
    "ciudad": "Machala",
    "profesion": "Licenciada"
}

# Paso 2: Cambiar la ciudad a una diferente
informacion["ciudad"] = "Cuenca"
# Paso 3: Cambiar o agregar la profesión (ya existe, solo la actualizo)
informacion["profesion"] = "Programadora"
# Paso 4: Verificar si "telefono" existe, y agregarlo si no
if "telefono" not in informacion:
    informacion["telefono"] = "0988997482"
# Paso 5: Eliminar la edad
del informacion["edad"]
# Paso 6: Mostrar el resultado final
print(informacion)
