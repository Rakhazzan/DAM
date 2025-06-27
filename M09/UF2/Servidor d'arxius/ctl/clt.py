import socket
import os
import time

# Configuración del cliente
HOST = '127.0.0.1'  # dirección del servidor
PORT = 12345
BUFFER_SIZE = 65536  # Buffer size máximo práctico (64KB)

def receive_file(sock, filename):
    """Recibe un archivo del servidor"""
    try:
        # Enviar solicitud GET
        sock.send(f"GET {filename}".encode())
        
        # Recibir respuesta inicial
        response = sock.recv(BUFFER_SIZE).decode()
        
        # Verificar respuesta
        if response.startswith("ERROR"):
            print(f"Error: {response}")
            return False
            
        # Extraer tamaño del archivo
        parts = response.split(" ")
        if len(parts) != 2 or parts[0] != "OK":
            print(f"Respuesta del servidor inválida: {response}")
            return False
            
        filesize = int(parts[1])
        print(f"Recibiendo archivo: {filename} ({filesize} bytes)")
        
        # Enviar confirmación de listo
        sock.send(b"READY")
        
        # Determinar nombre del archivo de salida
        output_filename = os.path.basename(filename)
        
        # Recibir y guardar el archivo
        with open(output_filename, "wb") as f:
            bytes_received = 0
            start_time = time.time()
            
            while bytes_received < filesize:
                data = sock.recv(min(BUFFER_SIZE, filesize - bytes_received))
                if not data:
                    break
                    
                f.write(data)
                bytes_received += len(data)
                
                # Mostrar progreso cada 1MB
                if bytes_received % 1048576 == 0:
                    print(f"Progreso: {bytes_received / filesize * 100:.1f}%")
            
            end_time = time.time()
            duration = end_time - start_time
            
        # Verificar si se recibió el archivo completo
        if bytes_received == filesize:
            print(f"Archivo recibido completamente: {output_filename}")
            print(f"Tiempo: {duration:.2f} segundos")
            print(f"Velocidad: {filesize / duration / 1024 / 1024:.2f} MB/s")
            return True
        else:
            print(f"Error: archivo incompleto ({bytes_received}/{filesize} bytes)")
            return False
            
    except Exception as e:
        print(f"Error al recibir archivo: {e}")
        return False

# Crear socket del cliente
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 262144)  # 256KB buffer de recepción

# Bucle principal del cliente
if __name__ == "__main__":
    try:
        # Conectar al servidor
        client_socket.connect((HOST, PORT))
        print(f"Conectado al servidor {HOST}:{PORT}")
        
        while True:
            command = input("\nComando (GET archivo.jpg / END): ")
            
            if command.lower() == "end":
                client_socket.send("END".encode())
                print("Cerrando conexión...")
                break
                
            elif command.lower().startswith("get "):
                filename = command[4:].strip()
                if not filename:
                    print("Error: especifica un nombre de archivo")
                else:
                    receive_file(client_socket, filename)
                    
            else:
                print("Comando desconocido. Usa 'GET archivo.jpg' o 'END'")
                
    except ConnectionRefusedError:
        print("Error: No se pudo conectar al servidor. Asegúrate de que esté en ejecución.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()
        print("Conexión cerrada")