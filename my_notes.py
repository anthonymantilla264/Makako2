# Mi tarea de PROGRAMACION
# Por: [ANTHONY_MANTILLA]

# Escribir archivo
print("Creando mi archivo...")

mi_archivo = open("my_notes.txt", "w")
mi_archivo.write("Me gusta estudiar programación y también microsoldadura\n")
mi_archivo.write("Los archivos en Python son útiles para empezar a programar\n")
mi_archivo.write("Esta tarea fue fácil de hacer gracias a la informacion en la plataforma\n")
mi_archivo.close()

print("Archivo my_notes.txt creado!")

# Leer archivo
print("Ahora voy a leer mi archivo:")

mi_archivo = open("my_notes.txt", "r")

# Usar readline() como pide la tarea
nota1 = mi_archivo.readline()
nota2 = mi_archivo.readline() 
nota3 = mi_archivo.readline()

print("Primera línea:", nota1.strip())
print("Segunda línea:", nota2.strip())
print("Tercera línea:", nota3.strip())

mi_archivo.close()
print("¡Listo!")
