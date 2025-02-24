import socket
# PROGRAMA SERVIDOR UDP
# Configuración del servidor UDP
ip_servidor = '192.168.1.37'
puerto_servidor = 12345
# Crear un socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((ip_servidor, puerto_servidor)) # Vincular el socket a una
print(f"Servidor UDP esperant a {ip_servidor}:{puerto_servidor}")
try:
datos, direccion_cliente = sock.recvfrom(1024) # S'espera aquí
mensaje_recibido = datos.decode()
6
print(f"Mensaje recibido del cliente {direccion_cliente}:
{mensaje_recibido}")
finally:
sock.close() # Tancar el socket
import socket
# PROGRAMA CLIENT
# Configuración del servidor UDP
ip_servidor = '192.168.1.37'
puerto_servidor = 12345
# Crear un socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
mensaje = "Hola, servidor UDP!"
sock.sendto(mensaje.encode(), (ip_servidor, puerto_servidor)) #
finally:
sock.close() # Cerrar el socketa