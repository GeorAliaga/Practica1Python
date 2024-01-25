def mime(nombre_archivo):
    tipos_mime = {
        'gif': 'image/gif',
        'jpg': 'image/jpeg',
        'jpeg': 'image/jpeg',
        'png': 'image/png',
        'pdf': 'application/pdf',
        'txt': 'text/plain',
        'zip': 'application/zip'
    }

    punto_posicion = nombre_archivo.rfind('.')
    if punto_posicion != -1:
        extension = nombre_archivo[punto_posicion + 1:].lower()
        tipo_mime = tipos_mime.get(extension, 'application/octet-stream')
    else:
        tipo_mime = 'application/octet-stream'

    return tipo_mime

nombre_archivo = input("Ingrese el nombre del archivo: ")

tipo_mime = mime(nombre_archivo)
print(f"El tipo MIME para {nombre_archivo} es: {tipo_mime}")