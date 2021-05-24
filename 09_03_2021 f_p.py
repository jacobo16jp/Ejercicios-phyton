#Leer N, generar aleatorios y calcular suma y promedio
#Librerias usadas en el programa 
import random

#Area de definicion de variables

cantidad_numeros=0
con_rep=0
acum_suma=0
promedio_num_ale=0.0
numero=0

#Variables segunda parte 
acum_positivos=0
acum_negativos=0
contador_posi=0
contador_nega=0
promedio_posi=0.0
promedio_nega=0

#Variables tercera parte del ejercicio
mayor_positivo=0
mayor_negativo=0
menor_positivo=0
menor_negativo=0

#Entradas
cantidad_numeros=int(input("Cantidad de numeros que requiere: "))

#Procesos
#Ciclo while

while con_rep<cantidad_numeros:
    numero=random.randint(-100,10000)
    acum_suma=acum_suma+numero 
    
    #Segunda parte del ejercicio 
    
    if numero>0: #Calculo para numeros positivos
        print("Numero positivo", numero)
        acum_positivos=acum_positivos+numero
        contador_posi=contador_posi+1
        #Tercera parte del ejercicio
        #Identificar el mayor de los positivos
        if numero>mayor_positivo:
            mayor_positivo=numero
        #Identificar el numero de los positivos
        if numero<menor_positivo:
            menor_positivo=numero
        #Fin tercera parte
        
    else: #Calculo para numeros negativos
        print("numero negativo", numero)
        acum_negativos=acum_negativos+1
        contador_nega=contador_nega+1
        
#Fin segunda parte ejercicio
        con_rep=con_rep+1
#Fin segunda parte ejercicio

#Calculo de los promedios
promedio_num_ale=acum_suma/con_rep
promedio_posi=acum_positivos/contador_posi
promedio_nega=acum_negativos/contador_nega

#Slidas todos los numeros
print("Suma de numeros aleatorios:",acum_suma)
print("El promedio de los numeros aleatorios es: ", promedio_num_ale)

#Salidas numeros positivos
print("Cantidad numeros positivos:", contador_posi)
print("Suma de numeros positivos:", acum_positivos)
print("El promedio de los numeros positivos: ", promedio_posi)

#Salida de todos lod numeros negativos
print("Cantidad numeros negativos:", contador_nega)
print("Suma de numeros negativos:", acum_negativos)
print("El promedio de los numeros negativos: ", promedio_nega)

#Imprimir mayor y menor de los positivos
print("Mayor de los positivos", mayor_positivo)
print("Menor de los positivos: ", menor_positivo)

        
