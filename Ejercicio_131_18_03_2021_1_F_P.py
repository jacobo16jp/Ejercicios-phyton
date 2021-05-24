# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 01:29:39 2021

@author: Andres Giron
"""
def producto(lista):
    prod=1
    for x in range(len(lista)):
        prod=prod*lista[x]
    return prod


# bloque principal

lista=[1, 2, 3, 4, 5]
print("Lista:", lista)
print("Multiplicacion de todos sus elementos:",producto(lista))

