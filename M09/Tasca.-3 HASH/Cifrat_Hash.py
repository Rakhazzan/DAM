import hashlib
import os
import tkinter as tk
from tkinter import messagebox

# Funció per generar el hash de la contrasenya amb SHA-256
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Funció per crear un usuari i guardar el seu hash de contrasenya en el fitxer
def crear_usuari(nom, password):
    password_hash = hash_password(password)
    # Crea o obre l'arxiu "usuaris.txt" en mode afegir
    with open("usuaris.txt", "a") as file:
        file.write(f"{nom},{password_hash}\n")
    messagebox.showinfo("Success", "Usuari creat correctament!")

# Funció per verificar si l'usuari i la contrasenya són correctes
def identificar_usuari(nom, password):
    password_hash = hash_password(password)
    # Comprovar si l'arxiu existeix
    if os.path.exists("usuaris.txt"):
        with open("usuaris.txt", "r") as file:
            for line in file:
                stored_nom, stored_hash = line.strip().split(',')
                if stored_nom == nom and stored_hash == password_hash:
                    return True
    return False

# Funció per manejar el procés de login
def login():
    nom = entry_nom.get()       # Recupera el nom d'usuari de l'entrada
    password = entry_password.get()   # Recupera la contrasenya de l'entrada

    if identificar_usuari(nom, password):
        messagebox.showinfo("Autorització", "Usuari autoritzat!")
    else:
        messagebox.showerror("Error", "Usuari o contrasenya incorrectes.")

# Funció per manejar la creació de nous usuaris
def registre():
    nom = entry_nom.get()       # Recupera el nom d'usuari de l'entrada
    password = entry_password.get()   # Recupera la contrasenya de l'entrada

    if nom and password:  # Comprova que no estiguin buits
        crear_usuari(nom, password)
    else:
        messagebox.showwarning("Advertència", "Tots els camps són obligatoris.")

# Crear la finestra principal
root = tk.Tk()
root.title("Gestió d'Usuaris")   # Títol de la finestra

# Crear etiquetes i camps d'entrada
label_nom = tk.Label(root, text="Nom d'usuari:")  # Etiqueta per al nom
label_nom.grid(row=0, column=0, padx=10, pady=10)  # Posició a la finestra

entry_nom = tk.Entry(root)  # Entrada de text per al nom
entry_nom.grid(row=0, column=1, padx=10, pady=10)

label_password = tk.Label(root, text="Contrasenya:")  # Etiqueta per la contrasenya
label_password.grid(row=1, column=0, padx=10, pady=10)

entry_password = tk.Entry(root, show="*")  # Entrada de text amb ocultació per la contrasenya
entry_password.grid(row=1, column=1, padx=10, pady=10)

# Botons per login i registre
button_login = tk.Button(root, text="Identificar-se", command=login)  # Botó per al login
button_login.grid(row=2, column=0, padx=10, pady=10)

button_registre = tk.Button(root, text="Crear usuari", command=registre)  # Botó per a registrar un nou usuari
button_registre.grid(row=2, column=1, padx=10, pady=10)

# Executar l'aplicació
root.mainloop()  # Mantenir la finestra oberta
