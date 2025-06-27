import socket
import os

# Configuración del servidor
HOST = '127.0.0.1'  # localhost
PORT = 12345
BUFFER_SIZE = 65536  # Buffer size máximo práctico (64KB)

# Crear el socket del servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Optimizar el socket para transferencias grandes
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 262144)  # 256KB buffer de envío
server_socket.bind((HOST, PORT))
server_socket.listen(5)
print(f"Servidor escuchando en {HOST}:{PORT}")

def send_file(conn, filename):
    """Envía un archivo al cliente"""
    try:
        # Comprobar si el archivo existe
        if not os.path.exists(filename):
            conn.send("ERROR: Archivo no encontrado".encode())
            return False
            
        # Obtener tamaño del archivo
        filesize = os.path.getsize(filename)
        print(f"Enviando archivo: {filename} ({filesize} bytes)")
        
        # Enviar respuesta positiva con el tamaño del archivo
        conn.send(f"OK {filesize}".encode())
        
        # Esperar confirmación del cliente
        response = conn.recv(BUFFER_SIZE)
        if response != b"READY":
            print(f"Error: El cliente no está listo, recibido: {response}")
            return False
            
        # Abrir y enviar el archivo
        with open(filename, "rb") as f:
            bytes_read = f.read(BUFFER_SIZE)
            while bytes_read:
                conn.sendall(bytes_read)
                bytes_read = f.read(BUFFER_SIZE)
        
        print(f"Archivo {filename} enviado completamente")
        return True
    except Exception as e:
        print(f"Error al enviar archivo: {e}")
        return False

def handle_client(conn, addr):
    """Maneja la conexión con un cliente"""
    print(f"Nueva conexión: {addr}")
    
    try:
        while True:
            # Recibir comando del cliente
            data = conn.recv(BUFFER_SIZE)
            if not data:
                break
                
            command = data.decode('utf-8')
            print(f"Comando recibido: {command}")
            
            # Procesar comando GET
            if command.startswith("GET "):
                filename = command[4:].strip()
                send_file(conn, filename)
            
            # Procesar comando END
            elif command == "END":
                print("Cliente solicitó cerrar conexión")
                break
            
            # Comando desconocido
            else:
                conn.send("ERROR: Comando desconocido".encode())
    except Exception as e:
        print(f"Error en la conexión con {addr}: {e}")
    finally:
        conn.close()
        print(f"Conexión con {addr} cerrada")

# Bucle principal del servidor
if __name__ == "__main__":
    try:
        while True:
            conn, addr = server_socket.accept()
            handle_client(conn, addr)
    except KeyboardInterrupt:
        print("\nServidor detenido")
    finally:
        server_socket.close()