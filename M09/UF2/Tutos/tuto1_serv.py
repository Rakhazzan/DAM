import socket
# Configuració del servidor
host = '127.0.0.1'
port = 12345


# Crear socket del servidor TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen()
print(f"Servidor lissen a {host}:{port}")
client_socket, client_address = server_socket.accept()  #quan accepta una connexio assigna un socket al client


if __name__ == "__main__":
    while True:
        message = client_socket.recv(1024)
        print (f"Client: {message}")
        message = input("Servidor:")
        client_socket.send(message.encode("utf-8"))