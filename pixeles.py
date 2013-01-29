
from math import floor,sqrt

kilo = 1024
mega = kilo*1024
gia = mega*1024


def normal(x,y,z):
	res = x/(y*z)
	res = floor(sqrt(res))
	print res
	altura = y*res
	ancho = z*res
	return ancho,altura



print "Escoge resolucion"
print "1-. Kilopixeles"
print "2-. Megapixeles"
print "3-. Gigapixeles"
opcion = int(raw_input("Dime tu opcion: "))
numero = int(raw_input("Dime el numero: "))
print "Mensiona la resolucion"
altura = int(raw_input("Dime la dimencion de altura: "))
ancho = int(raw_input("Dime la dimencion de la ancho: "))

if opcion == 1:
	anch,altu = normal(numero*kilo,altura,ancho)
	print "Resolucio: "
	print "Ancho: ",anch
	print "Altura: ",altu
if opcion == 2:
	anch,altu = normal(numero*mega,altura,ancho)
	anch,altu = normal(numero*kilo,altura,ancho)
        print "Resolucio: "
        print "Ancho: ",anch
        print "Altura: ",altu
if opcion == 3:
	anch,altu = normal(numero*giga,altura,ancho)
	anch,altu = normal(numero*kilo,altura,ancho)
        print "Resolucio: "
        print "Ancho: ",anch
        print "Altura: ",altu

