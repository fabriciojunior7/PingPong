import pygame, sys
import cores
import players, bolas

largura = 900
altura = 600

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("O Jogo!")
relogio = pygame.time.Clock()
frames = 60

#Jogadores
larguraJogado = 75
alturaJogador = 5
larguraBola = 10
alturaBola = larguraBola
player1 = players.Player((largura/2) - (larguraJogado/2), 570, larguraJogado, alturaJogador)
bolas = [bolas.Bola((largura/2) - (larguraBola/2), 500, larguraBola, alturaBola)]

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
	player1.desenhar(tela)
	for b in bolas:
		b.desenhar(tela)

















main()
