# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 19:58:45 2021

@author: Andres Giron
"""

def carga_suma () :
    valor1=int(input("Ingrese el primer valor"))
    valor2=int(input("Ingrese el segundo valor:"))
    suma=valor1+valor2
    print("La suma de los dos valores es:",suma)
    
def separacion () :
    print("******************************")
   
# Programa principal
for x in range(5):  
    carga_suma()
    separacion()
    

    