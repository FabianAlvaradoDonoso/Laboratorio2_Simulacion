# -*- coding: utf-8 -*-
from random import random
from math import cos,pi

def corta(l=1,d=1): #comprueba si corta o no la linea
    #válido únicamente si l <= d
    x = d*random()
    #Un poco anticlimático tener que usar pi
    y = l*cos(pi/2*random())
    if y>x:
        return True
    else:
        return False

intentos = 1000000
N = 0 #Número de Tiros
C = 0 #Número de tiros que Cortan
L=0.25 #Longitud de la aguja
D=0.75 #Distancia entre líneas de corte, D<1

while N < intentos:

    N+=1
    if corta(L,D): #Si corta se suma otro acierto
        C+=1


print ("Pi = ",(2.0*L*N)/(D*C))
input("Pulse ENTER para continuar") 
