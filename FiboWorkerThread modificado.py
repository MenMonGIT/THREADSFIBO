from threading import Thread
from fibonacci import fibo
import time 

class FiboWorkerThread(Thread):
    def __init__(self, vector, index):
        Thread.__init__(self)
        self.vector = vector
        self.index = index

    def run(self):
        self.vector[self.index] = fibo(self.vector[self.index])

def concurrente_fibonacci_thread():
    vector = [33] * 144
    hilos = []
    for i in range(len(vector)):
        hilo = FiboWorkerThread(vector, i)
        hilo.start()
        hilos.append(hilo)

    for hilo in hilos:
        hilo.join()

    return vector

if __name__ == "__main__":
    tiempos = []

    # Realizamos 5 ejecuciones y medimos los tiempos
    for x in range(5):
        inicio = time.time()  # Usamos time.time() en lugar de timeit.default_timer()
        concurrente_fibonacci_thread()
        fin = time.time()
        tiempos.append(fin - inicio)

    # Ordenamos los tiempos, eliminamos el mayor y el menor
    tiempos.sort()
    tiempos_filtrados = tiempos[1:-1]

    # Calculamos el promedio de los tiempos restantes
    promedio = sum(tiempos_filtrados) / len(tiempos_filtrados)

    print(f"Tiempos originales: {tiempos}")
    print(f"Tiempos filtrados (sin el mayor y menor): {tiempos_filtrados}")
    print(f"Promedio de los tres tiempos restantes: {promedio:.5f} segundos")
