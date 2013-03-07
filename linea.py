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
from math import *
Inombre = raw_input("Dame el nombre de la imagen con extencio: ")
nnormal = 'nimagen.png'
ngrises = 'filtro.png'
nfiltro = 'difusion.png'
nconvolucion = 'convolu.png'
numbra = 'umbral.png'
nnorma = 'normalizacion.png'

convx = "convox.png"
convy = "convoy.png"

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

def sii(visitados,ancho,altura):
	for i in range(ancho):
        	for j in range(altura):
                	if visitados[j][i] == 0:
                                return j,i
	return 0,0
def bordes(imagen):
	colores = ([130,130,130],[0,255,0],[0,0,255],[255,255,0],[0,255,255],[255,0,255],[250,0,0]) ##colores
	cola = []
	ancho,altura,pixels,im = cargar(imagen)
	visitados = []
	contcolor = 0
	for y in range(altura):
		visitados.append([])
		for x in range(ancho):
			if pixels[x,y][1] == 0:
				visitados[y].append(1)
				#if len(cola) == 0:
				#	cola.append((y,x))
			else:
				if len(cola) == 0:
                                        cola.append((y,x))
				visitados[y].append(0)			
	while len(cola) > 0:
		tam = len(cola)         ##extraemos datos de la colas
                a = int(cola[tam-1][0]) ##obtenemos direccion a y
		b = int(cola[tam-1][1]) ##b = x
                visitados[a][b] = 1 ##marcamos como visitados
                cola.pop(tam-1) ##borramos de la cola
                try:
                        if pixels[b,a+1][0] == pixels[b,a][0] and visitados[a][b+1] == 0:
				#print "llego a pasar por aqui chngado"
                                cola.append((a,b+1))
                except:
			pass
		try:
                        if pixels[b,a-1][0] == pixels[b,a][0] and visitados[a][b-1] == 0:
				#print "llego a pasar por aqui chngado"
                                cola.append((a,b-1))
		except:
                        pass
                try:
                        if pixels[b+1,a][0] == pixels[b,a][0] and visitados[a+1][b] == 0:
				                        #print "llego a pasar por aqui chngado"
                                cola.append((a+1,b))

                except:
                        pass
                try:
                        if pixels[b-1,a][0] == pixels[b,a][0] and visitados[a-1][b] == 0:
                               # print "llego a pasar por aqui chngado"         
				cola.append((a-1,b))
                except:
			pass
		r =colores[contcolor][0]
		g =colores[contcolor][1]
		h =colores[contcolor][2]
		pixels[b,a] = (r,g,h)
		#if puntos > 0:
		#	plista.append((a,b))
		if len(cola) == 0:
			#print "se termino la figura :P lol"
			#print contcolor
			j,i = sii(visitados,ancho,altura)
                        if i==0 and j ==0:
                                break
                        else:
                                cola.append((j,i))
                                contcolor = contcolor + 1
                                if contcolor == 7:
                                        contcolor = 1
	
	im.save(pin)
	print "finaliso"
	return pygame.image.load(pin)

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


###funcion de la doctora
def gvotos(frecs, ancho,altura):
	frec = list()
	for valor in histo:
		if valor is None:
			continue
		frecuencia = frecs[valor]
		acepta = False
		if len(frec) <= cantidad:
			acepta = True
		if not acepta:
			for (v, f) in frec:
				if frecuencia > f:
					acepta = True
					break
		if acepta:
			frec.append((valor, frecuencia))
			frec = sorted(frec, key = lambda tupla: tupla[1])
			if len(frec) > cantidad:
				frec.pop(0)
	incluidos = list()
	for (valor, frecuencia) in frec:
		incluidos.append(valor)
	return incluidos
##funcion de la doctora


def pints(mayor,rmin):
	##ancho 1
	##verticaul 0
	cola = []
        ancho,altura,pixels,im = cargar(nconvolucion)
	cont = 0
	aceptado = 0
	mod = []
        for k in range(len(mayor)):
		x = mayor[k][1]
		y = mayor[k][0]
		aceptado = 0
		for c in range(-rmin,rmin):
			if not y == rmin:
				if x+c >0 and x+c < ancho-1 and y+c >0 and y+c< altura-1:
					if pixels[x+c,y][1] == 255 or pixels[x,y+c][1]==255:
						cont = cont + 1
					if cont > 5:
						aceptado = 1
						print "valor de x aceptado: ",x
						print "valor de y acpetado: ",y
						mod.append((y,x))
	return aceptado,mod
		
	

