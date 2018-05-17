import pygame, random
from pygame.locals import *

pygame.init()

pygame.mixer.music.load("Som/som.wav")
pygame.mixer.music.play()
# ------------------------------------------- Cores ---------------------------------------------------------------------
vermelho = (255, 0, 0)
azul = (0, 0, 255)
preto = (0, 0, 0)
verde = (0, 255, 0)

# ---------------------------------------------Tamanho da tela-----------------------------------------------------------
comprimento_ecra = 640
altura_ecra = 480
ecra = pygame.display.set_mode((comprimento_ecra, altura_ecra))
pygame.display.set_caption('A Ilha 3')
# -------------------------------------------- circulo ------------------------------------------------------------------
raio_circulo = 10

# ------------------------------------------ Velocidade e posições ------------------------------------------------------
xpos = 320
ypos = 240
movimento_em_x = 1
movimento_em_y = 1
velocidade_do_asteroide = 1
relogio = pygame.time.Clock()
fps = 100

# --------------------------------------- asteroides que descem (down) --------------------------------------------------
posicao_dos_asteroides_em_x = random.randint(10, 208)
posicao_dos_asteroides_em_x2 = random.randint(228, 416)
posicao_dos_asteroides_em_x3 = random.randint(436, 630)
posicao_dos_asteroides_em_y_down = -20
posicao_dos_asteroides_em_y_down2 = -20
posicao_dos_asteroides_em_y_down3 = -20

# ---------------------------------------- asteroides que sobem (Up) ----------------------------------------------------
posicao_dos_asteroides_em_y_up = 500
posicao_dos_asteroides_em_y_up2 = 500
posicao_dos_asteroides_em_y_up3 = 500
posicao_dos_asteroides_em_x4 = random.randint(10, 280)
posicao_dos_asteroides_em_x5 = random.randint(228, 416)
posicao_dos_asteroides_em_x6 = random.randint(436, 630)

# ----------------------------------------- asteroides à esquerda (Left) ------------------------------------------------
posicao_dos_asteroides_em_x_left = 660
posicao_dos_asteroides_em_x_left2 = 660
posicao_dos_asteroides_em_x_left3 = 660
posicao_dos_asteroides_em_y1 = random.randint(10, 130)
posicao_dos_asteroides_em_y2 = random.randint(150, 300)
posicao_dos_asteroides_em_y3 = random.randint(320, 480)

# ------------------------------------------ asteroides à direita (Right) -----------------------------------------------
posicao_dos_asteroides_em_x_right = -20
posicao_dos_asteroides_em_x_right2 = -20
posicao_dos_asteroides_em_x_right3 = -20
posicao_dos_asteroides_em_y4 = random.randint(10, 130)
posicao_dos_asteroides_em_y5 = random.randint(150, 300)
posicao_dos_asteroides_em_y6 = random.randint(320, 480)

# ------------------------------------------ recompensas ----------------------------------------------------------------
posicao_da_recompensa_em_x = random.randint(0, 640)
posicao_da_recompensa_em_y = random.randint(0, 480)
score2 = 0
# ------------------------------------------ velocidade do jogo ---------------------------------------------------------
velocidadeDoJogo = 0

