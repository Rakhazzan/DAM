import socket
# PROGRAMA SERVIDOR UDP
# Configuración del servidor UDP
ip_servidor = '127.0.0.1'
puerto_servidor = 12345
# Crear un socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((ip_servidor, puerto_servidor)) # Vincular el socket a una direcció i port
print(f"Servidor UDP esperant a {ip_servidor}:{puerto_servidor}")


try:
    while True:
        # Rebre missatge del client
        dades, direccio_client = sock.recvfrom(1024)  
        missatge_rebut = dades.decode()
        print(f"Missatge rebut del client {direccio_client}: {missatge_rebut}")


        if missatge_rebut.lower() == "exit":
            print("El client ha finalitzat la connexió.")
            break


        # Enviar resposta al client
        resposta = input("Introdueix la resposta per al client: ")
        sock.sendto(resposta.encode(), direccio_client)


        if resposta.lower() == "exit":
            print("Finalitzant el servidor...")
            break


finally:
    sock.close()  # Tancar el socket
