consumo = float(input("Ingrese su consumo: "))
porcentaje_propina = float(input("Ingrese el porcentaje de propina que desea dejar: "))

propina = consumo * (porcentaje_propina / 100)
print(f"Debe dejar ${propina:.2f} como propina.")
