# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 01:28:12 2021

@author: Andres Giron
"""
def mascaracteres(palabras):
    pos=0
    for x in range(len(palabras)):
        if len(palabras[x])>len(palabras[pos]):
            pos=x
    return palabras[pos]


# bloque principal

palabras=["enero", "febrero", "marzo", "abril", "mayo", "junio"]
print("Palabra con mas caracteres:",mascaracteres(palabras))
