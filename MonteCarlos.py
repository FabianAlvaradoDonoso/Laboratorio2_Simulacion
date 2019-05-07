#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import math

def pi(n): #funcion que devuelve aproximacion del numero pi

    #Contador que cuenta cuantas veces el
    #punto seleccionado queda dentro del circulo
    aciertos = 0

    #Iteramos en el rango n (numero de iteraciones que se haran)
    for i in range(n):
        #generamos los números aleatorios
        x = random.random()
        y = random.random()

        #calcular distancia media
        deltaX = math.pow((x-0.5), 2)
        deltaY = math.pow((y-0.5), 2)

        #Distribucion
        distE = math.sqrt(deltaX+deltaY)

        #Comprobacion si el punto esta dentro del circulo
        if distE < 0.5:
            aciertos = aciertos + 1

    return (4 * float(aciertos) / n) #calculo del numero pi

#Mandamos a llamar la función pi()
for i in range(1,10):
    print (pi(100000*i)) #Numero aleatorio
input("Pulse ENTER para continuar")
