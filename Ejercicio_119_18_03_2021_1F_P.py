# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 00:11:40 2021

@author: Andres Giron
"""
def cantidad_vocales(cadena):
    cant=0
    for x in range (len(cadena)):
        if cadena[x]=="a" or cadena[x]=="e" or cadena [x]=="i" or cadena[x]=="u":
            cant=cant+1
    print("Cantidad de vocales de la palabra", cadena,"es", cant)
            
# Bloque princial 
cantidad_vocales("caminar")
cantidad_vocales("Andres")
cantidad_vocales("correr")


