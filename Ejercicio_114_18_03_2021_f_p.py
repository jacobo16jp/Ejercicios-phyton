# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 22:42:54 2021

@author: Andres Giron 
"""
# Desarrolar un programa con dos funciones. La primera que solicite el ingreso de un entero y muestre el cuadro de dicho valor. La segunda que solicite dos valores y muestre el producto de los mismos. Llamar desde el bloque del programa principal a ambas funciones.

def calcular_cuadrado () :
    valor=int(input("Ingrese un entero:"))
    cuadrado=valor*valor
    print("El cuadrado es",cuadrado)
    
def calcular_producto () :
    valor1=int(input("Ingrese el primer valor:"))
    valor2=int(input("Ingrese el segundo valor:"))
    producto=valor1*valor2
    print("El producto de los valores es:",producto)

# Bloque principal
    
calcular_cuadrado()
calcular_producto()

    
    
    
    
