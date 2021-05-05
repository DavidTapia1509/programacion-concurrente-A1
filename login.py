import time
import os
import sys
import sqlite3
import getpass
import mulmatrices
import mergesort
import fibo
 
#declaracion de variables
 
registeredUser = ('david_tapia_yepes@hotmail.com')
registeredPW = ('21931950')
 
#declaracion de funciones
def login(usuario,passw):
    if usuario in registeredUser:
        if passw in registeredPW:
            return 1
        else:
            print("\n\tPassword does not match...\n")
    else:
        return 2
        
opcion=0

def menu(opcion):
    
    opcion = input("Selecciona una opción")
    if opcion==1:
	    print ("\t1 - primera opción")
    os.system("mulmatrices.py")
    
    if opcion==2:
          print ("\t2 - segunda opción")
    os.system("mergesort.py")
    if opcion==3:
	    print ("\t3 - tercera opción")
    os.system("fibo.py")
    if opcion==4:
	    print ("\t4 - salir")
    

if __name__ == '__main__': 
 #inicializacion de procesos
    print('Introduzca su correo')
    usuario=input('User: ')
    passw = getpass.getpass('Password: ')
    
    if login(usuario,passw)==1:
        menu=menu(opcion)
        print('Welcome ',usuario)
        
    else:
        print('ERROR! User no encontrado.')



