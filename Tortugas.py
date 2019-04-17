# -*- coding: utf-8 -*-
#Ejercicio 2 
#Porpósito: Probar el gráfico Tortuga. 
#Autor: Alicia Pizarro
#Fecha: 13/10/2017

##Importación de módulos
from turtle import Screen, Turtle

#####################################################################################################
pantalla = Screen() #Creación de la pantalla y asignación de la variable.
pantalla.setup (425, 225) #Método setup que invoca el ancho y alto de la variable.
pantalla.screensize (400, 200) # Método que fija el tamño de de la superficie de dibujo.

tortuga = Turtle () #Creación de la tortuga y asignación de la variable. 
tortuga.forward (100) # Método que le indica a la tortuga que avance 100 pasos hacia la derecha.
tortuga.left (90) #Método que le indica a la tortuga que avance 90 pasos a la izquierda.
tortuga.forward (100)
tortuga.left(90)
tortuga.forward(100)
tortuga.pencolor("red")
tortuga.circle (10)
tortuga.left(90)
tortuga.forward(100)
tortuga.circle (20)

tortuga.st()

pantalla.exitonclick() # Método para que la ventana creada no desaparezca

#####################################################################################################
