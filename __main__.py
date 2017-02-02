import pygame, sys, random
import cores
import players, bolas, placas

largura = 900
altura = 600

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Pong")
relogio = pygame.time.Clock()
frames = 60

#Jogadores e Bolas
larguraJogado = 75
alturaJogador = 5
larguraBola = 10
alturaBola = larguraBola
player1 = players.Player((largura/2) - (larguraJogado/2), 570, larguraJogado, alturaJogador, cores.preto)
bolas = [bolas.Bola((largura/2) - (larguraBola/2), 500, larguraBola, alturaBola, cores.preto)]

#Placas
larguraPlaca = 35
alturaPlaca = 15
alturaMinima = 400
numPlacas = 10
todasAsPlacas = []
for i in range(numPlacas):
	x = random.randint(0, (largura - larguraPlaca))
	y = random.randint(0, (alturaMinima - alturaPlaca))
	tipo = 0
	todasAsPlacas.append(placas.Placa(x, y, larguraPlaca, alturaPlaca, cores.preto, tipo))


def main():

	pygame.init()

	while(True):
		for event in pygame.event.get():
			if(event.type == pygame.QUIT):
				pygame.quit()
				sys.exit()

			if(event.type == pygame.KEYDOWN):
				player1.botaoPressionado(event.key)

			if(event.type == pygame.KEYUP):
				player1.botaoSolto(event.key)
				





		#Rodar
		atualizarTela()
















def atualizarTela():
	#Rodar
	pygame.display.update()
	relogio.tick(frames)
	player1.atualizarPosicao(largura, altura)
	for b in bolas:
		if(b.corpo.colliderect(player1.corpo)):
			b.colidiu(player1.x, player1.y, player1.largura)
		b.atualizarPosicao(largura, altura)
	#Desenhar
	tela.fill(cores.branco)
	for e in todasAsPlacas:
		e.desenhar(tela)
	player1.desenhar(tela)
	for b in bolas:
		b.desenhar(tela)

















main()
