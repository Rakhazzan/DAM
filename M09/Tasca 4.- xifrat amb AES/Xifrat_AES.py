import os
import tkinter as tk
from tkinter import filedialog, messagebox
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import os

def generar_clau_iv(password):
    # Genera la clau i el IV (Initialization Vector) a partir de la contrasenya
    password_bytes = password.encode()
    salt = b'\x00' * 16  # Aquest salt es pot fer dinàmic per més seguretat
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = kdf.derive(password_bytes)
    iv = os.urandom(16)  # IV ha de ser aleatori per a cada codificació
    return key, iv

def codificar(ruta_original, ruta_cifrado, password):
    key, iv = generar_clau_iv(password)

    with open(ruta_original, "rb") as archivo:
        contenido = archivo.read()

    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    contenido_codificat = iv + encryptor.update(contenido) + encryptor.finalize()

    with open(ruta_cifrado, "wb") as archivo_codificat:
        archivo_codificat.write(contenido_codificat)

    messagebox.showinfo("Codificació", f"Arxiu codificat guardat com: {ruta_cifrado}")

def descodificar(ruta_codificada, ruta_descifrada, password):
    key, iv = generar_clau_iv(password)

    with open(ruta_codificada, "rb") as archivo:
        contenido = archivo.read()

    iv = contenido[:16]  # Extraure el IV al començament del fitxer
    contenido_encrypted = contenido[16:]

    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    contenido_descodificat = decryptor.update(contenido_encrypted) + decryptor.finalize()

    with open(ruta_descifrada, "wb") as archivo_descifrat:
        archivo_descifrat.write(contenido_descodificat)

    messagebox.showinfo("Descodificació", f"Arxiu descodificat guardat com: {ruta_descifrada}")

def seleccionar_fitxer():
    return filedialog.askopenfilename()

def guardar_com(ruta_original):
    # Obtener la extensión del archivo original
    extension = os.path.splitext(ruta_original)[1]
    # Pedir al usuario la ubicación para guardar el archivo con la extensión original
    return filedialog.asksaveasfilename(defaultextension=extension, filetypes=[("All files", "*.*")])

def main_ui():
    root = tk.Tk()
    root.title("Encriptació AES en mode CFB")

    tk.Label(root, text="Contrasenya:").grid(row=0, column=0, padx=5, pady=5)
    entry_password = tk.Entry(root, show="*")
    entry_password.grid(row=0, column=1, padx=5, pady=5)

    def executar_codificacio():
        ruta_original = seleccionar_fitxer()
        if ruta_original:
            ruta_cifrado = guardar_com(ruta_original)  # Usa la extensión original
            password = entry_password.get()
            codificar(ruta_original, ruta_cifrado, password)

    def executar_descodificacio():
        ruta_codificada = seleccionar_fitxer()
        if ruta_codificada:
            ruta_descifrada = guardar_com(ruta_codificada)  # Usa la extensión original
            password = entry_password.get()
            descodificar(ruta_codificada, ruta_descifrada, password)

    tk.Button(root, text="Codificar", command=executar_codificacio).grid(row=1, column=0, padx=5, pady=5)
    tk.Button(root, text="Descodificar", command=executar_descodificacio).grid(row=1, column=1, padx=5, pady=5)

    root.mainloop()

if __name__ == "__main__":
    main_ui()
