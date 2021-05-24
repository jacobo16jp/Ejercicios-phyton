# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 00:36:29 2021

@author: Andres Giron
"""
def retornar_superficie(lado):
    sup=lado*lado
    return sup


# bloque principal del programa

va=int(input("Ingrese el valor del lado del cuadrado:"))
superficie=retornar_superficie(va)
print("La superficie del cuadrado es",superficie)
