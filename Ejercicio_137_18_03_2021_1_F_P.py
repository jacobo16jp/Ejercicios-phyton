# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 01:40:55 2021

@author: Andres Giron
"""
def cargar():
    lista=[]
    for x in range(10):
        valor=int(input("Ingrese valor:"))
        lista.append(valor)
    return lista


def generar_listas(lista):
    listanega=[]
    listaposi=[]
    for x in range(len(lista)):
        if lista[x]<0:
            listanega.append(lista[x])
        else:
            if lista[x]>0:
                listaposi.append(lista[x])
    return [listanega,listaposi]                
           

def imprimir(lista):
    for x in range(len(lista)):
        print(lista[x])


# programa principal

lista=cargar()
listanega,listaposi=generar_listas(lista)
print("Lista con los valores negativos")
imprimir(listanega)
print("Lista con los valores positivos")
imprimir(listaposi)


