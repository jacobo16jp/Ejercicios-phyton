# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 00:50:59 2021

@author: Andres Giron
"""
def retornar_mayor(v1,v2):
    if v1>v2:
        mayor=v1
    else:
        mayor=v2
    return mayor


# bloque principal
valor1=int(input("Ingrese el primer valor:"))
valor2=int(input("Ingrese el segundo valor:"))
print(retornar_mayor(valor1,valor2))
