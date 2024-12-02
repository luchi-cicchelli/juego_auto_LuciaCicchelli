import pygame

pygame.init()

ANCHO = 800
ALTO = 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("OutRun-copia")

COLORES = {
    "NEGRO": (0, 0, 0),
    "BLANCO": (255, 255, 255),
    "GRIS": (50, 50, 50),
    "VERDE": (0, 200, 0),
    "AZUL": (0, 0, 255),
    "ROSA": (255, 182, 193)
}


imagen_coche = pygame.image.load("coche_jugador.png").convert_alpha()
imagen_coche = pygame.transform.scale(imagen_coche, (50, 100))

imagen_obstaculo = pygame.image.load("coche_enemigo.png").convert_alpha()
imagen_obstaculo = pygame.transform.scale(imagen_obstaculo, (50, 100))
