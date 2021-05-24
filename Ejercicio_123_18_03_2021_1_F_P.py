# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 00:52:17 2021

@author: Andres Giron
"""
def retornar_promedio(v1,v2,v3):
    promedio=(v1+v2+v3)//3
    return promedio


# bloque principal

valor1=int(input("Ingrese primer valor:"))
valor2=int(input("Ingrese segundo valor:"))
valor3=int(input("Ingrese tercer valor:"))
print("Valor promedio de los tres numeros", retornar_promedio(valor1,valor2,valor3))


