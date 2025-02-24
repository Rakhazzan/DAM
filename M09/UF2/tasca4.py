import os
import queue
import threading
from PIL import Image
from cryptography.fernet import Fernet

class JPGCodec:
    def __init__(self, directory, key=None):
        self.directory = directory
        self.file_queue = queue.Queue()
        self.key = key if key else Fernet.generate_key()
        self.cipher = Fernet(self.key)
        
        # Ompli la cua amb arxius jpg
        self._populate_queue()
    
    def _populate_queue(self):
        """Omple la cua amb tots els arxius jpg del directori"""
        for filename in os.listdir(self.directory):
            if filename.lower().endswith('.jpg'):
                self.file_queue.put(filename)
    
    def _process_file(self, is_encode=True):
        """Processa fitxers de la cua"""
        while not self.file_queue.empty():
            try:
                filename = self.file_queue.get_nowait()
                filepath = os.path.join(self.directory, filename)
                
                if is_encode:
                    self._encode_file(filepath)
                else:
                    self._decode_file(filepath)
                
                self.file_queue.task_done()
            except queue.Empty:
                break
    
    def _encode_file(self, filepath):
        """Codifica un arxiu jpg"""
        with open(filepath, 'rb') as file:
            file_data = file.read()
            encrypted_data = self.cipher.encrypt(file_data)
        
        encrypted_filepath = filepath + '.encrypted'
        with open(encrypted_filepath, 'wb') as file:
            file.write(encrypted_data)
        
        os.remove(filepath)
        print(f"Codificat: {filepath}")
    
    def _decode_file(self, filepath):
        """Descodifica un arxiu jpg"""
        if not filepath.endswith('.encrypted'):
            return
        
        with open(filepath, 'rb') as file:
            encrypted_data = file.read()
            decrypted_data = self.cipher.decrypt(encrypted_data)
        
        decrypted_filepath = filepath.replace('.encrypted', '_decrypted.jpg')
        with open(decrypted_filepath, 'wb') as file:
            file.write(decrypted_data)
        
        os.remove(filepath)
        print(f"Descodificat: {filepath}")
    
    def process(self, is_encode=True):
        """Llança 3 processos per codificar/descodificar"""
        threads = []
        for _ in range(3):
            thread = threading.Thread(target=self._process_file, args=(is_encode,))
            thread.start()
            threads.append(thread)
        
        # Espera que tots els threads acabin
        for thread in threads:
            thread.join()
        
        print("Procés completat.")

# Exemple d'ús
def main():
    directory = '/Users/Mohamed/Documents/Tasca4'
    
    # Codificar tots els JPGs
    codec = JPGCodec(directory)
    codec.process(is_encode=True)
    
    # Més tard, per descodificar
    codec = JPGCodec(directory, key=codec.key)
    codec.process(is_encode=False)

if __name__ == '__main__':
    main()