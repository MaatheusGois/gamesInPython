#!/usr/bin/env python

import pygame, random
from pygame.locals import *


pygame.init()

#------------------------------------------- Cores ---------------------------------------------------------------------
vermelho = (255, 0, 0)
azul = (0,0,255)
preto = (0, 0, 0)

#---------------------------------------------Tamanho da tela-----------------------------------------------------------
comprimento_ecra = 640
altura_ecra = 480
ecra = pygame.display.set_mode((comprimento_ecra, altura_ecra))
pygame.display.set_caption('A Ilha 3')
#-------------------------------------------- circulo ------------------------------------------------------------------
raio_circulo = 10

#------------------------------------------ Velocidade e posições ------------------------------------------------------
xpos = 50
ypos = 90
movimento_em_x = 1
movimento_em_y = 1
velocidade_do_asteroide = 1
relogio = pygame.time.Clock()
fps = 180

#--------------------------------------- asteroides que descem (down) --------------------------------------------------
posicao_dos_asteroides_em_x = random.randint(10, 208)
posicao_dos_asteroides_em_x2 = random.randint(228, 416)
posicao_dos_asteroides_em_x3 = random.randint(436, 630)
posicao_dos_asteroides_em_y = 0

#---------------------------------------- asteroides que sobem (Up) ----------------------------------------------------
posicao_dos_asteroides_em_y_up = 480
posicao_dos_asteroides_em_x4 = random.randint(10, 280)
posicao_dos_asteroides_em_x5 = random.randint(228, 416)
posicao_dos_asteroides_em_x6 = random.randint(436, 630)

#----------------------------------------- asteroides à esquerda (Left) ------------------------------------------------
posicao_dos_asteroides_em_x_left = 640
posicao_dos_asteroides_em_y1 = random.randint(10, 130)
posicao_dos_asteroides_em_y2 = random.randint(150, 300)
posicao_dos_asteroides_em_y3 = random.randint(320, 480)

#------------------------------------------ asteroides à direita (Right) -----------------------------------------------
posicao_dos_asteroides_em_x_right = 0
posicao_dos_asteroides_em_y4 = random.randint(10, 130)
posicao_dos_asteroides_em_y5 = random.randint(150, 300)
posicao_dos_asteroides_em_y6 = random.randint(320, 480)


