#!/usr/bin/env python

##importamos las librerias necesarias
import pygame                ##interfaz
from pygame.locals import *  ##Para los botones y presion del raton
import Image                 ##para cargar imagenes, matriz de los pixeles
from math import *           ##operaciones
import sys                   ##cosas de sistema como para terminar el programa
import numpy                 ##arreglos
import time
import math

Inombre = raw_input("Dame el nombre de la imagen con extencio: ")
nnormal = 'nimagen.png'
ngrises = 'filtro.png'
nfiltro = 'difusion.png'
nconvolucion = 'convolu.png'
numbra = 'umbral.png'
nnorma = 'normalizacion.jpg'
min = 110.0 ##parametro definido
max = 190.0 ##parametro definido
boton = pygame.Surface((100,25)) ##para crear el rectangulo del boton
boton.fill((100,100,255))        ##para el color del boton
matrii = ([0,0,0],[-1,0,0],[0,0,0])

def cargar(imagen):
	im = Image.open(imagen)
	ancho, altura = im.size
	pixels = im.load()
	return ancho,altura,pixels,im



###funcion de filtro
def filtro(imagen):
	ancho,altura,pixels,im = cargar(imagen)
	ancho = ancho -1
	altura = altura -1
	for j in range(altura):
		for i in range(ancho):
			if i == 0 and j == 0:
				prom = (sum(pixels[i + 1,j])/3 + sum(pixels[i,j + 1])/3 + sum(pixels[i,j])/3)/3
				
			#esquina superior derecha#
			if i == ancho and j == 0:
		        	prom = (sum(pixels[i,j+1])/3 + sum(pixels[i-1,j])/3 + sum(pixels[i,j])/3)/3
				
			#esquina inferior izquierda
			if i == 0 and j == altura:
                               	prom = (sum(pixels[i,j-1])/3 + sum(pixels[i+1,j])/3 + sum(pixels[i,j])/3)/3
			#esquina inferior derecha
			if i == altura and j == ancho:
                                prom = (sum(pixels[i - 1,j])/3 + sum(pixels[i,j - 1])/3 + sum(pixels[i,j])/3)/3


			##barra superior
			if i > 0 and i < ancho and j == 0:
				prom = (sum(pixels[i+1,j])/3 + sum(pixels[i-1,j])/3 +sum(pixels[i,j+1])/3+ sum(pixels[i,j])/3)/4
				
			##barra inferior
			if i > 0 and i < ancho and j == altura:
				prom = (sum(pixels[i -1,j])/3 + sum(pixels[i,j-1])/3 +sum(pixels[i+1,j])/3+ sum(pixels[i,j])/3)/4
	
			##barra lateral izquierda
			if j >0  and j <altura  and i == 0:
                        	prom = (sum(pixels[i+1,j])/3 + sum(pixels[i,j-1])/3 +sum(pixels[i,j +1])/3+ sum(pixels[i,j])/3)/4
				 
			##barra lateral derecha
			if i == ancho and j >0 and j < altura:
	                	prom = (sum(pixels[i - 1,j])/3 + sum(pixels[i,j-1])/3 + sum(pixels[i,j +1])/3+ sum(pixels[i,j])/3)/4
			##cuando tiene los cuatro vecinos
			if i > 0 and i< ancho and j>0 and j< altura:
				prom = (sum(pixels[i,j])/3 + sum(pixels[i + 1,j])/3 + sum(pixels[i - 1,j])/3 + sum(pixels[i,j + 1])/3 + sum(pixels[i,j -1])/3)/5		

			##igualamos a los pixeles
			a = prom
			b = prom
			c = prom
			##guardamos para la nueva imagen
			pixels[i,j] = (a,b,c)
	##guardamos la nueva imagen
	im.save(nfiltro)
	##enviamos la imagen ya cargada
	return pygame.image.load(nfiltro)


