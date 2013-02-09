#!/usr/bin/env python

##importamos las librerias necesarias
import pygame                ##interfaz
from pygame.locals import *  ##Para los botones y presion del raton
import Image                 ##para cargar imagenes, matriz de los pixeles
from math import *           ##operaciones
import sys                   ##cosas de sistema como para terminar el programa
#from pygame import *
import numpy                 ##arreglos
#from numpy  import *

Inombre = raw_input("Dame el nombre de la imagen con extencio: ")
nimagen = 'nimagen.png'
nfiltro = 'filtro.png'
difusion = 'difusion.png'
convolun = 'convolu.png'


min = 110.0 ##parametro definido
max = 190.0 ##parametro definido
im = Image.open(Inombre)   ##  cargar la imagen original
ancho, altura = im.size    ##  Sacar ancho y altura de la imagenpara ajustar la ventana
boton = pygame.Surface((100,25)) ##para crear el rectangulo del boton
boton.fill((100,100,255))        ##para el color del boton
#matriz = array([1,2,1],[1,5,1],[1,2,1])
pixels = im.load()
matrix = ([-1,0,1],[-2,0,2],[-1,0,1])
matriy = ([1,2,1],[0,0,0],[-1,-2,-1])
i = 11
j = 11

q = i -1 
w = j -1
print pixels[i -w,j -q][0]*matrix[0][0]


###funcion de filtro
def filtro(nfiltro):
	im = Image.open(Inombre) ##igual cargamos imagenes
        ancho, altura = im.size  ##altura y ancho para los fors
        pixels = im.load()       ##cargamos matriz de pixeles
	prom = 0                 ##declaraicon de variable para promedio
	altura = altura - 1      ##esto es para los for ya que inicia en cero
	ancho = ancho - 1        ##esto es para los for ya que inicia en cero
	for j in range(altura):
		for i in range(ancho):
	
			##se dividio las diferentes condiciones para sus respectivos vecinos
			##que se podria obtener
			#esquina superior izquierda#
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
	im.save(difusion)
	##enviamos la imagen ya cargada
	return pygame.image.load(difusion)



def convolucion(imagen):

	
	im = Image.open(imagen)
	ancho, altura = im.size
	pixels = im.load()
	altura = altura - 1
	ancho = ancho - 1
	for i in range(ancho):
		for j in range(altura):
			suma = 0
			for x in range(2):
				for y in range(2):
					q = x - 1
					w = y - 1
					try:
						#q = i+x-1
						#w = j+y-1
						sumax = (sum(pixels[i -q,j -w])/3)*matrix[x][y]
		                                sumay = (sum(pixels[i -q,j -w])/3)*matriy[x][y]

						#print sumax
						#sumay = pixels[i,j][0]*matrix[x][y]
						suma = sumax + suma + sumay
                                        	#a = int(sum(pixels[(i+x-1),(j+y-1)])/3)
						#b = int(matrix[x][y])
						#c = a*b
						
								
					except:
						suma = suma + 0
						#sumax = sumax + 0
						#sumay = sumay + 0	
			if suma > 255:
				suma = 255
			if suma < 0:
				suma = 0
			#else:
			#	suma = sumax + sumay
			pixels[i,j] = (suma,suma,suma)
	im.save(convolun)
	return pygame.image.load(convolun)



##funcion para la escala de grises
def escala(Inombre):
	im = Image.open(Inombre) ##igual que el de arriba cargamos la imagen
        ancho, altura = im.size  ##anco y altura
        pixels = im.load()       ##cargamos matriz de pixeles
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
        im.save(nfiltro) ##guardamos la imagen nueva
	return pygame.image.load(nfiltro) ##enviamos la imagen cargada

##funcion para el umbral
def mumbra(Inombre):
	im = Image.open(Inombre)  ##Aqui lo mismo que las dos funciones anteriores
        ancho, altura = im.size
        pixels = im.load()
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
	im.save(nimagen)                     ##guardamos 
	return pygame.image.load(nimagen)    ##regresemos la imagen cargada

##funcio para la diferenciacion entre la original y la imagen filtrada
def diferencia(imagen1,imagen2):
	im = Image.open(imagen1) ##cargamos todo el rollo para las dos imagenes
	im1 = Image.open(imagen2) ##la original y la imagen filtrada
	ancho,altura = im.size
	pixels = im.load()
	pixels1 = im1.load()
	for i in range (ancho):
		for j in range (altura):
			(a,b,c) = pixels[i,j] ##guardamos pixeles de ambas 
			(a1,b1,c1) = pixels1[i,j] ##imagenes
			prom = a+b+c/3            ##sacamos propedio de ambas
			prom1 = a1+b1+c1/3
			prom2 = prom - prom1      ##restamos
			if prom2 > 200:            ##aqui asemos binarisasion
				prom2 = 255
			else:
				prom2 = 0
			a = prom2                 ##reasignamos la diferencia
			b = prom2
			c = prom2
			pixels[i,j] = (a,b,c)    ##cambiamos pixeles
	im.save(nimagen)                         ##guardamos imagenes
	return pygame.image.load(nimagen)	##enviamos imagenes cargadas


##funcion principla del programa
def main(nombreI):
	pygame.init() ##inicialisamos python
	pantalla = pygame.display.set_mode((ancho + 150,altura)) ##inicialisamos pantalla
	pygame.display.set_caption("Rutinas para imagenes") ##ponemos nombre
	imagen = pygame.image.load(nombreI) ##cargamos imagen principal a mostrar
	fuente = pygame.font.Font(None, 20) ##para la fuente de las letras
	grisle = 'Escala de grices'         ##variable para guardar las letras a mostrar y cambiar posteriormente
	umbral = fuente.render('Umbral',1,(255,255,255)) ##para poner la fuente a variable o predefinido 
        normal = fuente.render('Normal',1,(255,255,255)) ##igual que la de arriba
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
						imagen = filtro(nfiltro) ##lo mismo que arriba pero para filtro
						grisle = 'convolucion'
					if cont == 2:
						imagen = convolucion(difusion) ##lo mismo de arriba para difucion
						grisle = 'normal'
					cont = cont + 1	
					if cont == 3:
						cont = 0
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
                pantalla.blit(umbral,(0,30)) ##coloar letra umbral
                pantalla.blit(boton,(0,60)) ##colocar boton 3
                pantalla.blit(normal,(0,60)) ##colocar letra normal
		pantalla.blit(esgris,(0,0)) ##colocar letra gris
		pantalla.blit(imagen, (100,0)) ##ppner la imagen actual
		pygame.display.update()  ##refrescamos la pantalla con los nuevos elemntos


		 
main(Inombre) ##llamamos la funcion principa lol

