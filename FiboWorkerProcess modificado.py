#
# Este script define un hilo que se encarga de calcular la posicion 'n' en la 
# serie de Fibonacci.
#
# Autor: John Sanabria - john.sanabria@correounivalle.edu.co
# Fecha: 2023-01-10
#
from fibonacci import fibo
from time import time
import multiprocessing
import sys

class FiboWorker(multiprocessing.Process):
  def __init__(self, n, pid):
    multiprocessing.Process.__init__(self)
    self.n = n
    self._pid = pid

  def run(self):
    print(f"[{self._pid}] Fibonacci de {self.n} es {fibo(self.n)}")
    return fibo(self.n); #modificacion de la funcion para que retorne valor de fibo
    

def main():
  #modificacion al main
  tiempos=[]
  procesos2=[33]*144
  num_cpus = multiprocessing.cpu_count() # CPUs disponibles
  print(f"Calculando el fibonacci 33 en {num_cpus} CPUs")
  procesos = []*144 # Vector de procesos
  ts = time() # se toma tiempo
  LIMITES=int(144/num_cpus) #Variable para control de limites
  for x in range(num_cpus): # Ciclo para crear trabajadores
    print(f"Trabajador {x} comienza")
    for y in range (x*LIMITES,(x+1)*LIMITES,1):
      
      worker = FiboWorker(procesos2[y],y)
      worker.start()
      procesos2.append(worker)

  #for z in range(num_cpus): # Ciclo para esperar por trabajadores
   # print(f"Esperando por trabajador {z}")
    #procesos[z].join()

  print(f"Tomo {time() - ts}")


if __name__ == "__main__":
  main()
