import socket
import threading
import tkinter as tk
from tkinter import simpledialog, messagebox
import pygame
import tempfile

HOST = 'localhost'
PORT = 12345

class MusicClient:
    def __init__(self, root):
        self.root = root
        self.root.title("Client de Música")
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.selected_song = None
        self.temp_file = None

        try:
            self.sock.connect((HOST, PORT))
        except Exception as e:
            messagebox.showerror("Error", f"No s'ha pogut connectar: {e}")
            root.destroy()
            return

        self.authenticate()
        self.setup_ui()
        self.get_song_list()

    def authenticate(self):
        user = simpledialog.askstring("Login", "Usuari:")
        pwd = simpledialog.askstring("Contrasenya", "Contrasenya:", show='*')
        self.sock.recv(1024)  # Username prompt
        self.sock.sendall(user.encode() + b'\n')
        self.sock.recv(1024)  # Password prompt
        self.sock.sendall(pwd.encode() + b'\n')
        response = self.sock.recv(1024).decode()
        if "failed" in response:
            messagebox.showerror("Error", "Autenticació fallida")
            self.root.destroy()

    def setup_ui(self):
        self.listbox = tk.Listbox(self.root)
        self.listbox.pack(fill=tk.BOTH, expand=True)
        self.listbox.bind('<<ListboxSelect>>', self.on_select)

        self.play_button = tk.Button(self.root, text="▶ Reproduir", command=self.play_selected_song, state=tk.DISABLED)
        self.play_button.pack(pady=10)

        pygame.mixer.init()

    def get_song_list(self):
        song_data = self.sock.recv(4096).decode()
        self.song_list = eval(song_data)
        for song in self.song_list:
            self.listbox.insert(tk.END, song)

    def on_select(self, event):
        selection = self.listbox.curselection()
        if selection:
            self.selected_song = self.song_list[selection[0]]
            self.play_button.config(state=tk.NORMAL)

    def play_selected_song(self):
        if not self.selected_song:
            return

        self.sock.sendall(self.selected_song.encode())
        self.temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
        while True:
            data = self.sock.recv(1024)
            if b'__END__' in data:
                break
            self.temp_file.write(data)
        self.temp_file.close()

        pygame.mixer.music.load(self.temp_file.name)
        pygame.mixer.music.play()

if __name__ == "__main__":
    root = tk.Tk()
    app = MusicClient(root)
    root.mainloop()
