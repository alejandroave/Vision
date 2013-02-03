#!/usr/bin/env python

import pygame
from pygame.locals import *
import Image
from math import *
import sys
from pygame import *

Inombre = raw_input("Dame el nombre de la imagen con extencio: ")
nimagen = 'nimagen.jpg'
nfiltro = 'filtro.jpg'
min = 110.0
max = 190.0
im = Image.open(Inombre)
ancho, altura = im.size
boton = pygame.Surface((100,25))
boton.fill((100,100,255))


def filtro(nfiltro):
	im = Image.open(Inombre)
        ancho, altura = im.size
        pixels = im.load()
	prom = 0
	altura = altura - 1
	ancho = ancho - 1

	for j in range(altura):
		for i in range(ancho):
			#esquina superior izquierda#
			if i == 0 and j == 0:
				prom = pixels[i + 1,j][0] + pixels[i,j + 1][0] + pixels[i,j][0]/3
			#esquina superior derecha#
			if i == ancho and j == 0:
				prom = pixels[i,j+1][0] + pixels[i-1,j][0] + pixels[i,j][0]/3
				
			#esquina inferior izquierda
			if i == altura and j == 0:
				prom = pixels[i+1,j][0] + pixels[i,j - 1][0] + pixels[i,j][0]/3
			#esquina inferior derecha
			if i == altura and j == ancho:
                                prom = pixels[i - 1,j][0] + pixels[i,j - 1][0] + pixels[i,j][0]/3


			##barra superior
			if i > 0 and i < ancho and j == 0:
		        	prom = pixels[i+1,j][0] + pixels[i-1,j][0] +pixels[i,j+1][0]+ pixels[i,j][0]/4
				
			##barra inferior
			if i > 0 and i < ancho and j == altura:
				prom = pixels[i -1,j][0] + pixels[i,j-1][0] +pixels[i+1,][0]+ pixels[i,j][0]/4
	
			##barra lateral izquierda
			if j >0  and j <altura  and i == 0:
                        	prom = pixels[i+1,j][0] + pixels[i,j-1][0] +pixels[i,j +1][0]+ pixels[i,j][0]/4

				 
			##barra lateral derecha
			if j == ancho and i >0 and i < altura:
	                	prom = pixels[i - 1,j][0] + pixels[i,j-1][0] +pixels[i,j +1][0]+ pixels[i,j][0]/4
			
			if i > 0 and i< ancho and j>0 and j< altura:
				prom = pixels[i,j][0] + pixels[i + 1,j][0] + pixels[i - 1,j][0] + pixels[i,j + 1][0] + pixels[i,j -1][0]/5		

			a = prom
			b = prom
			c = prom
			pixels[i,j] = (a,b,c)

	im.save(nfiltro)
	return pygame.image.load(nfiltro)





def escala(Inombre):
	im = Image.open(Inombre)
        ancho, altura = im.size
        pixels = im.load()
	for i in range(ancho):
        	for j in range(altura):
			(a,b,c) = pixels[i,j]	
			suma = a+b+c
			prom = suma/3
			a = prom
			b = prom
			c = prom							
			pixels[i,j] = (a,b,c)
        im.save(nfiltro)
	return pygame.image.load(nfiltro)

def mumbra(Inombre):
	im = Image.open(Inombre)
        ancho, altura = im.size
        pixels = im.load()
	for i in range(ancho):
		for j in range(altura):
			(a,b,c) = pixels[i,j]
			prom = a+b+c/3
			if min >= prom:
				prom = 0
			if max <= prom:
				prom = 255
			a = prom
			b = prom
			c = prom
			pixels[i,j]=(a,b,c)
	im.save(nimagen)
	return pygame.image.load(nimagen)

def main(nombreI):
	pygame.init()
	screen = pygame.display.set_mode((ancho +150 ,altura + 150))
	pygame.display.set_caption("Rutinas para imagenes")
	imagen = pygame.image.load(nombreI)
	fuente = pygame.font.Font(None, 20)
	grisle = 'Escala de grices'
	umbral = fuente.render('Umbral',1,(255,255,255))
        normal = fuente.render('Normal',1,(255,255,255))
	cont = 0
	while True:
               	esgris = fuente.render(grisle,1,(255,255,255))
		for event in pygame.event.get():
			if event.type == MOUSEBUTTONDOWN:
				cordx, cordy  = pygame.mouse.get_pos()
				if 0 < cordx < 100 and 0 < cordy < 30:
					if cont == 0:
						imagen = escala(nombreI)
						grisle = 'Filtro'
						cont = 1
					else:
						imagen = filtro(nfiltro)
						grisle = 'Escala de grises'
						cont = 0
				if 0 < cordx < 100 and 30 < cordy < 60:
					imagen = mumbra(nombreI)
				if 0 < cordx < 100 and 60 < cordy < 90:
					imagen = pygame.image.load(nombreI)
					grisle = 'Escala de grices'
					cont = 0
            		if event.type == pygame.QUIT:
                		sys.exit()

		screen.fill((0,0,0))
		screen.blit(boton,(0,0))
                screen.blit(boton,(0,30))
                screen.blit(umbral,(0,30))
                screen.blit(boton,(0,60))
                screen.blit(normal,(0,60))
		screen.blit(esgris,(0,0))
		screen.blit(imagen, (100,0))
		pygame.display.update()
		

		
main(Inombre)

