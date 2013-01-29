#!/usr/bin/env python

import pygame
from pygame.locals import *
import sys
import Image


pantallalatura = 800
pantallaanchura = 600
a = 0
b = 0
c = 0
nimagen = 'nimagen.jpg'

def cambio(Inombre):
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
        im.save(nimagen)

def main(nombreI):
	pygame.init()
	screen = pygame.display.set_mode((pantallalatura,pantallaanchura))
	pygame.display.set_caption("Rutinas para imagenes")
	imagen = pygame.image.load(nombreI).convert_alpha()
	screen.blit(imagen, (200, 0))
	pygame.display.flip()
	while True:
	
		cambio(nombreI)
		imagen = pygame.image.load(nimagen).convert_alpha()
		screen.blit(imagen, (200,0))
                pygame.display.flip()
        
		for event in pygame.event.get():
            		if event.type == pygame.QUIT:
                		sys.exit()

		



Inombre = raw_input("Dame el nombre de la imagen con extencio: ")
cambio(Inombre)
main(Inombre)

