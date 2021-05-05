import concurrent.futures
import multiprocessing as mp
import time
import random






def merge_sort (a) :

    if len(a) < 2:
      return a
    
    # De lo contrario, se divide en 2
    else:
        middle = len(a) // 2
        right = merge_sort(a[:middle])
        left = merge_sort(a[middle:])
        return merge(right, left)
    
# Función merge
def merge(a1, a2):
    """
    merge se encargara de intercalar los elementos de las dos
    divisiones.
    """
    i, j = 0, 0 # Variables de incremento
    result = [] # Lista de resultado
 
   # Intercalar ordenadamente
    while(i < len(a1) and j < len(a2)):
        if (a1[i] < a2[j]):
            result.append(a1[i])
            i += 1
        else:
            result.append(a2[j])
            j += 1
 
   # Agregamos los resultados a la lista
    result += a1[i:].copy()
    result += a2[j:].copy()

    # Retornamos el resultado
    return result
def par_mergesort(a,*args ):
    
    if not args:
        shared_array = mp.RawArray('i', a)
        par_mergesort(shared_array)
        return parallel_result
    else:
        args=left,right,depth
        n_cores = 8# Obtengo los cores de mi pc
    
        if (depth >= math.log(8, 2)):
            seq_mergesort(a, left,right)
        
        elif (left< right):
            mid= (left + right) //2
            left_proc = mp.Process(target=par_mergesort,args=(a, left, mid, depth+1))
            left_proc.start()
            par_mergesort(a.mid+1,right, depth+1)
            left_proc.join()
            
            merge(a, izq, mid,dcha)

# Prueba del algoritmo
if __name__ == '__main__':
    inicioS = time.time()
    
    a = [random.randint(0, 9) for i in range(21931950)]
    merge_sort_result = merge_sort(a)  
    finS = time.time()
    print( "el tiempo en secuencial  es :   ",finS-inicioS)
    
    
    

    print('Evaluando Paralelo...')
    inicioP = time.time()
    a = [random.randint(0, 9) for i in range(21931950)]
    parallel_result= par_mergesort(a)
    finP = time.time() 

    print('Tiempo paralelo:  ',finP - inicioP)
    