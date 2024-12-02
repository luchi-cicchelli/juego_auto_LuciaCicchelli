import pygame
import random
from configuraciones import *

def actualizar_obstaculos(obstaculos, velocidad, ancho_pista, puntuacion):
    """Actualiza la posición de los obstáculos y gestiona la reposición de los mismos cuando salen de la pantalla.

    Cada obstáculo se mueve hacia abajo a la velocidad indicada. Si un obstáculo supera la altura de la pantalla,
    se reposiciona en la parte superior con una nueva posición aleatoria en el eje X y se incrementa la puntuación.

    Args:
        obstaculos (lista): Lista de objetos pygame.Rect que representan los obstáculos.
        velocidad (int): La velocidad a la que los obstáculos se mueven hacia abajo.
        ancho_pista (tupla): Una tupla que define los límites del ancho de la pista
        puntuacion (int): La puntuación actual del jugador.


    Returns:
        int: La puntuación actualizada.
    """
    for obstaculo in obstaculos:
        obstaculo.y += velocidad
        if obstaculo.top > ALTO:
            obstaculo.y = -100
            obstaculo.x = random.randint(ancho_pista[0], ancho_pista[1] - 50)
            puntuacion += 10
    return puntuacion

def verificar_colisiones(coche, obstaculos):
    """Verifica si el coche ha colisionado con algún obstáculo.

    Compara la posición del coche con la de los obstáculos para detectar colisiones. Si el coche se superpone
    con alguno de los obstáculos, la función devuelve True, indicando que ocurrió una colisión.

    Args:
        coche (pygame.Rect): El objeto pygame.Rect que representa el coche del jugador.
        obstaculos (lista): objetos pygame.Rect que representan los obstáculos.

    Returns:
        bool: True si el coche colisiona con algún obstáculo, False si no lo hace.  
    """
    for obstaculo in obstaculos:
        if coche.colliderect(obstaculo):
            return True
    return False

def mover_coche(coche, teclas, velocidad, limites):
    """Mueve el coche hacia la izquierda o la derecha dependiendo de las teclas presionadas.

    El movimiento está limitado por los bordes de la pista. Si la tecla de la izquierda es presionada, el coche
    se mueve hacia la izquierda, pero no puede salirse de los límites. Si la tecla de la derecha es presionada,
    el coche se mueve hacia la derecha con las mismas restricciones.


    Args:
        coche (pygame.Rect): El objeto pygame.Rect que representa el coche del jugador.
        teclas (dict): contiene el estado de las teclas presionadas.
        velocidad (int): La velocidad a la que se mueve el coche.
        limites (tupla): define los límites del movimiento del coche (izquierda, derecha).
    """
    if teclas[pygame.K_LEFT] and coche.left > limites[0]:
        coche.x -= velocidad
    if teclas[pygame.K_RIGHT] and coche.right < limites[1]:
        coche.x += velocidad

def dibujar_lineas_carretera(pantalla, color, x_pos, altura, desplazamiento, i=0):
    """ Dibuja las líneas de la carretera que se desplazan hacia abajo para simular el movimiento.

    Las líneas se dibujan a intervalos regulares en el eje Y. El parámetro desplazamiento permite que las líneas
    se muevan hacia abajo a medida que el juego progresa.


    Args:
        pantalla (pygame.Surface): La superficie de la pantalla donde se dibujan las líneas.
        color (tupla): El color de las líneas en formato RGB.
        x_pos (int): La posición X donde se dibujan las líneas de la carretera.
        altura (int): La altura de la pantalla para asegurar que las líneas se dibujan correctamente dentro de la misma.
        desplazamiento (int): El desplazamiento vertical que controla el movimiento de las líneas.
        i (int, opcional): Un índice de recursión para controlar el número de líneas que se dibujan (por defecto es 0).
    """
    if i < 20:
        linea_y = (i * 30 + desplazamiento) % altura
        pygame.draw.rect(pantalla, color, (x_pos, linea_y, 20, 20))
        dibujar_lineas_carretera(pantalla, color, x_pos, altura, desplazamiento, i + 1)

def generar_obstaculos_unicos(num_obstaculos):
    """Genera una lista de obstáculos con posiciones únicas en el eje X dentro de la pista.

    Esta función se asegura de que no haya obstáculos en la misma posición horizontal dentro del rango
    determinado por el ancho de la pista. Si hay colisiones de posiciones, se generan nuevas posiciones
    hasta que se tenga el número deseado de obstáculos únicos.

    Args:
        num_obstaculos (int): El número de obstáculos únicos a generar.

    Returns:
        lista: Una lista de objetos pygame.Rect que representan los obstáculos generados con posiciones únicas.
    """
    posiciones_obstaculos = set()  
    while len(posiciones_obstaculos) < num_obstaculos:
        posicion = random.randint(ANCHO // 4, 3 * ANCHO // 4 - 50)
        posiciones_obstaculos.add(posicion) 
    return [pygame.Rect(pos, -100, 50, 100) for pos in posiciones_obstaculos]