def sinradio(rmin,rmax,gx,gy,mxy):
	print "Buscando radios"
	r = []
	maxa = 0
	rmaxa = 0
	ancho,altura,pixels,im = cargar(nconvolucion)
	ancho1,altura1,pixels1,im1 = cargar(ngrises)
	while rmin <= rmax:
		frecuencias,cord,mayor = circulos(gx,gy,rmin)
		if mayor > maxa:
			maxa = mayor
			print "mayor",rmin
			if len(cord) > 0:
				print "pasado"
			#maxa = mayor
			#rmaxa = rmin
			##print maxa
			#print "rado: ",rmin
				aceptado,mod = pints(cord,rmin)
				if aceptado == 1:
					#print "radio aceptado: ",rmin
					for xx in range(len(mod)-1):
						 for angulo in range(360):
							 x = mod[xx][1] + rmin*cos(angulo)
							 y = mod[xx][0] + rmin*sin(angulo)
							 if x > 0 and y > 0 and  y < altura -1 and  x < ancho -1:
								 pixels1[x,y] = (0,0,255)    
		rmin = rmin + 1
	im1.save(ngrises)	
	print "Termine"	
        return pygame.image.load(ngrises)
	#print "valor de puntos:",maxa
	#print "valor del radio:",rmaxa

def gvotos(votos,ancho,altura):
	dim = int(ancho*altura)
	for rango in range (1,2):
		agregado = True
		while agregado:
			agregado = False
			for y in range(altura):
				for x in range(ancho):
					v = votos[y][x]
					if v > 0:
						for dy in xrange(-rango, rango):
							for dx in xrange(-rango, rango):
								if not (dx == 0 and dy == 0):
									if y + dy > 0 and y + dy < altura and x + dx > 0 and x + dx < ancho:
										w = votos[y + dy][x + dx]
										if w > 0:
											if v - rango >= w:
												votos[y][x] = v + w 
												votos[y + dy][x + dx] = 0
												agregado = True
		#if rango >= 200:										
		#	print rango										
	return votos

def circulos(gx,gy,radio):
	tiempo = time.time()
	CERO = 0.0001 ##para comparaciones de los angulos
        magnitud = [] ##guardamos el gradiente              
        angulos = [] ##guaramos angulos              
        rhos = [] ##guardamos rho                           
        ancho,altura,pixels,im = cargar(ngrises)                             
        #ancho2,altura2,pixels2,im2 = cargar(               
        angulo = 0.0 ##iniciamos rho como cero inicia  
        #normalisacion()
        ancho2,altura2,pixels2,im2 = cargar(nconvolucion) ##ca
	#print "inicio de rho: "
	cose = 0
	sen = 0
	votos = list()
	#print "poniendoles todos cero"
	for x in range(altura):
		votos.append([])
		for y in range(ancho):
			votos[x].append(int(0))			
	#print "cchekando las frecuencias"		
        for y in range(altura):
                rhos.append([])                                  
                angulos.append([])##                                
                magnitud.append([])##agre
		votos.append([])
		#xm = altura/2 - x
                for x in range(ancho):
		#	ym = y - ancho/2
			if x > 0 and y > 0 and  y < altura -1 and  x < ancho -1:
				if pixels2[x,y][1] == 255:
					hor = gx[y][x] ##dat                       
					ver = gy[y][x] ##dato de             
					#mag = mxy[y][x] ##dato de gradiente combinacion
					g = math.sqrt(hor ** 2 + ver ** 2)
					if fabs(g) > 0.0:
						#print "paso aqui si acao"
						#angulo = atan(ver/hor)
						cose = hor / g
						sen = ver / g
						xc = int(round(x -radio*cose))
						yc = int(round(y -radio*sen))
					
						xcm = xc
						ycm = yc
						#xcm = xc + ancho/2
						#ycm = altura/2 - yc
						
					#print "si paso aqui"
						if xcm > 0 and xcm < ancho -1 and ycm > 0 and ycm < altura:
							votos[ycm][xcm] += 1
							pixels[xcm,ycm] = (0,255,0) 
	#print "chekando vecinos"						
	votos = gvotos(votos,ancho,altura)						
	maximo = 0
	suma = 0.0
	#print "sumando"
	for x in range(altura):
		for y in range(ancho):
			v = votos[x][y]
			suma += v
			if v > maximo:
				maximo = v
                 
	promedio = suma / (ancho * altura)
	umbral = (promedio+maximo)/2.0
	#umbral = maximo-promedio
	#print "detectando"
	puntosx = []
	puntosy = []
	mayor = 0
	cord = []
	mayorx = 0
	mayory = 0
	#print "lalalala"
	for x in range(altura):
		for y in range(ancho):
			v = votos[x][y]
			if v > umbral:
				#print "pase"
				#print "contador: "
				#cord.append((x,y))
				if v > mayor:
					mayory = y 
					mayorx = x
					mayor = v
					cord.append((mayorx,mayory))
					#mayor = v
					#print mayor
				#print "punto detectado en x:",x,"en y: ",y
				#puntosx.append(y)
				#puntosy.append(x)
				#pixels[y,x] = (255,0,0)
	#print mayor
	#cord.append((mayorx,mayory))		
	return	votos,cord,mayor		
	       		#print "valor de ancho",y,"valor de la altura",x
	#for cont in range(len(puntosx)):
	#	print cont
	#	for angulo in range(360):
	#		x = puntosx[cont] + radio*cos(angulo)
	#		y = puntosy[cont] + radio*sin(angulo)
	#		pixels[x,y] = (0,0,255)
	#im.save(ngrises)			
	#print "termono"			
	#return pygame.image.load(ngrises)

