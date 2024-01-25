
time = input("Ingrese la hora en formato de 24 horas: ")
hours, minutes = time.split(":")
hora_numerica = float(hours + "." + minutes)

if 7.0 <= hora_numerica <= 8.0:
    print("Es hora de desayunar.")
elif 12.0 <= hora_numerica <= 13.0:
    print("Es hora de almorzar.")
elif 18.0 <= hora_numerica <= 19.0:
    print("Es hora de cenar.")
else:
    pass
