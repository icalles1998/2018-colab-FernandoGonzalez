def move(self, velV, velW):
		'''
		Función que hace avanzar y girar al robot al mismo tiempo, según las velocidades V,W dadas como parámetro.

		@type velV, velW: enteros de [1 a 5, a mas, se corta en 5]
		@param velV, velW: velocidades de avance de motores lineal y angular, en m/s y rad/s respectivamente
		'''
		# Puertos de datos para servos izquierdo y derecho
		puertoL = 4
		puertoR = 18

		def esnegativo(n):
			return n < 0

		def espositivo(n):
			return n > 0

		def escero(n):
			return n == 0

		def movermotorizq(vel):

			if(not esnegativo(vel)):

				if(escero(vel)):
					self._dit.set_servo_pulsewidth(puertoL, 1510) #parado 1525
				elif(vel <= 0.0355): #velocidad muy lenta
					self._dit.set_servo_pulsewidth(puertoL, 1529) #hacia el frente, 1526-1537
				elif(vel > 0.0355 and vel <= 0.0655):
					self._dit.set_servo_pulsewidth(puertoL, 1540)
				elif(vel > 0.0655 and vel <= 0.0925):
					self._dit.set_servo_pulsewidth(puertoL, 1550)
				elif(vel > 0.0925 and vel <= 0.13):
					self._dit.set_servo_pulsewidth(puertoL, 1570)
				else: #velocidad muy rapida
					self._dit.set_servo_pulsewidth(puertoL, 2500)
			else:
				if(vel >= -0.0355): #velocidad muy lenta
					self._dit.set_servo_pulsewidth(puertoL, 1498)
				elif(vel < -0.0355 and vel >= -0.0655):
					self._dit.set_servo_pulsewidth(puertoL, 1490)
				elif(vel < -0.0655 and vel >= -0.0925):
					self._dit.set_servo_pulsewidth(puertoL, 1480)
				elif(vel < -0.0925 and vel >= -0.13):
					self._dit.set_servo_pulsewidth(puertoL, 1470)
				else: #velocidad muy rapida
					self._dit.set_servo_pulsewidth(puertoL, 500)

		def movermotordcho(vel):

			if(not esnegativo(vel)):

				if(escero(vel)):
					self._dit.set_servo_pulsewidth(puertoR, 1525) #parado 1510
				if(vel <= 0.0355): #velocidad muy lenta
					self._dit.set_servo_pulsewidth(puertoR, 1510) #hacia el frente, 1510-1512
				elif(vel > 0.0355 and vel <= 0.0655):
					self._dit.set_servo_pulsewidth(puertoR, 1501)
				elif(vel > 0.0655 and vel <= 0.0925):
					self._dit.set_servo_pulsewidth(puertoR, 1490)
				elif(vel > 0.0925 and vel <= 0.13):
					self._dit.set_servo_pulsewidth(puertoR, 1474)
				else: #velocidad muy rapida
					self._dit.set_servo_pulsewidth(puertoR, 500)
			else:
				if(vel >= -0.0355): #velocidad muy lenta
					self._dit.set_servo_pulsewidth(puertoR, 1541)
				elif(vel < -0.0355 and vel >= -0.0655):
					self._dit.set_servo_pulsewidth(puertoR, 1545)
				elif(vel < -0.0655 and vel >= -0.0925):
					self._dit.set_servo_pulsewidth(puertoR, 1559)
				elif(vel < -0.0925 and vel >= -0.13):
					self._dit.set_servo_pulsewidth(puertoR, 1568)
				else: #velocidad muy rapida
					self._dit.set_servo_pulsewidth(puertoR, 2500)

		#Aqui empieza la algoritmia principal

		if(velW != 0):
			rcir = abs(velV / velW) #Es el radio de la circunferencia que tengo que trazar. En valor absoluto
			velmotorgiro = abs(velV) + rcir     #Velocidad a la que tiene que girar el motor encargado del giro del robot
		if(escero(velV) and not escero(velW)):
			#Motor izquierdo hacia atras y motor derecho hacia adelante a velocidad maxima
			if(espositivo(velW)):
				movermotordcho(1)
				movermotorizq(-1)
			else:
				movermotordcho(-1)
				movermotorizq(1)

		elif(not escero(velV) and escero(velW)):
			#Avanza hacia el frente a la velocidad lineal dada
			movermotordcho(velV)
			movermotorizq(velV)

		elif(espositivo(velV) and espositivo(velW)):
			movermotorizq(velV)
			movermotordcho(velmotorgiro)
		elif(espositivo(velV) and esnegativo(velW)):
			movermotorizq(velmotorgiro)
			movermotordcho(velV)
		elif(esnegativo(velV) and espositivo(velW)):
			movermotorizq(-velmotorgiro)
			movermotordcho(velV)
		elif(esnegativo(velV) and esnegativo(velW)):
			movermotorizq(velV)
			movermotordcho(-velmotorgiro)
