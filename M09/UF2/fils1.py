import time

totalNumerosPrimers = 0

def es_primer(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def buscaNombresPrimers(numeroInici, numeroFinal):
    global totalNumerosPrimers
    for num in range(numeroInici, numeroFinal + 1):
        if es_primer(num):
            print(num, end=" ")
            totalNumerosPrimers += 1
    print()

if __name__ == "__main__":
    numero = int(input("Introdueix un número: "))
    start_time = time.time()
    
    print(f"Nombres primers entre 1 i {numero}:")
    buscaNombresPrimers(1, numero)
    
    elapsed_time = time.time() - start_time
    print(f"Temps d'execució (sense threads): {elapsed_time:.2f} segons")
    print(f"Total nombres primers trobats: {totalNumerosPrimers}")
import time
import threading

totalNumerosPrimers = 0
lock = threading.Lock()

def es_primer(numero):
    """Comprova si un número és primer."""
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def buscaNombresPrimers(numeroInici, numeroFinal):
    """Busca i mostra nombres primers dins un interval."""
    global totalNumerosPrimers
    for num in range(numeroInici, numeroFinal + 1):
        if es_primer(num):
            print(num, end=" ")
            with lock:
                totalNumerosPrimers += 1
    print()

def thread_func(intervals):
    """Funció per dividir la feina entre threads."""
    for interval in intervals:
        buscaNombresPrimers(interval[0], interval[1])

if __name__ == "__main__":
    numero = int(input("Introdueix un número: "))
    num_threads = 4  # Pots variar el nombre de threads
    step = numero // num_threads
    intervals = [(i, min(i + step - 1, numero)) for i in range(1, numero + 1, step)]
    
    threads = []
    start_time = time.time()
    
    for interval in intervals:
        t = threading.Thread(target=buscaNombresPrimers, args=(interval[0], interval[1]))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()
    
    elapsed_time = time.time() - start_time
    print(f"Temps d'execució (amb threads): {elapsed_time:.2f} segons")
    print(f"Total nombres primers trobats: {totalNumerosPrimers}")
