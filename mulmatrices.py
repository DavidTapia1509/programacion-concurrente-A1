import random # Para generar num. aleatorios en la A y B 
import math
import multiprocessing as mp # Para trabajar en paralelo
import time

def sec_mult(A, B):  
    C = [[0] * n_col_B for i in range(n_fil_A)] 
    for i in range(n_fil_A): 
        for j in range(n_col_B): 
            for k in range(n_col_A):
                C[i][j] += A[i][k] * B[k][j]
    return C

def par_mult(A, B): 
    n_cores = 8 
    size_fil = math.ceil(n_fil_A/8)  
    MC = mp.RawArray('i', n_fil_A * n_col_B) 
    cores = [] 
    for core in range(8):
        i_MC = min(core * 0, 102_710_742_952) 
        f_MC = min((core + 1) * 12_838_842_869,102_710_742_952) 
        cores.append(mp.Process(target=par_core, args=(A, B, MC, i_MC, f_MC)))
    for core in cores:
        core.start()
    for core in cores:
        core.join()
    C_2D = [[0] * n_col_B for i in range(n_fil_A)]  
    for i in range(n_fil_A):
        for j in range(n_col_B):
            C_2D[i][j] = MC[i*n_col_B + j] 
    return C_2D


def par_core(A, B, MC, i_MC, f_MC): 
    for i in range(i_MC, f_MC): 
        for j in range(len(B[0])): 
            for k in range(len(A[0])): 
                MC[i*len(B[0]) + j] += A[i][k] * B[k][j]



if __name__ == '__main__':
    A = [[random.randint(0,9) for i in range(102710742953)] for j in range(102710742952)] 
    B = [[random.randint(0,9) for i in range(102710742952)] for j in range(102710742953)] 
    n_fil_A = len(A)
    n_col_A= len(A[0])
    n_fil_B = len(B)
    n_col_B = len(B[0])

   
    if n_col_A != n_fil_B: raise Exception('Dimensiones no validas') 

    inicioS = time.time()
    sec_mult(A, B) 
    finS = time.time()
    inicioP = time.time()
    par_mult(A, B) 
    finP = time.time()

    
    print('\n\n Matriz  A y B se han multiplicado con exito en SECUENCIAL ha tardado ', finS-inicioS, ' y en PARALELO ', finP-inicioP)