def convolucion(imagen):
	tiempoi = time.time()
	print "Iniciando convolucion: "
	ancho,altura,pixels,im = cargar(imagen)
        prom = 0                 ##declaraicon de variable para promedio
	suma = 0
	matrix = ([-1,0,1],[-2,0,2],[-1,0,1])
	matriy = ([1,2,1],[0,0,0],[-1,-2,-1])
	sumax = 0
	sumay = 0
        for j in range(altura):
                for i in range(ancho):
			sumax = 0
			sumay = 0
			for x in range(len(matrix[0])):
				for y in range(len(matrix[0])):
					try:
						#multix = matrix[x][y]*pixels[i+y -1,j+x -1][1]
						#multiy = matriy[x][y]*pixels[i+y -1,j+x -1][1]
						multix = matrix[x][y]*pixels[i+y,j+x][1]
                                                multiy = matriy[x][y]*pixels[i+y,j+x][1]

					except:
						multix = 0
						multiy = 0
					sumax = multix + sumax
					sumay = multiy + sumay
			xm = pow(sumax,2)
                        ym = pow(sumay,2)
                        g = int(math.sqrt(xm+ym))
			suma = g
			#suma = sumax + sumay
			#print suma
			if suma > 255:
				suma = 255
			if suma < 0:
				suma = 0
			pixels[i,j] = (suma,suma,suma)
	im.save(nconvolucion)
	tiempof = time.time()
        print "Se tardo: ",tiempof-tiempoi,"segundos"
	return pygame.image.load(nconvolucion)


##funcion para la escala de grises
def escala(imagen):
	ancho,altura,pixels,im = cargar(imagen)
	for i in range(ancho):
        	for j in range(altura):
			##sacamos promedio de (r,g,b) de los pixeles
			(a,b,c) = pixels[i,j]	
			suma = a+b+c 
			prom = suma/3
			a = prom ##igualamos
			b = prom ##igualamos
			c = prom ##igualamos 	 		
			pixels[i,j] = (a,b,c) ##igualamos
        im.save(ngrises) ##guardamos la imagen nueva
	return pygame.image.load(ngrises) ##enviamos la imagen cargada

##funcion para el umbral
def mumbra(imagen):
	ancho,altura,pixels,im = cargar(imagen)
	for i in range(ancho):
		for j in range(altura):
			(a,b,c) = pixels[i,j] ##obtenemos valore
			prom = a+b+c/3        ##promedio
			if min >= prom:       #condiciones para poner blanco o negro
				prom = 0
			if max <= prom:
				prom = 255
			a = prom              ##asignamos el promedio a los pixeles
			b = prom
			c = prom
			pixels[i,j]=(a,b,c)  ##asiganmos
	im.save(numbra)                     ##guardamos 
	return pygame.image.load(numbra)    ##regresemos la imagen cargada

##funcio para la diferenciacion entre la original y la imagen filtrada

def normalisacion(imagen):
	tiempoi = time.time()
	a = 0
	b = 255
	c = 5
	d = 95
	res = 0
	ancho,altura,pixels,im = cargar(imagen)
	for j in range(altura):
		for i in range(ancho):
			res = (pixels[i,j][1] - c)*((b-a)/(c - d)) + 255
			
			if res > 100:
				res = 255
			else:
				res = 0
			#if res > 255:
			#	res = 255
			#if res < 0:
			#	res = 0
			#pixels[i,j]=(res,res,res)	
	im.save(nnorma) ##guardamos imagenes
        tiempof = time.time()
	print "tiempo de normalizacion: ",tiempof - tiempoi
        return pygame.image.load(nnorma)		



def diferencia(imagen1,imagen2,min,max):
	ancho,altura,pixels,im = cargar(imagen1)
        ancho,altura,pixels,im = cargar(imagen2)
	for i in range (ancho -2):
		for j in range (altura -2):
			(a,b,c) = pixels[i,j] ##guardamos pixeles de ambas 
			(a1,b1,c1) = pixels1[i,j] ##imagenes
			prom = a+b+c/3            ##sacamos propedio de ambas
			prom1 = a1+b1+c1/3
			prom2 = prom - prom1      ##restamos
			v = prom2*255/500
			print v
			if v > 25:            ##aqui asemos binarisasion
				prom2 = 255
			else:
				prom2 = 0
			a = prom2                 ##reasignamos la diferencia
			b = prom2
			c = prom2
			pixels[i,j] = (a,b,c)    ##cambiamos pixeles
	im.save(nimagen)                         ##guardamos imagenes
	return pygame.image.load(nimagen)	##enviamos imagenes cargadas

