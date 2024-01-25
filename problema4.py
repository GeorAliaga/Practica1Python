N = int(input("Ingrese un entero positivo N: "))

if N <= 0:
    print("Por favor, ingrese un entero positivo.")
else:
    suma = (N * (N + 1)) // 2

print(f"La suma de todos los enteros desde 1 hasta {N} es: {suma}")