#-------------------------------------------- Loop Principal -----------------------------------------------------------
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.flip()
    relogio.tick(fps)

    #----------------------------------------- asteroides que descem (down) --------------------------------------------
    posicao_dos_asteroides_em_y += velocidade_do_asteroide
    #-----------------------------------------asteroides que sobem (Up) ------------------------------------------------
    posicao_dos_asteroides_em_y_up -= velocidade_do_asteroide
    #-----------------------------------------asteroides à esquerda (Left) ---------------------------------------------
    posicao_dos_asteroides_em_x_left -= velocidade_do_asteroide
    #-----------------------------------------asteroides à direita (Right) ---------------------------------------------
    posicao_dos_asteroides_em_x_right += velocidade_do_asteroide


    #----------------------------------------- Movimento Personagem ----------------------------------------------------
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


    #------------------------------------------- Movimento Asteroides --------------------------------------------------
    elif posicao_dos_asteroides_em_y > 480:
        posicao_dos_asteroides_em_y = 0
        posicao_dos_asteroides_em_x = random.randint(10, 630)
        posicao_dos_asteroides_em_x2 = random.randint(10,630)
        posicao_dos_asteroides_em_x3 = random.randint(10, 630)

    elif posicao_dos_asteroides_em_y_up < 0:
        posicao_dos_asteroides_em_y_up = 480
        posicao_dos_asteroides_em_x4 = random.randint(10, 630)
        posicao_dos_asteroides_em_x5 = random.randint(10,630)
        posicao_dos_asteroides_em_x6 = random.randint(10, 630)

    elif posicao_dos_asteroides_em_x_left < 0:
        posicao_dos_asteroides_em_x_left = 640
        posicao_dos_asteroides_em_y1 = random.randint(10, 130)
        posicao_dos_asteroides_em_y2 = random.randint(150, 300)
        posicao_dos_asteroides_em_y3 = random.randint(320, 480)

    elif posicao_dos_asteroides_em_x_right > 640:
        posicao_dos_asteroides_em_x_right = 0
        posicao_dos_asteroides_em_y4 = random.randint(10, 130)
        posicao_dos_asteroides_em_y5 = random.randint(150, 300)
        posicao_dos_asteroides_em_y6 = random.randint(320, 480)


    #-----------------------------------------  fundo da tela ----------------------------------------------------------
    ecra.fill(preto)

    #---------------------------------------- Circulo Azul ( personagem) -----------------------------------------------
    circulo = pygame.draw.circle(ecra, azul, (xpos, ypos), raio_circulo)

    # ------------------------------------ Asteroids Down ---------------------------------------------------------------
    asteroide = pygame.draw.circle(ecra, vermelho, (posicao_dos_asteroides_em_x, posicao_dos_asteroides_em_y), raio_circulo)
    asteroide2 = pygame.draw.circle(ecra, vermelho, (posicao_dos_asteroides_em_x2, posicao_dos_asteroides_em_y), raio_circulo)
    asteroide3 = pygame.draw.circle(ecra, vermelho, (posicao_dos_asteroides_em_x3, posicao_dos_asteroides_em_y), raio_circulo)

    # ------------------------------------ Asteroids Up -----------------------------------------------------------------
    asteroide4 = pygame.draw.circle(ecra, vermelho, (posicao_dos_asteroides_em_x4, posicao_dos_asteroides_em_y_up), raio_circulo)
    asteroide5 = pygame.draw.circle(ecra, vermelho, (posicao_dos_asteroides_em_x5, posicao_dos_asteroides_em_y_up), raio_circulo)
    asteroide6 = pygame.draw.circle(ecra, vermelho, (posicao_dos_asteroides_em_x6, posicao_dos_asteroides_em_y_up), raio_circulo)

    # ------------------------------------ Asteroids Left --------------------------------------------------------------
    asteroide7 = pygame.draw.circle(ecra, vermelho, (posicao_dos_asteroides_em_x_left, posicao_dos_asteroides_em_y1), raio_circulo)
    asteroide8 = pygame.draw.circle(ecra, vermelho, (posicao_dos_asteroides_em_x_left, posicao_dos_asteroides_em_y2), raio_circulo)
    asteroide9 = pygame.draw.circle(ecra, vermelho, (posicao_dos_asteroides_em_x_left, posicao_dos_asteroides_em_y3), raio_circulo)

    # ------------------------------------ Asteroids Right -------------------------------------------------------------
    asteroide10 = pygame.draw.circle(ecra, vermelho, (posicao_dos_asteroides_em_x_right, posicao_dos_asteroides_em_y4), raio_circulo)
    asteroide11 = pygame.draw.circle(ecra, vermelho, (posicao_dos_asteroides_em_x_right, posicao_dos_asteroides_em_y5), raio_circulo)
    asteroide12 = pygame.draw.circle(ecra, vermelho, (posicao_dos_asteroides_em_x_right, posicao_dos_asteroides_em_y6), raio_circulo)
    pygame.display.flip()

    # ------------------------------------------------- detectando colisão ---------------------------------------------
    if circulo.colliderect(asteroide):
        break
    if circulo.colliderect(asteroide2):
        break
    if circulo.colliderect(asteroide3):
        break
    if circulo.colliderect(asteroide4):
        break
    if circulo.colliderect(asteroide5):
        break
    if circulo.colliderect(asteroide6):
        break
    if circulo.colliderect(asteroide7):
        break
    if circulo.colliderect(asteroide8):
        break
    if circulo.colliderect(asteroide9):
        break
    if circulo.colliderect(asteroide10):
        break
    if circulo.colliderect(asteroide11):
        break

pygame.quit()