def lineas(mxy,gx,gy):
	tiempoi = time.time()
	CERO = 0.0001 ##para comparaciones de los angulos
	magnitud = [] ##guardamos el gradiente 
	angulos = [] ##guaramos angulos
	rhos = [] ##guardamos rho
	ancho,altura,pixels,im = cargar(ngrises) ##cargamos imagen a escalade grises
	#ancho2,altura2,pixels2,im2 = cargar(nconvolucion) ##cargamos la imagen de bordes
	angulo = 0.0 ##iniciamos rho como cero inicia

#	normalisacion()
	ancho2,altura2,pixels2,im2 = cargar(nconvolucion) ##cargamos la imagen de bordes 
	#gy = normalisacion(gy)
	print "inicio de rho: "
	for x in range(altura):
		rhos.append([])   ##agregamos fila
		angulos.append([])##agregamos fila
		magnitud.append([])##agregamos fila
		for y in range(ancho):
			if x > 0 and y > 0 and  x < altura -1 and y < ancho -1:
				hor = gx[x][y] ##dato de gradientes gx
				ver = gy[x][y] ##dato de gradiente gy
				mag = mxy[x][y] ##dato de gradiente combinacion
				if fabs(hor) > 0.0:
					angulo = atan(ver/hor)
				else:
					
					if fabs(hor) + fabs(ver) <= 0.0:#nada en ninguna direccion
						angulo = None
					#elif hor == 0 and ver == 255: ##para saber si es vertical
						#angulo = pi/2
						#print "angulo de la mitad: ",angulo
					elif fabs(ver - hor) < CERO: # casi iguales diagonales
						angulo = atan(1.0)
					elif hor * ver > 0.0: # mismo signo horizontal
						angulo = pi 
					else: # negativo -> -pi##horizontal
						angulo = 0.0	
				if angulo is not None:
					#cosa = '%0.2f'%angulo
					# asegurar que este entre cero y pi (0 y 180) y comparaciones mas adelante
 					while angulo < CERO:
						angulo += pi
					while angulo > pi:
						angulo -= pi
					cosa = float('%0.2f'%angulo)
					#if cosa == float('%0.2f'%pi/2):
					#	print "y"
					#if cosa == 0.79:
					#	print "x"
					
					rho = fabs( y * cos(angulo) + x * sin(angulo))
					magnitud[x].append(mag)                                    
					angulos[x].append(cosa)
					rhos[x].append(float('%0.2f'%rho))
					#print cosa
				

				if angulo == None:
					magnitud[x].append(mag)
                                        angulos[x].append(angulo)
                                        rhos[x].append(None)

                                                #angulos[x].append(int(180*(angulo/pi))/18)
                                        #       rhos[x].append(rho) 	
	##aqu  contamos las frecuencia de cada uno de las rho				
	grupos = dict() ##diccionario
	cont = 0 ##contador para ciertas cosas como contar los vecinos si tiene el mismo angulo
	#print len(magnitud)
	#print altura
	for x in range(altura):
		for y in range(ancho):
			if x > 0 and y > 0 and  x < altura -1 and y < ancho -1:
			#	print "rhos: ",len(rhos[x])
			#x	print "ancho: ",ancho
				      #  ancho2,altura2,pixels2,im2 = cargar(nconvolucion) ##cargamos la imagen de bordes 
				try:
					if rhos[x][y] != None:
						dato = ((rhos[x][y]),(angulos[x][y]))
					if dato in grupos:   ##decimas me falla esa part
						grupos[dato] += 1 ##aqui chekamos si el 
					else:                      ##se encuentra en el d
						grupos[dato] = 1  ##si no lo agrega y pone
				except:
					pass
	print "frecuencias"			
	frec = frecuentes(grupos, int(ceil(len(grupos) * 50))) # 
	print "termino"
	for x in range(altura):
		for y in range(ancho):
			#if pixels2[y,x][1] == 255:
			if x > 0 and x< altura-1 and y > 0 and y < ancho-1:
				#if pixels2[y,x][0] == 0:
				try:
					if pixels2[y,x][1] == 255:
					#if gx[x][y] == 255 or gy[x][y] == 255:
						rho, ang = rhos[x][y],angulos[x][y]
						if (rho, ang) in frec:
							#print "valor de theta: ",theta
							if ang == 0.79:
								pixels[y,x] = (0,0,255)
							if ang == 3.14 or ang == 0:
								pixels[y,x] = (255,255,0)
							if 1.50 < ang and ang < 1.60 :
								pixels[y,x] = (255,0,0)

				except:
					pass
	print "finalizo "
	im.save(ngrises) ##guardamos puntos 						 
	tiempof = time.time()
	print "Tiempo estimado: ",tiempof-tiempoi
	return pygame.image.load(ngrises)


