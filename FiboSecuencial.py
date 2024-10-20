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
    print(f"[{self._pid}] Fibonacci de {self.n} es {fibo(self.n)}")
    return fibo(self.n); #modificacion de la funcion para que retorne valor de fibo

def main():
  #aca empieza el ejercicio 
  tiempos=[]
  procesos2=[33]*144
  ts1=time()#tiempo ejecucion global ( 144 calculos de fibonacci de manera consecutiva)
  for x in range(len(procesos2)):
    ts = time() # se toma tiempo 
    print(f"Ejecucion {x+1} ")
    trabajador=FiboWorker(procesos2[x],x)
    procesos2[x]=trabajador.run()
    tiempos.append(time()-ts)
    print(f"Tomo {time() - ts}")
  print(f"Tomo en global {time()-ts1}")
  print(tiempos)
                           
  
if __name__ == "__main__":
  main()
