numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

print("Seleccione una opción:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")


opcion = input("Ingrese el número de la opción deseada (1, 2, o 3): ")

if opcion == "1":
    resultado = numero1 + numero2
    print(f"La suma de {numero1} y {numero2} es: {resultado}")
elif opcion == "2":
    resultado = numero1 - numero2
    print(f"La resta de {numero1} y {numero2} es: {resultado}")
elif opcion == "3":
    resultado = numero1 * numero2
    print(f"La multiplicación de {numero1} y {numero2} es: {resultado}")
else:
    print("Opción inválida. Por favor, seleccione 1, 2, o 3.")