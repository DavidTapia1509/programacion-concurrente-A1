import concurrent.futures
import multiprocessing as mp
import time

def fibo_sinparalelo(n):
    a=0
    b=1

    for k in range(n):
        c= a+b
        a=b
        b=c

    return b

def fibo_paralelo(n):
    if n<= 0:
        return 0

    i = n-1
    a,b = 1,0
    c,d= 0,1

    while i>0:
        if i%2 == 1:
            a,b= d*b + c*a, d*(b+a) + c*b
        c,d=c**2 + d**2, d*(2*c+d)
        i= i/2
        
    return a+b



if __name__ == '__main__':
    inicioS = time.time()
    for x in range(21931950):
        
       print(fibo_sinparalelo(x), end="," )
    finS = time.time()
    print("\n el tiempo que tarda recursivamente es :   ",finS-inicioS) 
    
    print("\n")


    inicioP = time.time()
    for x in range(21931950):
        print(fibo_paralelo(x), end=",")
    finP = time.time()
    #print(fibo_iter(n), end="," )
    print("\n el tiempo que tarda paralelamente es :   ",finP-inicioP) 


