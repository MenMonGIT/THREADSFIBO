from multiprocessing import Process, Array
from time import time
from fibonacci import fibo

class FiboWorker(Process):
    def __init__(self, vector):
        Process.__init__(self)
        self.vector = vector

    def run(self):
        result = fibo(33)  # Calcula Fibonacci de 33
        for i in range(len(self.vector)):
            self.vector[i] = result  # Almacena el resultado en todo el vector

def main():
    total_times = []
    ejecuciones = 5
    vector_length = 144
    ts1 = time()  # Tiempo total de ejecución

    for x in range(ejecuciones):
        ts = time()  # Tiempo de cada ejecución
        vector = Array('i', [0] * vector_length)  # Crea un array compartido para el vector

        # Crea y lanza el proceso
        worker = FiboWorker(vector)
        worker.start()
        worker.join()  # Espera que el proceso termine

        print(f"Ejecución {x + 1}:")
        print(f"Vector: {[vector[i] for i in range(vector_length)]}")  # Muestra el vector
        tiempo_ejecucion = time() - ts  # Tiempo de ejecución individual
        total_times.append(tiempo_ejecucion)

        print(f"Tomo {tiempo_ejecucion:.4f} segundos\n")

    tiempo_total = time() - ts1  # Tiempo total de todas las ejecuciones
    print(f"Tomo en global {tiempo_total:.4f} segundos")
    print("Tiempos de cada ejecución:", total_times)

    # Descarta el tiempo más corto y el más largo
    if len(total_times) > 2:
        total_times.remove(min(total_times))  # Elimina el tiempo más corto
        total_times.remove(max(total_times))  # Elimina el tiempo más largo

    # Calcula el promedio de los tiempos restantes
    promedio_tiempo = sum(total_times) / len(total_times) if total_times else 0
    print(f"Promedio de tiempos (sin el más corto y el más largo): {promedio_tiempo:.4f} segundos")

if __name__ == "__main__":
    main()

