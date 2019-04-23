# -*- coding: utf-8 -*-
#Ejercicio 7 
#Propósito: Realizar un programa que un menú que indique al usuario las diferentes opciones los parámetros del 
#elipsoide correspondiente. 
#Autor: Alicia Pizarro
#Fecha: 15/11/2017

#IMPORTACIÓN DE MÓDULOS
import math

##DEFINICIÓN DE DICCIONARIOS 
def calculo_elipsoide (elipsoide,**datum):
    
    diccionario_result = datum
        
    if elipsoide == 1:
        diccionario_result['Semieje_menor'] = diccionario_result['Semieje_mayor']*(1-diccionario_result['Aplanamiento'])
        diccionario_result['Excentricidad_lineal'] = math.sqrt(diccionario_result['Semieje_mayor']**2 - diccionario_result['Semieje_menor']**2)
        diccionario_result['Excentricidad_primera'] = diccionario_result['Excentricidad_lineal']/diccionario_result['Semieje_mayor'] 
        diccionario_result['Excentricidad_segunda'] = diccionario_result['Excentricidad_lineal']/diccionario_result['Semieje_menor'] 
       
    elif elipsoide == 2:
        diccionario_result['Excentricidad_lineal'] =  diccionario_result['Excentricidad_primera'] *  diccionario_result['Semieje_mayor'] 
        diccionario_result['Semieje_menor'] = math.sqrt( diccionario_result['Semieje_mayor']**2 -  diccionario_result['Excentricidad_lineal']**2)
        diccionario_result['Excentricidad_segunda'] =  diccionario_result['Excentricidad_lineal'] /  diccionario_result['Semieje_menor']
        diccionario_result['Aplanamiento'] = ( diccionario_result['Semieje_mayor'] -  diccionario_result['Semieje_menor'])/  diccionario_result['Semieje_mayor']
       
    elif elipsoide == 3:
        diccionario_result['Semieje_mayor'] =  diccionario_result['Semieje_menor']/ (1-  diccionario_result['Aplanamiento'])
        diccionario_result['Excentricidad_lineal'] = math.sqrt( diccionario_result['Semieje_mayor']**2 -  diccionario_result['Semieje_menor']**2)
        diccionario_result['Excentricidad_primera'] =  diccionario_result['Excentricidad_lineal']/ diccionario_result['Semieje_mayor'] 
        diccionario_result['Excentricidad_segunda'] =  diccionario_result['Excentricidad_lineal']/ diccionario_result['Semieje_menor']
        
    elif elipsoide == 4:
        diccionario_result['Semieje_mayor'] =  diccionario_result['Excentricidad_lineal'] /  diccionario_result['Excentricidad_primera']
        diccionario_result['Semieje_menor'] = math.sqrt(diccionario_result['Semieje_mayor']**2 -  diccionario_result['Excentricidad_lineal']**2)
        diccionario_result['Excentricidad_segunda'] =  diccionario_result['Excentricidad_lineal']/ diccionario_result['Semieje_menor']
        diccionario_result['Aplanamiento'] = ( diccionario_result['Semieje_mayor'] -  diccionario_result['Semieje_menor'])/  diccionario_result['Semieje_mayor']
       
    elif elipsoide == 5:
        diccionario_result['Excentricidad_lineal'] = math.sqrt( diccionario_result['Semieje_mayor']**2- diccionario_result['Semieje_menor']**2)
        diccionario_result['Excentricidad_primera'] =  diccionario_result['Excentricidad_lineal']/ diccionario_result['Semieje_mayor']
        diccionario_result['Excentricidad_segunda'] =  diccionario_result['Excentricidad_lineal']/ diccionario_result['Semieje_menor']
        diccionario_result['Aplanamiento'] = ( diccionario_result['Semieje_mayor'] -  diccionario_result['Semieje_menor'])/  diccionario_result['Semieje_mayor']
       
    for clave in datum:
        print clave, 'tiene un valor de ', datum[clave]
    
##DEFINICIÓN DE PREGUNTAS Y ASIGNACIÓN DE RESPUESTAS 
print("¿Qué elipsoide desea?")
print("1.Hayford")
print("2.NAD83")
print("3.WGS84")
print("4.ITRS")
print("5.Krassowsky")

    
elipsoide = 0
elipsoide = int(input("Introduce el elipsoide (1/2/3/4/5): "))

while elipsoide > 0 and elipsoide <= 5:
    
    if elipsoide == 1:
        diccionario_result = calculo_elipsoide(elipsoide, Semieje_mayor = 6378388, Aplanamiento = 0.003367003367003367003367003367)
    elif elipsoide == 2:
        diccionario_result = calculo_elipsoide(elipsoide, Semieje_mayor = 6378137, Excentricidad_primera = 0.08181919104) 
    elif elipsoide == 3:
        diccionario_result = calculo_elipsoide(elipsoide, Semieje_menor = 6356752.314, Aplanamiento = 0.003367003367003367003367003367)
    elif elipsoide == 4:
        diccionario_result = calculo_elipsoide(elipsoide, Excentricidad_lineal = 521854.642, Excentricidad_primera = 0.08181647051)
    elif elipsoide == 5:
        diccionario_result = calculo_elipsoide(elipsoide, Semieje_mayor = 6378245, Semieje_menor = 6356863.019)

    elipsoide = int(input("Introduce el elipsoide (1/2/3/4/5): "))

############################################################ FINISH RUN #####################################################################
############################################################################################################################################