def convolucion(imagen):
	tiempoi = time.time()
	print "Iniciando convolucion: "
	ancho,altura,pixels,im = cargar(ngrises)
        #prom = 0                 ##declaraicon de variable para promedio
	#suma = 0
	#matrix = [[-1,0,1],[-2,2,2],[-1,-1,-1]]
	#matriy = [[-1,2,-1],[-1,2,-1],[-1,2,-1]]
	matrix = ([-1,0,1],[-2,0,2],[-1,0,1])
        matriy = ([1,2,1],[0,0,0],[-1,-2,-1])
	#suma = 0
	#pix = im.load()

	###imagen con las dos combinaciones
	nuevai = Image.new("RGB", (ancho, altura))
	npixels = nuevai.load()
	##imagen con las dos combinaciones
	#lis = list()
	gx = [] ##gradientes de x
	gy = [] ##gradientes de y
	mxy = [] ##la convinacon de ambos
	for i in range(altura):
		#c = list()
		gx.append([])
		gy.append([])
		mxy.append([])
		for j in range(ancho):
			sumax = 0
			sumay = 0
			cont = 0
			sumx = 0
			sumy = 0
			if j > 0 and i > 0 and  i < altura -1 and j <ancho -1:             
				for x in range(len(matrix[0])):
					for y in range(len(matrix[0])):
						try:
							sumax = matrix[x][y] * pixels[j+y-1,i+x-1][1]
							sumay = matriy[x][y] * pixels[j+y-1,i+x-1][1]
						
						except:
							sumax = 0
							sumay = 0
							#pass
						sumx = sumx + sumax
						sumy = sumy + sumay
			r = int(math.sqrt(sumx**2+sumy**2)) ##calculamos gradiente mayor 
			#c.append(r)
			#r = sumay			
			gx[i].append(sumx) ##guardamos los gradientes en x
			gy[i].append(sumy) ##guardamos los gradientes en y 
			mxy[i].append(r)    ##guardamos el resultado de los gradientes en x e y
			if r < 0:
				r = 0
			if r > 255:
				r = 255	
			npixels[j, i] = (r,r,r)	
	nuevai.save(nconvolucion)
	tiempof = time.time()
	normalisacion()
        print "Se tardo: ",tiempof-tiempoi,"segundos"
	return pygame.image.load(nconvolucion),gx,gy,mxy


##funcion para la escala de grises
def escala(imagen):
	ancho,altura,pixels,im = cargar(imagen)
	for i in range(ancho):
        	for j in range(altura):
			##sacamos promedio de (r,g,b) de los pixeles
			(a,b,c) = pixels[i,j]	
			suma = a+b+c 
			prom = int(suma/3)
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

def normalisacion():
	tiempoi = time.time()
	a = 0
	b = 255
	c = 5
	d = 95
	res = 0
	ancho,altura,pixels,im = cargar(nconvolucion)
	for j in range(altura):
		for i in range(ancho):
			if j > 0 and i > 0 and  j < altura -1 and i <ancho -1:
				#res = (pixels[i,j][1] - c)*((b-a)/(c - d)) + 255
				res = (pixels[i,j][1] -c)*((b-a)/(c-d))+255
				if res >= 100:
					res = 0
				else:
					res = 255
			pixels[i,j] = (res,res,res)
			
	#if res > 255:
	#res = 255
	#if res < 0:
	#res = 0
			#pixels[i,j]=(res,res,res)
	im.save(nconvolucion) ##guardamos imagenes
        #tiempof = time.time()
	#print "tiempo de normalizacion: ",tiempof - tiempoi
        #return pygame.image.load(nconvolucion)		
	return 				


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
	#lista = []
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
						imagen,gx,gy,mxy = convolucion(nfiltro) ##lo mismo de arriba para difucion
						grisle = 'lineas'
					#if cont == 3:
					#	imagen = normalisacion(ngrises) 
					#	grisle = 'lineas'
					if cont == 3:
						imagen = sinradio(10,150,gx,gy,mxy)
                                                #imagen = lineas(mxy,gx,gy) ##lo mismo de arriba para$
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
