import pygame
import cores
import entidades

class Bola(entidades.Entidade):
	#Atributos
	def __init__(self, x, y, largura, altura):
		entidades.Entidade.__init__(self, x, y, largura, altura)
		self.velocidadeXMaxima = 5
		self.velocidadeYMaxima = 3
		self.velocidadeX = 0
		self.velocidadeY = -3

	def atualizarPosicao(self, largura, altura):
		if(self.x < 0 or self.x > (largura - self.largura)):
			self.velocidadeX *= -1
		if(self.y < 0 or self.y > (altura - self.altura)):
			self.velocidadeY *= -1

		self.x += self.velocidadeX
		self.y += self.velocidadeY

	def colidiu(self, x, y, largura):
		if((self.x + self.largura/2) < (x + largura/2)):
			self.velocidadeX = -(self.velocidadeXMaxima * (((x + (largura/2.0)) - (self.x + (self.largura/2.0))) / (largura/2.0)))
			print(self.velocidadeX)

		elif((self.x + self.largura/2) > (x + largura/2)):
			self.velocidadeX = -(self.velocidadeXMaxima * (((x + (largura/2.0)) - (self.x + (self.largura/2.0))) / (largura/2.0)))
			print(self.velocidadeX)

		elif((self.x + self.largura/2) == (x + largura/2)):
			self.velocidadeX = 0
			print("No Centro!")

		self.velocidadeY *= -1
		self.y = y - 10
