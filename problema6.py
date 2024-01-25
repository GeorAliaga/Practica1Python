edad = int(input("Ingrese la edad del cliente: "))

if edad < 4:
    precio_entrada = 0
elif 4 <= edad <= 18:
    precio_entrada = 5
else:
    precio_entrada = 10


print(f"El precio de entrada es: ${precio_entrada}")