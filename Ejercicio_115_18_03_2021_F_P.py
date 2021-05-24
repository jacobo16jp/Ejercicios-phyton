# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 23:20:34 2021

@author: Andres Giron
"""
def menor_valor():
    valor1=int(input("Ingrese primer valor:"))
    valor2=int(input("Ingrese segundo valor:"))
    valor3=int(input("Ingrese tercer valor:"))    
    print("Menor de los tres")
    if valor1<valor2 and valor1<valor3:
        print(valor1)
    else:
        if valor2<valor3:
            print(valor2)
        else:
            print(valor3)
            

# bloque principal

menor_valor()
menor_valor()
 
