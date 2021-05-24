# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 23:50:19 2021

@author: Andres Giron
"""
def mostrar_perimetro(lado) :
    peri=lado*4
    print("El perimetro es",peri)
    
def mostrar_superficie(lado):
    sup=lado*lado
    print("La superficie es",sup)

def cargar_dato():
    La=int(input("Ingrese el valor del lado de un cuadrado:"))
    respuesta=input("Quiere calcular el perimetro o la superficie[ingresar texto: perimetro/superficie]?")
    if respuesta=="perimetro":
        mostrar_superficie(La)
        
        
        
    
