#configurações iniciais
import pygame
import random

pygame.init()
pygame.display.set_caption("Snake")
largura, altura = 1200, 800
tela = pygame.display.set_mode((largura, altura))
relogio = pygame.time.Clock()
ultimoMovimento = "teste"
tamanho_cobra = 1

#cores RGB
preta = (0, 0, 0)
branca = (255, 255, 255)
vermelha = (255, 0, 0)
verde = (0, 255, 0)

#parametro da cobrinha
tamanho_quadrado = 20
velocidade_jogo = 10

def desenhar_comida(tamanho, comida_x, comida_y):
    pygame.draw.rect(tela, verde, [comida_x, comida_y, tamanho, tamanho])

def gerar_comida():
    comida_x = round(random.randrange(0, largura - tamanho_quadrado) / float(tamanho_quadrado)) * float(tamanho_quadrado)
    comida_y = round(random.randrange(0, altura - tamanho_quadrado) / float(tamanho_quadrado)) * float(tamanho_quadrado)
    return comida_x, comida_y

def desenhar_cobra(tamanho, pixels):
    for pixel in pixels:
        pygame.draw.rect(tela, branca, [pixel[0], pixel[1], tamanho, tamanho])

def desenhar_pontuacao(pontuação):
    fonte = pygame.font.SysFont("Helvetica", 30)
    texto = fonte.render(f"Pontos: {pontuação}", True, vermelha)
    tela.blit(texto, [1, 1])

def selecionar_velocidade(tecla):
    global ultimoMovimento
    global velocidade_x
    global velocidade_y
    global tamanho_cobra
    if tecla == pygame.K_DOWN and (ultimoMovimento  != "cima" or tamanho_cobra == 1):
        velocidade_x = 0
        velocidade_y = tamanho_quadrado
        ultimoMovimento = "baixo"
    elif tecla == pygame.K_UP and (ultimoMovimento != "baixo" or tamanho_cobra == 1):
        velocidade_x = 0
        velocidade_y = -tamanho_quadrado
        ultimoMovimento = "cima"
    elif tecla == pygame.K_RIGHT and (ultimoMovimento != "esquerda" or tamanho_cobra == 1):
        velocidade_x = tamanho_quadrado
        velocidade_y = 0
        ultimoMovimento = "direita"
    elif tecla == pygame.K_LEFT and (ultimoMovimento != "direita" or tamanho_cobra == 1):
        velocidade_x = -tamanho_quadrado
        velocidade_y = 0
        ultimoMovimento = "esquerda"
    return velocidade_x, velocidade_y

def rodar_jogo():
    fim_jogo = False

    x = largura / 2
    y = altura / 2

    velocidade_x = 0
    velocidade_y = 0

    global tamanho_cobra
    pixels = []

    comida_x, comida_y = gerar_comida()

    while not fim_jogo:
        tela.fill(preta)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_jogo = True
            elif evento.type == pygame.KEYDOWN:
                velocidade_x, velocidade_y = selecionar_velocidade(evento.key)

        #desenho comida
        desenhar_comida(tamanho_quadrado, comida_x, comida_y)
        
        #ataualizar a posição da cobra
        if x < 0 or x >= largura or y < 0 or y >= altura:
                fim_jogo = True

        x += velocidade_x
        y += velocidade_y

        #desenhar cobra
        pixels.append([x, y])
        if len(pixels) > tamanho_cobra:
            del pixels[0]

        #se a cobrinha bater no propriocorpo
        for pixel in pixels[:-1]:
            if pixel == [x,y]:
                fim_jogo = True

        desenhar_cobra(tamanho_quadrado, pixels)

        #desenhar pontos
        desenhar_pontuacao(tamanho_cobra - 1)

        #atualização da tela
        pygame.display.update()

        #criar nova comida
        if x == comida_x and y == comida_y:
            tamanho_cobra += 1
            comida_x, comida_y = gerar_comida()

        relogio.tick(velocidade_jogo)

rodar_jogo()