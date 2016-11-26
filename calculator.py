#encoding: UTF-8
continuar = 1
while continuar == 1:
	print ("""
		*********************************
		*				*
		*	   Calculadora		*
		*				*
		*  _\|/_   By Alex  	_\|/_	*
		*				*
		*********************************
		
	Elegir Opcion (Numero):

		Calculadora:
				1 - Sumar.
				2 - Restar.
				3 - Multiplicar.
				4 - Dividir.
		Extra:
				5 - Calcula cuantos dias haz vivido
				6 - Teorema de Pitagoras
      	""")


	Opcion = int(input ("Elegir opcion: "))
	if Opcion == 1:
		print ("Usted a elegido Sumar.")
		N1 = int(input("Introduzca el primer numero: "))
		N2 = int(input("Introduzca el numero a sumar: "))
		print ("Esto da: ",N1+N2)
	elif Opcion == 2:
		print ("Usted a elegido Restar.")
		N1 = int(input("Introduzca el primer numero: "))
		N2 = int(input("Numero a restar: "))
		print ("Esto da: ",N1-N2)
	elif Opcion == 3:
		print ("""
	Usted a elegido Multiplicar.
	""")
		N1 = int(input("Introduzca Numero a Multiplicar: "))
		N2 = int(input("Por : "))
		print ("Esto da: ",N1*N2)
	elif Opcion == 4:
		print ("""
	Usted a elegido Dividir.
	""")
		N1 = int(input("Primer Numero: "))
		N2 = int(input("Dividido por: "))
		print ("Esto da: ",N1/N2)
	elif Opcion == 5:
		print ("""
	Colocar la fecha en 4 numeros ej: 1900
	""")
		N1 = int(input("Año nacimiento: "))
		N2 = int(input("Año actual: "))
		N3 = N2 - N1
		print ("Haz vivido aproximadamente" ,N3*365, "diaz")
	elif Opcion == 6:
		print ("""
		*****************************
		*			    *
		*    Teorema de pitagoras   *
		*			    *
		*****************************
	""")
		a = int(input("Lado a: "))
		b = int(input("Lado b: "))
		c = a*a
		d = b*b
		e = c+d
		import math
		f=math.sqrt(e)
		print ("X es igual a: ", f)
 
	else:
		print ("""
	Opcion incorrecta
	""")
		raw_input()

	seguir = "s"
	seguir1 = str(input("desea seguir?s/n"))
	if seguir == seguir1:
		pass
	elif seguir != seguir1:
		break

