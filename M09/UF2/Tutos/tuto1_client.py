import socket
# PROGRAMA CLIENT
# Configuración del servidor UDP (NO LA DEL CLIENT)
ip_servidor = '127.0.0.1'
puerto_servidor = 12345
# Crear un socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
    while True:
        # Enviar missatge al servidor
        missatge = input("Introdueix un missatge per al servidor: ")
        sock.sendto(missatge.encode(), (ip_servidor, puerto_servidor))


        if missatge.lower() == "exit":
            print("Finalitzant el client...")
            break


        # Rebre resposta del servidor
        dades, _ = sock.recvfrom(1024)
        resposta_servidor = dades.decode()
        print(f"Resposta del servidor: {resposta_servidor}")


        if resposta_servidor.lower() == "exit":
            print("El servidor ha finalitzat la connexió.")
            break


finally:
    sock.close()  # Tancar el socket
