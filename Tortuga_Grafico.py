# -*- coding: utf-8 -*-
#Propósito: realizar un gráfico con tortugas
#Autor: Alicia Pizarro
#Fecha: 15/11/2017

import matplotlib.pyplot as plt
import numpy as np

lista1 = [11,2,3,15,8,13,21,34]
plt.plot(lista1)
plt.show()

lista1 = [11,2,3,15,8,13,21,34]   # Declara lista1 con 8 valores
plt.plot(lista1)   # Dibuja el gráfico
plt.title("Título")   # Establece el título del gráfico
plt.xlabel("abscisa")   # Establece el título del eje x
plt.ylabel("ordenada")   # Establece el título del eje y