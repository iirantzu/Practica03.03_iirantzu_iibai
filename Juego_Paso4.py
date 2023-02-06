import pygame
from random import randint


pygame.init()
ventana = pygame.display.set_mode((640, 500))
pygame.display.set_caption("Paso 4")

ball = pygame.image.load("vigu2.png")
ballrect = ball.get_rect()
speed = [randint(3, 6), randint(3, 6)]
ballrect.move_ip(0, 0)
ball_dir = [1, 1]

barra = pygame.image.load("sichan.png")
barrarect = barra.get_rect()
barrarect.move_ip(240, 450)
barrarect_speed = 1

fuente = pygame.font.Font(None, 36)

jugando = True
while jugando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        barrarect = barrarect.move(-3, 0)
    if keys[pygame.K_RIGHT]:
        barrarect = barrarect.move(3, 0)

    if barrarect.colliderect(ballrect):
        speed[1] = -speed[1]
    if barrarect.colliderect(ballrect):
        ball_dir[1] = -ball_dir[1]
        if barrarect_speed >= 8:
            barrarect_speed = barrarect_speed + 0.5


    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > ventana.get_width():
        speed[0] = -speed[0]
    if ballrect.top < 0:
        speed[1] = -speed[1]

    # La pelota al tocar la barra de abajo se termina el juego y además imprime un texto de “GAME OVER”.
    if ballrect.bottom > ventana.get_height():
        texto = fuente.render("Game Over", True, (125, 125, 125))
        texto_rect = texto.get_rect()
        texto_x = ventana.get_width() / 2 - texto_rect.width / 2
        texto_y = ventana.get_height() / 2 - texto_rect.height / 2
        ventana.blit(texto, [texto_x, texto_y])
    else:
        ventana.fill((252, 243, 207))
        ventana.blit(ball, ballrect)
        ventana.blit(barra, barrarect)

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