#def normalizacion():


##funcion principla del programa
def main(nombreI):
	pygame.init() ##inicialisamos python
	ancho,altura,pixels,im = cargar(nombreI)
	pantalla = pygame.display.set_mode((ancho + 150,altura)) ##inicialisamos pantalla
	pygame.display.set_caption("Rutinas para imagenes") ##ponemos nombre
	imagen = pygame.image.load(nombreI) ##cargamos imagen principal a mostrar
	fuente = pygame.font.Font(None, 20) ##para la fuente de las letras
	grisle = 'Escala de grices'         ##variable para guardar las letras a mostrar y cambiar posteriormente
	umbral = fuente.render('Umbral',1,(255,255,255)) ##para poner la fuente a variable o predefinido 
        normal = fuente.render('Normal',1,(255,255,255)) ##igual que la de arriba
	normali = fuente.render('Normalizacion',1,(255,255,255))
	cont = 0 ##para diferentes acciones de los botones psoteriores
	##ciclo principal
	while True:
               	esgris = fuente.render(grisle,1,(255,255,255)) ##poner fuente a la letras grisle anteriormente declarada arriba
		for event in pygame.event.get(): ##verificar si existe algun evento
			if event.type == MOUSEBUTTONDOWN: ##chekar si se presiono el boton del raton
				cordx, cordy  = pygame.mouse.get_pos() ##tomar cordenadas del puntero del raton despues de ser presionado
				##primer evento para el primer boton			
				if 0 < cordx < 100 and 0 < cordy < 30:
					##se usa condiciones para cambiar la letra
					## adenmas de hacer escala de grises y posteriormente el mismo boton aplica filtro
					##la tercera condicion es para aplicar la diferencia para que sala borrosa la imagen
					if cont == 0:
						imagen = escala(nombreI) ##hace llamar a la funcion de escala y garda el resultado
						grisle = 'Filtro'
					if cont == 1:
						imagen = filtro(ngrises) ##lo mismo que arriba pero para filtro
						grisle = 'convolucion'
					if cont == 2:
						imagen = convolucion(nfiltro) ##lo mismo de arriba para difucion
						grisle = 'normalizacion'
					if cont == 3:
                                                imagen = normalisacion(nconvolucion) ##lo mismo de arriba para$
                                                grisle = 'normal'
                                       # cont = cont + 1	
					if cont == 4:
						imagen = pygame.image.load(nombreI)
						cont = 0
					cont = cont + 1
				##accion para el boton de umbral

				if 0 < cordx < 100 and 30 < cordy < 60:
					imagen = mumbra(nombreI) ##llama al metodo umbral
				if 0 < cordx < 100 and 60 < cordy < 90:
					imagen = pygame.image.load(nombreI) ##carga la imagen normal u original
					grisle = 'Escala de grices'
					cont = 0
			## esto es para quitar la ventan y salir del programa
            		if event.type == pygame.QUIT:
                		sys.exit()

		pantalla.fill((0,0,0))  ##borrar todo lo grafico
		pantalla.blit(boton,(0,0)) ##colocar boton 1
                pantalla.blit(boton,(0,30)) ##colocar boton 2
		pantalla.blit(boton,(0,90)) ##boton 4
                pantalla.blit(umbral,(0,30)) ##coloar letra umbral
                pantalla.blit(boton,(0,60)) ##colocar boton 3
                pantalla.blit(normal,(0,60)) ##colocar letra normal
		pantalla.blit(esgris,(0,0)) ##colocar letra gris
		pantalla.blit(normali,(0,90))
		pantalla.blit(imagen, (100,0)) ##ppner la imagen actual
		pygame.display.update()  ##refrescamos la pantalla con los nuevos elemntos


		 
main(Inombre) ##llamamos la funcion principa lol

