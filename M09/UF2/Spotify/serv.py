import socket
import threading
import os
import json

HOST = 'localhost'
PORT = 12345
MUSIC_DIR = 'music'
USER_DB = 'users.json'

def load_users():
    if os.path.exists(USER_DB):
        with open(USER_DB, 'r') as f:
            return json.load(f)
    return {}

def client_handler(conn, addr):
    print(f"[CONNEXIÓ] {addr}")

    users = load_users()
    conn.sendall(b'Username: ')
    username = conn.recv(1024).decode().strip()
    conn.sendall(b'Password: ')
    password = conn.recv(1024).decode().strip()

    if username not in users or users[username]["password"] != password:
        conn.sendall(b'Authentication failed.\n')
        conn.close()
        return

    conn.sendall(b'Authentication successful.\n')

    song_list = os.listdir(MUSIC_DIR)
    conn.sendall(json.dumps(song_list).encode())

    while True:
        song_name = conn.recv(1024).decode().strip()
        if song_name == 'exit':
            break
        song_path = os.path.join(MUSIC_DIR, song_name)
        if os.path.exists(song_path):
            with open(song_path, 'rb') as f:
                while chunk := f.read(1024):
                    conn.sendall(chunk)
            conn.sendall(b'__END__')  # signal end of file
        else:
            conn.sendall(b'File not found.')

    conn.close()

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"[SERVIDOR] Escoltant a {HOST}:{PORT}")
        while True:
            conn, addr = s.accept()
            threading.Thread(target=client_handler, args=(conn, addr), daemon=True).start()

if __name__ == "__main__":
    start_server()
