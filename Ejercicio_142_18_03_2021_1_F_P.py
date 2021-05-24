# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 01:46:20 2021

@author: Andres Giron
"""
def tabla(numero, terminos=10):
    for x in range(terminos):
        va=x*numero
        print(va,",",sep="",end="")
    print()
    

# bloque principal

print("Tabla del 3")
tabla(3)
print("Tabla del 3 con 5 terminos")
tabla(3,5)
print("Tabla del 3 con 20 terminos")
tabla(terminos=20,numero=3)

