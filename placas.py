import pygame
import cores
import entidades

class Placa(entidades.Entidade):
#Atributos
	def __init__(self, largura, altura, x, y, cor, tipo):
		self.tipo = tipo
		if(self.tipo == 0): cor = cores.cinza
		elif(self.tipo == 1): cor = cores.verde
		elif(self.tipo == 2): cor = cores.azul
		elif(self.tipo == 3): cor = cores.vermelho
		entidades.Entidade.__init__(self, largura, altura, x, y, cor)


		