def codificar(ruta_original, ruta_cifrado ):
    try:
        # Obrim l'arxiu original en mode lectura binària
        with open(ruta_original, "rb") as arxiu:
            contingut = arxiu.read()

        # Codifiquem afegint 1 a cada byte
        contingut_codificat = bytearray((byte + 1) % 256 for byte in contingut)

        # Guardem l'arxiu codificat
        with open(ruta_cifrado , "wb") as arxiu_codificat:
            arxiu_codificat.write(contingut_codificat)

        print(f"Arxiu codificat guardat com: {ruta_cifrado }")
    except Exception as e:
        print(f"Error en codificar l'arxiu: {e}")


def descodificar(nom_arxiu_entrada, nom_arxiu_sortida):
    try:
        # Obrim l'arxiu codificat en mode lectura binària
        with open(nom_arxiu_entrada, "rb") as arxiu:
            contingut = arxiu.read()

        # Descodifiquem restant 1 a cada byte
        contingut_descodificat = bytearray((byte - 1) % 256 for byte in contingut)

        # Guardem l'arxiu descodificat
        with open(nom_arxiu_sortida, "wb") as arxiu_descodificat:
            arxiu_descodificat.write(contingut_descodificat)

        print(f"Arxiu descodificat guardat com: {nom_arxiu_sortida}")
    except Exception as e:
        print(f"Error en descodificar l'arxiu: {e}")


def main():
    user_input = input("Opcions\n 1.- Codificar \n 2.- Descodificar\n")
    option = int(user_input)

    if option == 1:
        # Sol·licitar el nom del fitxer a codificar
        nom_arxiu = input("Introdueix el nom de l'arxiu a codificar (per exemple: dibuix.jpg):\n")
        nom_arxiu_sortida = "COD_" + nom_arxiu
        codificar(nom_arxiu, nom_arxiu_sortida)
    elif option == 2:
        # Sol·licitar el nom del fitxer ja codificat
        nom_arxiu = input("Introdueix el nom de l'arxiu codificat (per exemple: COD_dibuix.jpg):\n")
        nom_arxiu_sortida = "DEC_" + nom_arxiu[4:]  # Treu "COD_" per obtenir el nom original
        descodificar(nom_arxiu, nom_arxiu_sortida)
    else:
        print("Opció no vàlida!")


if __name__ == "__main__":
    main()
ruta_original = r"C:\Users\Mohamed\Documents\DAM\M09\mario.bmp"
ruta_cifrado = r"C:\Users\Mohamed\Documents\DAM\M09\COD_mario_xor.bmp"
ruta_descifrado = r"C:\Users\Mohamed\Documents\DAM\M09\DEC_mario_xor.bmp"