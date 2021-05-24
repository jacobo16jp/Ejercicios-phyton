# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 01:03:25 2021

@author: Andres Giron
"""
def retornar_perimetro(lado):
    perimetro=lado*4
    return perimetro


# bloque principal

lado=int(input("Lado del cuadrado:"))
print("El perimetro es:",retornar_perimetro(lado))

