# -*- coding: utf-8 -*-
#Autor: Alicia Pizarro
#Fecha: 05 de diciembre de 2017
#Descripción: Almacenar  los nombres de todos sus archivos junto con su tamaño en un diccionario e imprimir el contenido. 

## IMPORTACIÓN DE LIBRERÍAS
import sys
import os

##########################################################################################################################
##sys.argv[1] Directorio elegido
path = 'C:\\Users\\Alicia\\Desktop\\MASTER_TIG\\Primer cuatrimestre\\Funtos_analisis\\Redes\\AV_Pizarro_Alicia_P3'

diccionario = {} # CREAR DICCIONARIO 
    
lstfiles = os.listdir(path) #Listar archivos en el direcctorio

for archivos in lstfiles:
    (nombre, extension) = os.path.splitext(archivos) #Devuelve  el nombre de los archivos
    archivo_path = os.path.join(path, archivos) #Construir ruta de acceso a dichos archivos
    archivo_tamano = os.path.getsize(archivo_path) #Devuelve el tamaño de los archivos 

    diccionario[nombre] = archivo_tamano #Añade al diccionario

for clave in diccionario:
        print 'El archivo {0} tiene un tamaño de {1} bytes'.format (clave, diccionario[clave])

######################################################### FINISH #########################################################
##########################################################################################################################
