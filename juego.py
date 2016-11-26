import random
continuar = 1
while continuar == 1:
	print("Hola picha")
	print("Elige la dificultad del juego: 1-easy 2-hard 3-superhard")

	dificultad = int(input("Escribe la dificultad del juego"))

	
	if dificultad == 1:
			cant_digitos = 3
	elif dificultad == 2:
			cant_digitos = 4
	elif dificultad == 3:
			cant_digitos = 5
	elif dificultad == 4:
			cant_digitos = 2

	digitos = ("1","2","3","4","5","6","7","8","9")
	codigo = ""

	for i in range(cant_digitos):
		elegido = random.choice(digitos)
		while elegido in codigo:
			elegido = random.choice(digitos)
		codigo = codigo + elegido

	print("Tienes que adivinar un codigo de ",cant_digitos, "digitos distintos")
	propuesta = input("Que codigo propones?: ")

	intentos = 1

	while propuesta != codigo:
		intentos = intentos + 1
		aciertos = 0
		coincidencias = 0
		for i in range(cant_digitos):
			if propuesta[i] == codigo[i]:
				aciertos = aciertos + 1 
			elif propuesta[i] in codigo:
				coincidencias = coincidencias + 1
		print("Tu propuesta(",propuesta,") tiene ",aciertos,"aciertos y ", coincidencias,"coincidencias")
		propuesta = input("Escribe otro codigo: ")

	print("Enhorabuena adivinaste el codigo en", intentos,"intentos")
	continuar1 = int(input("Quiere seguir jugando?: 1-SI  0-NO"))
	if continuar1 == continuar:
		pass
		
	elif continuar1 != continuar:
		break
