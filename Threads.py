from threading import Thread
from fibonacci import fibo
import time 

class FiboWorkerThread(Thread):
    def __init__(self, vector, index):
        Thread.__init__(self)
        self.vector = vector
        self.index = index

    def run(self):
	# Calcular Fibonacci y almacenar en la posición correspondiente
        self.vector[self.index] = fibo(self.vector[self.index])

def concurrente_fibonacci_thread():
    vector = [33] * 144
    hilos = []
    for i in range(len(vector)):
        hilo = FiboWorkerThread(vector, i) # Crear un hilo para cada índice
        hilo.start() # Iniciar el hilo
        hilos.append(hilo) # Añadir a la lista de hilos

    # Esperar a que todos los hilos terminen
    for hilo in hilos:
        hilo.join() # Esperar a que todos los hilos terminen

    return vector

if __name__ == "__main__":
    tiempos = []

    # Realizamos 5 ejecuciones y medimos los tiempos
    for _ in range(5):
        inicio = time.time()
        resultado = concurrente_fibonacci_thread()  # Ejecutar la función con hilos
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

    # Imprimir el resultado final
    print("Resultados de Fibonacci en el vector:")
    print(resultado)  # Muestra el arreglo final
