import tkinter as tk
from tkinter import messagebox
import threading
import time
import pygame

def alarma():
    pygame.mixer.init()
    pygame.mixer.music.load("alarm.mp3")  
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():  
        continue



class TemporitzadorsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Temporitzadors")

  
        self.threads = []

 
        self.label = tk.Label(root, text="Introdueix els segons:")
        self.label.pack()

        self.entry = tk.Entry(root)
        self.entry.pack()


        self.set_button = tk.Button(root, text="SET", command=self.crea_temporitzador)
        self.set_button.pack()

        self.clear_button = tk.Button(root, text="CLEAR ALL", command=self.clear_all)
        self.clear_button.pack()

    def crea_temporitzador(self):
        try:
            segons = int(self.entry.get())
            if segons <= 0:
                raise ValueError("El temps ha de ser positiu.")
        except ValueError:
            messagebox.showerror("Error", "Introdueix un número vàlid de segons.")
            return


        t = threading.Thread(target=self.temporitzador, args=(segons,))
        t.start()
        self.threads.append(t)

    def temporitzador(self, segons):
        time.sleep(segons)
        alarma()

    def clear_all(self):

        for t in self.threads:
            if t.is_alive():
                t.join(0)  
        self.threads.clear()
        messagebox.showinfo("CLEAR ALL", "Tots els temporitzadors s'han esborrat.")


if __name__ == "__main__":
    root = tk.Tk()
    app = TemporitzadorsApp(root)
    root.mainloop()
