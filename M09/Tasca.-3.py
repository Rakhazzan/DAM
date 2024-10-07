import tkinter as tk
from tkinter import messagebox
import hashlib
import os

USER_FILE = "usuaris.txt"

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def crear_usuari():
    nom = entry_nom.get()
    password = entry_password.get()
    hashed_password = hash_password(password)
    

    with open(USER_FILE, "a") as f:
        f.write(f"{nom},{hashed_password}\n")
    
    messagebox.showinfo("Info", "Usuari creat amb èxit!")

def identificar_usuari():
    nom = entry_nom.get()
    password = entry_password.get()
    hashed_password = hash_password(password)

    if not os.path.exists(USER_FILE):
        messagebox.showerror("Error", "No hi ha cap usuari registrat!")
        return

    with open(USER_FILE, "r") as f:
        for line in f:
            saved_nom, saved_hashed_password = line.strip().split(",")
            if saved_nom == nom and saved_hashed_password == hashed_password:
                messagebox.showinfo("Autorització", "AUTORITZAT")
                return
    
    messagebox.showerror("Error", "Usuari o password incorrecte")

root = tk.Tk()
root.title("Gestió d'Usuaris")

label_nom = tk.Label(root, text="Nom d'usuari:")
label_nom.grid(row=0, column=0)
entry_nom = tk.Entry(root)
entry_nom.grid(row=0, column=1)

label_password = tk.Label(root, text="Contrasenya:")
label_password.grid(row=1, column=0)
entry_password = tk.Entry(root, show="*")
entry_password.grid(row=1, column=1)

button_crear = tk.Button(root, text="Crear Usuari", command=crear_usuari)
button_crear.grid(row=2, column=0)

button_identificar = tk.Button(root, text="Identificar-se", command=identificar_usuari)
button_identificar.grid(row=2, column=1)

root.mainloop()
