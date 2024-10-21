def codificar(ruta_original, cod_path):
    with open(ruta_original, "rb") as file:
        content = file.read()
    cod = bytearray((byte + 1) % 256 for byte in content)
    with open(cod_path, "wb") as cod_file:
        cod_file.write(cod)

    print(f"Arxiu codificat com: {cod_path}")


def descodificar(cod_path, decod_path):
    with open(cod_path, "rb") as file:
        content = file.read()
    decod = bytearray((byte - 1) % 256 for byte in content)
    with open(decod_path, "wb") as decode_file:
        decode_file.write(decod)

    print(f"Archivo descodificado guardado como: {decod_path}")


def main():
    ori_path = r"C:\Users\Mohamed\Documents\DAM\M09\mario.bmp"
    cod_path = r"C:\Users\Mohamed\Documents\DAM\M09\COD_mario.bmp"
    decod_path = r"C:\Users\Mohamed\Documents\DAM\M09\DEC_mario.bmp"

    option = int(input("Opcio:\n 1.- Codificar \n 2.- Descodificar\n"))

    if option == 1:
        codificar(ori_path, cod_path)
    elif option == 2:
        descodificar(cod_path, decod_path)
    else:
        print("¡Opción no válida!")


if __name__ == "__main__":
    main()
1