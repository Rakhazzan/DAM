import socket


HOST = '127.0.0.1' #sempre configuració del servidor exemple 192.169.1.8
PORT = 12345


# Crear un socket del client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Conectar al servidor
client_socket.connect((HOST, PORT))


if __name__ == "__main__":
    while True:
        message = input("Client:")
        client_socket.send(message.encode('utf-8'))
        message= client_socket.recv(1024).decode('utf-8')
        print(f"Servidor: {message}")
