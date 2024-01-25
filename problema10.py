lista_muestra = ['Rojo', 'Verde', 'Blanco', 'Negro', 'Rosa', 'Amarillo']
posiciones_a_eliminar = [0, 4, 5]
print("Lista inicial:", lista_muestra )
for posicion in sorted(posiciones_a_eliminar, reverse=True):
    if 0 <= posicion < len(lista_muestra):
        lista_muestra.pop(posicion)

print("Lista Resultante:", lista_muestra)