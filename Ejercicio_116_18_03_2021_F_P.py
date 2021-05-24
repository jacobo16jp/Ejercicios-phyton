# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 23:25:01 2021

@author: Andres Giron
"""
def mostrar_mensaje(mensaje):
    print("*************************************************")
    print(mensaje)
    print("*************************************************")

def carga_suma():
    valor1=int(input("Ingrese el primer valor:"))
    valor2=int(input("Ingrese el segundo valor:"))
    suma=valor1+valor2
    print("La suma de los dos valores es:",suma)


# programa principal

mostrar_mensaje("Calcula la suma de dos valores ingresados por teclado")
carga_suma()
mostrar_mensaje("Gracias, vuelva pronto")
