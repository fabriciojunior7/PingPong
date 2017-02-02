import pygame
import cores

class Entidade(object):
	#Atributos
	def __init__(self, x, y, largura, altura):
		self.x = x
		self.y = y
		self.largura = largura
		self.altura = altura
		self.corpo = pygame.Rect(self.x, self.y, self.largura, self.altura)

	#Metodos
	def desenhar(self, tela):
		self.corpo = pygame.Rect(self.x, self.y, self.largura, self.altura)
		pygame.draw.rect(tela, cores.preto, self.corpo)