def codificar(ruta_original, ruta_cifrado):
    # Abrimos el archivo original en modo lectura binaria y leemos su contenido
    with open(ruta_original, "rb") as archivo:
        contenido = archivo.read()

    # Codificamos sumando 1 a cada byte
    contenido_codificado = bytearray((byte + 1) % 256 for byte in contenido)

    # Guardamos el archivo codificado
    with open(ruta_cifrado, "wb") as archivo_codificado:
        archivo_codificado.write(contenido_codificado)

    print(f"Archivo codificado guardado como: {ruta_cifrado}")


def descodificar(ruta_codificada, ruta_descifrada):
    # Abrimos el archivo codificado en modo lectura binaria y leemos su contenido
    with open(ruta_codificada, "rb") as archivo:
        contenido = archivo.read()

    # Descodificamos restando 1 a cada byte
    contenido_descodificado = bytearray((byte - 1) % 256 for byte in contenido)

    # Guardamos el archivo descodificado
    with open(ruta_descifrada, "wb") as archivo_descodificado:
        archivo_descodificado.write(contenido_descodificado)

    print(f"Archivo descodificado guardado como: {ruta_descifrada}")


def main():
    # Rutas específicas proporcionadas
    ruta_original = r"C:\Users\Mohamed\Documents\DAM\M09\mario.bmp"
    ruta_cifrado = r"C:\Users\Mohamed\Documents\DAM\M09\COD_mario.bmp"
    ruta_descifrado = r"C:\Users\Mohamed\Documents\DAM\M09\DEC_mario.bmp"

    # Pedir al usuario si quiere codificar o descodificar
    opcion = int(input("Opciones:\n 1.- Codificar \n 2.- Descodificar\n"))

    if opcion == 1:
        codificar(ruta_original, ruta_cifrado)
    elif opcion == 2:
        descodificar(ruta_cifrado, ruta_descifrado)
    else:
        print("¡Opción no válida!")


if __name__ == "__main__":
    main()
1