# -------------------------------------------- Loop Principal -----------------------------------------------------------
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.flip()

    # ----------------------------------------- asteroides que descem (down) --------------------------------------------
    if velocidadeDoJogo >= 300:
        posicao_dos_asteroides_em_y_down += velocidade_do_asteroide
    if velocidadeDoJogo >= 1500:
        posicao_dos_asteroides_em_y_down2 += velocidade_do_asteroide
    if velocidadeDoJogo >= 2700:
        posicao_dos_asteroides_em_y_down3 += velocidade_do_asteroide

    # -----------------------------------------asteroides que sobem (Up) ------------------------------------------------
    if velocidadeDoJogo >= 600:
        posicao_dos_asteroides_em_y_up -= velocidade_do_asteroide
    if velocidadeDoJogo >= 1800:
        posicao_dos_asteroides_em_y_up2 -= velocidade_do_asteroide
    if velocidadeDoJogo >= 3000:
        posicao_dos_asteroides_em_y_up3 -= velocidade_do_asteroide

    # -----------------------------------------asteroides à esquerda (Left) ---------------------------------------------
    if velocidadeDoJogo >= 900:
        posicao_dos_asteroides_em_x_left -= velocidade_do_asteroide
    if velocidadeDoJogo >= 2100:
        posicao_dos_asteroides_em_x_left2 -= velocidade_do_asteroide

    if velocidadeDoJogo >= 3300:
        posicao_dos_asteroides_em_x_left3 -= velocidade_do_asteroide

    # -----------------------------------------asteroides à direita (Right) ---------------------------------------------
    if velocidadeDoJogo >= 1200:
        posicao_dos_asteroides_em_x_right += velocidade_do_asteroide
    if velocidadeDoJogo >= 2400:
        posicao_dos_asteroides_em_x_right2 += velocidade_do_asteroide
    if velocidadeDoJogo >= 3600:
        posicao_dos_asteroides_em_x_right3 += velocidade_do_asteroide

        # ------------------------------------------VELOCIDADE DO JOGO------------------------------------------------------
    if velocidadeDoJogo >= 300 and velocidadeDoJogo <= 1000:
        fps = 120
    elif velocidadeDoJogo >= 1000 and velocidadeDoJogo <= 1500:
        fps = 125
    elif velocidadeDoJogo >= 1500 and velocidadeDoJogo <= 3000:
        fps = 150
    elif velocidadeDoJogo >= 3000 and velocidadeDoJogo <= 5000:
        fps = 175
    elif velocidadeDoJogo >= 5000 and velocidadeDoJogo <= 8000:
        fps = 200
    elif velocidadeDoJogo >= 8000 and velocidadeDoJogo <= 10000:
        fps = 225
    elif velocidadeDoJogo >= 10000 and velocidadeDoJogo <= 12000:
        fps = 250
    elif velocidadeDoJogo >= 12000 and velocidadeDoJogo <= 14000:
        fps = 275
    elif velocidadeDoJogo >= 14000 and velocidadeDoJogo <= 20000:
        fps = 300
    elif velocidadeDoJogo >= 20000 and velocidadeDoJogo <= 25000:
        fps = 325
    elif velocidadeDoJogo >= 25000 and velocidadeDoJogo <= 30000:
        fps = 350
    elif velocidadeDoJogo >= 30000:
        fps = 375
    relogio.tick(fps)



    # ----------------------------------------- Movimento Personagem ----------------------------------------------------
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

    # ------------------------------------------- Movimento Asteroides --------------------------------------------------
    elif posicao_dos_asteroides_em_y_down > 480:
        posicao_dos_asteroides_em_y_down = 0
        posicao_dos_asteroides_em_x = random.randint(10, 630)


    elif posicao_dos_asteroides_em_y_down2 > 480:
        posicao_dos_asteroides_em_y_down2 = 0
        posicao_dos_asteroides_em_x2 = random.randint(10, 630)

    elif posicao_dos_asteroides_em_y_down3 > 480:
        posicao_dos_asteroides_em_y_down3 = 0
        posicao_dos_asteroides_em_x3 = random.randint(10, 630)

    # -----------------------------------------  Movimento Asteroides ---------------------------------------------------

    elif posicao_dos_asteroides_em_y_up < 0:
        posicao_dos_asteroides_em_y_up = 480
        posicao_dos_asteroides_em_x4 = random.randint(10, 630)

    elif posicao_dos_asteroides_em_y_up2 < 0:
        posicao_dos_asteroides_em_y_up2 = 480
        posicao_dos_asteroides_em_x5 = random.randint(10, 630)

    elif posicao_dos_asteroides_em_y_up3 < 0:
        posicao_dos_asteroides_em_y_up3 = 480
        posicao_dos_asteroides_em_x6 = random.randint(10, 630)

    # ----------------------------------------- Movimento Asteroides  ---------------------------------------------------

    elif posicao_dos_asteroides_em_x_left < 0:
        posicao_dos_asteroides_em_x_left = 640
        posicao_dos_asteroides_em_y1 = random.randint(10, 130)

    elif posicao_dos_asteroides_em_x_left2 < 0:
        posicao_dos_asteroides_em_x_left2 = 640
        posicao_dos_asteroides_em_y2 = random.randint(150, 300)

    elif posicao_dos_asteroides_em_x_left3 < 0:
        posicao_dos_asteroides_em_x_left3 = 640
        posicao_dos_asteroides_em_y3 = random.randint(320, 480)

    # ----------------------------------------- Movimento Asteroides  ---------------------------------------------------

    elif posicao_dos_asteroides_em_x_right > 640:
        posicao_dos_asteroides_em_x_right = 0
        posicao_dos_asteroides_em_y4 = random.randint(10, 130)

    elif posicao_dos_asteroides_em_x_right2 > 640:
        posicao_dos_asteroides_em_x_right2 = 0
        posicao_dos_asteroides_em_y5 = random.randint(150, 300)

    elif posicao_dos_asteroides_em_x_right3 > 640:
        posicao_dos_asteroides_em_x_right3 = 0
        posicao_dos_asteroides_em_y6 = random.randint(320, 480)

    # -----------------------------------------  fundo da tela ----------------------------------------------------------
    ecra.fill(preto)

    # ---------------------------------------- Circulo Azul ( personagem) -----------------------------------------------
    circulo = pygame.draw.circle(ecra, azul, (xpos, ypos), raio_circulo)

    # ------------------------------------ Asteroids fase1 ---------------------------------------------------------------
    asteroide = pygame.draw.circle(ecra, vermelho, (posicao_dos_asteroides_em_x, posicao_dos_asteroides_em_y_down),
                                   raio_circulo)
    asteroide2 = pygame.draw.circle(ecra, vermelho, (posicao_dos_asteroides_em_x2, posicao_dos_asteroides_em_y_down2),
                                    raio_circulo)
    asteroide3 = pygame.draw.circle(ecra, vermelho, (posicao_dos_asteroides_em_x3, posicao_dos_asteroides_em_y_down3),
                                    raio_circulo)

    # ------------------------------------ Asteroids fase2 -----------------------------------------------------------------
    asteroide4 = pygame.draw.circle(ecra, vermelho, (posicao_dos_asteroides_em_x4, posicao_dos_asteroides_em_y_up),
                                    raio_circulo)
    asteroide5 = pygame.draw.circle(ecra, vermelho, (posicao_dos_asteroides_em_x5, posicao_dos_asteroides_em_y_up2),
                                    raio_circulo)
    asteroide6 = pygame.draw.circle(ecra, vermelho, (posicao_dos_asteroides_em_x6, posicao_dos_asteroides_em_y_up3),
                                    raio_circulo)

    # ------------------------------------ Asteroids fase3 --------------------------------------------------------------
    asteroide7 = pygame.draw.circle(ecra, vermelho, (posicao_dos_asteroides_em_x_left, posicao_dos_asteroides_em_y1),
                                    raio_circulo)
    asteroide8 = pygame.draw.circle(ecra, vermelho, (posicao_dos_asteroides_em_x_left2, posicao_dos_asteroides_em_y2),
                                    raio_circulo)
    asteroide9 = pygame.draw.circle(ecra, vermelho, (posicao_dos_asteroides_em_x_left3, posicao_dos_asteroides_em_y3),
                                    raio_circulo)

    # ------------------------------------ Asteroids fase4 -------------------------------------------------------------
    asteroide10 = pygame.draw.circle(ecra, vermelho, (posicao_dos_asteroides_em_x_right, posicao_dos_asteroides_em_y4),
                                     raio_circulo)
    asteroide11 = pygame.draw.circle(ecra, vermelho, (posicao_dos_asteroides_em_x_right2, posicao_dos_asteroides_em_y5),
                                     raio_circulo)
    asteroide12 = pygame.draw.circle(ecra, vermelho, (posicao_dos_asteroides_em_x_right3, posicao_dos_asteroides_em_y6),
                                     raio_circulo)

    # ------------------------------------------ recompensas ----------------------------------------------------------------
    recompensa = pygame.draw.circle(ecra, verde, (posicao_da_recompensa_em_x, posicao_da_recompensa_em_y), raio_circulo)

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
    if circulo.colliderect(asteroide12):
        break



    # ------------------------------------------- Score ----------------------------------------------------------------
    velocidadeDoJogo += 1
    score = velocidadeDoJogo
    fonte = pygame.font.Font(None, 30)
    pontuacao = fonte.render('Pontuação: ' + str(score+score2), 2, azul)
    caixadepontuacao = pontuacao.get_rect()
    ecra.blit(pontuacao, [400, 40])
    pontuacao_final = score+score2

    # ------------------------------------------- Recompensa -----------------------------------------------------------
    if circulo.colliderect(recompensa):
        posicao_da_recompensa_em_x = random.randint(0, 640)
        posicao_da_recompensa_em_y = random.randint(0, 480)
        score2 += 10000
print(pontuacao_final)
pygame.quit()