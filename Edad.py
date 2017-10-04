# -*- coding: utf-8 -*-
class Edad():

	def calcular_edad(self,edad):
		if  type(edad) is not str:
			if edad<=0:
				return 'No existes'
			if edad<=12:
				return 'Eres niño'
			if edad<=17:
				return 'Eres adolescente'
			if edad<=64:
				return 'Eres adulto'
			if edad<=120:
				return 'Eres adulto mayor'
			else:
				return 'Eres Mumm-Ra'

		else:
			return 'Datos incorrectos'

