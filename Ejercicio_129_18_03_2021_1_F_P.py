# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 01:26:51 2021

@author: Andres Giron 
"""
def multiplicar(lista,va):
    for x in range(len(lista)):
        multi=lista[x]*va
        print(multi)


# bloque principal

lista=[3, 7, 8, 10, 2]
print("Lista original:",lista)
print("Lista multiplicando cada elemento por 3")
multiplicar(lista,3)

