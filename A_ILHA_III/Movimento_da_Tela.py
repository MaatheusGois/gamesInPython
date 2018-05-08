#!/usr/bin/env python

import pygame, random
from pygame.locals import *

if not pygame.font:
    print
    'Atenção, não existem fontes.'

if not pygame.mixer:
    print
    'Atenção, não existe som.'

pygame.init()

vermelho = (255, 0, 0)
preto = (0, 0, 0)

comprimento_ecra = 640
altura_ecra = 480

ecra = pygame.display.set_mode((comprimento_ecra, altura_ecra))

raio_circulo = 10

xpos = 50
ypos = 50

circulo = pygame.draw.circle(ecra, vermelho, (xpos, ypos), raio_circulo)

movimento_em_x = 1
movimento_em_y = 1

# asteroides
velocidade_do_asteroide = 1
posicao_dos_asteroides_em_x = random.randint(10, 630)
posicao_dos_asteroides_em_y = 0


asteroide = pygame.draw.circle(ecra, vermelho, (posicao_dos_asteroides_em_x, posicao_dos_asteroides_em_y), raio_circulo)
pygame.display.flip()



while True:
    for event in pygame.event.get():
        pass

    pygame.display.flip()
    posicao_dos_asteroides_em_y += velocidade_do_asteroide
    tecla_pressionada = pygame.key.get_pressed()

    if tecla_pressionada[K_LEFT]:
        xpos -= movimento_em_x
        if xpos <= 0:
            xpos = 0

    if tecla_pressionada[K_RIGHT]:
        xpos += movimento_em_x
        if xpos >= 640:
            xpos = 640

    if tecla_pressionada[K_UP]:
        ypos -= movimento_em_y
        if ypos <= 0:
            ypos = 0

    if tecla_pressionada[K_DOWN]:
        ypos += movimento_em_y
        if ypos >= 480:
            ypos = 480
    if posicao_dos_asteroides_em_y > 480:
        posicao_dos_asteroides_em_y = 0
        posicao_dos_asteroides_em_x = random.randint(10, 630)

    ecra.fill(preto)
    circulo = pygame.draw.circle(ecra, vermelho, (xpos, ypos), raio_circulo)
    asteroide = pygame.draw.circle(ecra, vermelho, (posicao_dos_asteroides_em_x, posicao_dos_asteroides_em_y),
                                  raio_circulo)
    pygame.display.flip()