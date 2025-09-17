#Fuuncion
def calcular_descuento(monto_total, porcentaje_descuento=5):
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento
#Llamado de la funcion
monto1 = 200
monto2 = 150

# Primera llamada: (5% de Descuento)
descuento1 = calcular_descuento(monto1)
monto_final1 = monto1 - descuento1

# Segunda llamada: (15% de Descuento)
descuento2 = calcular_descuento(monto2, 15)
monto_final2 = monto2 - descuento2

# Mostrar resultados
print("RESULTADOS DE DESCUENTOS")
print(f"\nPrimera compra:")
print(f"Monto total: ${monto1}")
print(f"Descuento aplicado (5%): ${descuento1}")
print(f"Monto final a pagar: ${monto_final1}")

print(f"\nSegunda compra:")
print(f"Monto total: ${monto2}")
print(f"Descuento aplicado (10%): ${descuento2}")
print(f"Monto final a pagar: ${monto_final2}")







