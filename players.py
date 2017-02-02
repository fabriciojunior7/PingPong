import pygame
import cores
import entidades

class Player(entidades.Entidade):
	#Atributos
	def __init__(self, largura, altura, x, y, cor):
		entidades.Entidade.__init__(self, largura, altura, x, y, cor)
		self.movimento = [False, False]
		self.velocidadeX = 3

	#Metodos
	def botaoPressionado(self, key):
		if(key == 97):
			self.movimento[0] = True
		if(key == 100):
			self.movimento[1] = True


	def botaoSolto(self, key):
		if(key == 97):
			self.movimento[0] = False
		if(key == 100):
			self.movimento[1] = False

	def atualizarPosicao(self, largura, altura):
		if(self.movimento[0] == True and self.x > 0):
			self.x -= self.velocidadeX
		elif(self.movimento[1] == True and self.x < (largura - self.largura)):
			self.x += self.velocidadeX

		#print(self.movimento)
