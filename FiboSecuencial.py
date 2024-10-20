#
# Este script define un hilo que se encarga de calcular la posicion 'n' en la 
# serie de Fibonacci.
#
# Autor: John Sanabria - john.sanabria@correounivalle.edu.co
# Fecha: 2023-01-10
#
from fibonacci import fibo
from time import time
import sys

class FiboWorker(): #modificamos para que no use multiprocesamiento o threads
  def __init__(self, n, pid):
    self.n = n
    self._pid = pid

  def run(self):
    print(f"[{self._pid}] Fibonacci ")
    return fibo(self.n); #modificacion de la funcion para que retorne valor de fibo

def main():
  #aca empieza el ejercicio 
  tiempos=[0]*5
  for y in range(5):  
    ts1=time()#tiempo ejecucion global ( 144 calculos de fibonacci de manera consecutiva)
    procesos2=[33]*144
    for x in range(len(procesos2)): 
      print(f"Ejecucion {x+1} ")
      trabajador=FiboWorker(procesos2[x],x)
      procesos2[x]=trabajador.run()
    tiempos[y]=(time()-ts1)
  # Ordenamos los tiempos, eliminamos el mayor y el menor
  tiempos.sort()
  tiempos_filtrados = tiempos[1:-1]                  
  # Calculamos el promedio de los tiempos restantes
  promedio = sum(tiempos_filtrados) / len(tiempos_filtrados)
  print(f"Tiempos originales: {tiempos}")
  print(f"Tiempos filtrados (sin el mayor y menor): {tiempos_filtrados}")
  print(f"Promedio de los tres tiempos restantes: {promedio:.5f} segundos")


  
if __name__ == "__main__":
  main()
