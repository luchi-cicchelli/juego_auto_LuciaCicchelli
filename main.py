import pygame
from configuraciones import *
from archivos import *
from pantalla import *
from logica import *
import sys
import random
from mapa import*

def main():
    """    Función principal que ejecuta el juego.

    Inicializa Pygame, configura el juego, maneja la lógica del juego, y controla las interacciones del usuario,
    como el movimiento del coche, la generación de obstáculos, la puntuación, y las condiciones de finalización del juego.
    """
    pygame.init()
    nombre_usuario = pantalla_inicial()
    pygame.mixer.music.load("sonido_carrera.mp3")
    pygame.mixer.music.play(-1)

    coche = pygame.Rect(ANCHO // 2 - 25, ALTO - 120, 50, 100)
    velocidad_coche = 5
    reloj = pygame.time.Clock()
    obstaculos = generar_obstaculos_unicos(3)
    velocidad_obstaculos = 5
    puntuacion = 0
    fuente = pygame.font.Font(None, 36)
    desplazamiento_lineas = 0

    filas = 10  
    columnas = 5
    mapa = generar_mapa_carretera(filas, columnas)
    mostrar_mapa(mapa) 

    jugando = True
    while jugando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT] and coche.left > ANCHO // 4:
            coche.x -= velocidad_coche
        if teclas[pygame.K_RIGHT] and coche.right < 3 * ANCHO // 4:
            coche.x += velocidad_coche

        pantalla.fill(COLORES["NEGRO"])
        pygame.draw.rect(pantalla, COLORES["VERDE"], (0, 0, ANCHO // 4, ALTO))
        pygame.draw.rect(pantalla, COLORES["VERDE"], (3 * ANCHO // 4, 0, ANCHO // 4, ALTO))
        pygame.draw.rect(pantalla, COLORES["GRIS"], (ANCHO // 4, 0, ANCHO // 2, ALTO))

        dibujar_lineas_carretera(pantalla, COLORES["BLANCO"], ANCHO // 2 - 10, ALTO, desplazamiento_lineas)
        desplazamiento_lineas += 5  
        if desplazamiento_lineas >= 30:
            desplazamiento_lineas = 0

        for obstaculo in obstaculos:
            pantalla.blit(imagen_obstaculo, (obstaculo.x, obstaculo.y))
            obstaculo.y += velocidad_obstaculos

            if obstaculo.top > ALTO:
                obstaculo.y = -100
                obstaculo.x = random.randint(ANCHO // 4, 3 * ANCHO // 4 - 50)
                puntuacion += 10

            if coche.colliderect(obstaculo):
                mensaje = "¡Has chocado!"
                pygame.mixer.music.stop()
                guardar_mejor_puntuacion(nombre_usuario, puntuacion)
                guardar_partida(nombre_usuario, puntuacion)
                pantalla_final(mensaje, puntuacion)
                jugando = False

        pantalla.blit(imagen_coche, (coche.x, coche.y))
        texto_puntuacion = fuente.render(f"Puntos: {puntuacion}", True, COLORES["BLANCO"])
        pantalla.blit(texto_puntuacion, (10, 10))

        if puntuacion >= 600:
            mensaje = "¡Has ganado la carrera!"
            pygame.mixer.music.stop()
            guardar_mejor_puntuacion(nombre_usuario, puntuacion)
            guardar_partida(nombre_usuario, puntuacion)
            pantalla_final(mensaje, puntuacion)
            jugando = False

        pygame.display.flip()
        reloj.tick(60)

if __name__ == "__main__":
    main()
