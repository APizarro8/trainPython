# -*- coding: utf-8 -*-
#Ejercicio 2 
#Porp�sito: Probar el gráfico Tortuga. 
#Autor: Alicia Pizarro
#Fecha: 13/10/2017

from turtle import Screen, Turtle

pantalla = Screen() #Creaci�n de la pantalla y asignaci�n de la variable
pantalla.setup (425, 225) #M�todo setup que invoca el ancho y alto de la variable
pantalla.screensize (400, 200) # M�todo que fija el tama�o de de la superficie de dibujo

tortuga = Turtle () #Creaci�n de la tortuga y asignaci�n de la variable 
tortuga.forward (100) # M�todo que le indica a la tortuga que avance 100 pasos hacia la derecha
tortuga.left (90) #M�todo que le indica a la tortuga que avance 90 pasos a la izquierda
tortuga.forward (100)
tortuga.left(90)
tortuga.forward(100)
tortuga.pencolor("red")
tortuga.circle (10)
tortuga.left(90)
tortuga.forward(100)
tortuga.circle (20)

tortuga.st()

pantalla.exitonclick() # M�todo para que la ventana creada no desaparezca
