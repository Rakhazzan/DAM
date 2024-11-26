def generar_array_bytes(password):
    return bytearray(password.encode())

def codificar(ruta_original, ruta_cifrado, password):
    pass_bytes = generar_array_bytes(password)
    pass_len = len(pass_bytes)

    with open(ruta_original, "rb") as archivo:
        contenido = archivo.read()

    contenido_codificat = bytearray((contenido[i] + pass_bytes[i % pass_len]) % 256 for i in range(len(contenido)))

    with open(ruta_cifrado, "wb") as archivo_codificat:
        archivo_codificat.write(contenido_codificat)

    print(f"Arxiu codificat guardat com: {ruta_cifrado}")

def descodificar(ruta_codificada, ruta_descifrada, password):
    pass_bytes = generar_array_bytes(password)
    pass_len = len(pass_bytes)

    with open(ruta_codificada, "rb") as archivo:
        contenido = archivo.read()

    contenido_descodificat = bytearray((contenido[i] - pass_bytes[i % pass_len]) % 256 for i in range(len(contenido)))

    with open(ruta_descifrada, "wb") as archivo_descodificat:
        archivo_descodificat.write(contenido_descodificat)

    print(f"Arxiu descodificat guardat com: {ruta_descifrada}")

def main():
    ruta_original = r"C:\Users\Mohamed\Documents\DAM\M09\mario.bmp"
    '''
     En el cas de decodificar cambia el valor de Original per aquest:
     ruta_original = r"C:\Users\Mohamed\Documents\DAM\M09\COD_mario_xor.bmp"
    '''
    ruta_cifrado = r"C:\Users\Mohamed\Documents\DAM\M09\COD_mario_xor.bmp"
    ruta_descifrado = r"C:\Users\Mohamed\Documents\DAM\M09\DEC_mario_xor.bmp"

    password = input("Introdueix la contrasenya:\n")
    opcion = int(input("Opcions:\n 1.- Codificar \n 2.- Descodificar\n"))

    if opcion == 1:
        codificar(ruta_original, ruta_cifrado, password)
    elif opcion == 2:
        descodificar(ruta_cifrado, ruta_descifrado, password)
    else:
        print("¡Opció no vàlida!")

if __name__ == "__main__":
    main()
