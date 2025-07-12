import threading
import time

def imprimir_pares():
    for i in range(0, 10, 2):
        print(f"Par: {i}")
        time.sleep(1)

def imprimir_impares():
    for i in range(1, 10, 2):
        print(f"Ímpar: {i}")
        time.sleep(1)

# Criando threads
thread1 = threading.Thread(target=imprimir_pares)
thread2 = threading.Thread(target=imprimir_impares)

# Iniciando as threads
thread1.start()
thread2.start()

# Esperando as threads terminarem
thread1.join()
thread2.join()

print("Execução concorrente finalizada.")
