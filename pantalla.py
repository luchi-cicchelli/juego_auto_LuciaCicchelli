import os
from configuraciones import COLORES 
import pygame
from configuraciones import*
import sys
from archivos import*
import json

def mostrar_texto(pantalla, texto, tamaño, color, centro):
    """
    Muestra un texto en la pantalla en una posición centrada.

    La función renderiza el texto con la fuente y el color proporcionado,
    y lo dibuja en la pantalla en el centro de la posición especificada.


    Args:
        pantalla (pygame.Surface): La superficie de la pantalla donde se dibuja el texto.
        texto (str): El texto a mostrar.
        tamaño (int): El tamaño de la fuente del texto.
        color (tupla): El color del texto en formato RGB.
        centro (tupla): La posición (x, y) donde se centra el texto en la pantalla.
    """
    fuente = pygame.font.Font(None, tamaño)
    renderizado = fuente.render(texto, True, color)
    rect = renderizado.get_rect(center=centro)
    pantalla.blit(renderizado, rect)

def pantalla_inicial():
    """
    Muestra la pantalla inicial del juego, solicita el nombre de usuario y lo devuelve.
    También incluye un botón para ver el ranking de puntuaciones.
    """
    nombre_usuario = "" 
    fuente = pygame.font.Font(None, 48) 
    mensaje_error = ""  
    boton_rect_iniciar = pygame.Rect(ANCHO // 3, ALTO // 2 + 100, ANCHO // 3, 50)  
    boton_rect_ranking = pygame.Rect(ANCHO // 3, ALTO // 2 + 160, ANCHO // 3, 50)  
    caja_texto_rect = pygame.Rect(ANCHO // 3, ALTO // 2, ANCHO // 3, 50)  

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:  
                x, y = event.pos
                if boton_rect_iniciar.collidepoint(x, y):  
                    if len(nombre_usuario.strip()) > 0: 
                        return nombre_usuario
                    else:
                        mensaje_error = "¡El usuario debe ser ingresado!"  
                elif boton_rect_ranking.collidepoint(x, y):  #
                    mostrar_ranking()

            elif event.type == pygame.KEYDOWN:  
                if event.key == pygame.K_BACKSPACE:  
                    nombre_usuario = nombre_usuario[:-1]  
                elif event.key == pygame.K_RETURN:  
                    if len(nombre_usuario.strip()) > 0:  
                        return nombre_usuario
                else:
                    nombre_usuario += event.unicode  
                    nombre_usuario = nombre_usuario.upper()  

        pantalla.fill(COLORES["ROSA"]) 

        texto_inicio = fuente.render("Ingrese su nombre", True, COLORES["BLANCO"])  
        texto_rect = texto_inicio.get_rect(center=(ANCHO // 2, ALTO // 3)) 
        pantalla.blit(texto_inicio, texto_rect)  

        texto_nombre = fuente.render(nombre_usuario, True, COLORES["NEGRO"])  
        pantalla.blit(texto_nombre, (ANCHO // 3, ALTO // 2)) 

        if mensaje_error:  
            texto_error = fuente.render(mensaje_error, True, (255, 0, 0)) 
            pantalla.blit(texto_error, (ANCHO // 3, ALTO // 2 + 100))  

        pygame.draw.rect(pantalla, COLORES["AZUL"], boton_rect_iniciar)  
        texto_boton_iniciar = fuente.render("INICIAR", True, COLORES["BLANCO"])  
        boton_texto_rect_iniciar = texto_boton_iniciar.get_rect(center=boton_rect_iniciar.center)  
        pantalla.blit(texto_boton_iniciar, boton_texto_rect_iniciar)  

        pygame.draw.rect(pantalla, COLORES["VERDE"], boton_rect_ranking)  
        texto_boton_ranking = fuente.render("Ver Ranking", True, COLORES["BLANCO"])  
        boton_texto_rect_ranking = texto_boton_ranking.get_rect(center=boton_rect_ranking.center)  
        pantalla.blit(texto_boton_ranking, boton_texto_rect_ranking)  

        pygame.draw.rect(pantalla, COLORES["BLANCO"], caja_texto_rect, 3)
        pygame.display.update()

def mostrar_ranking():
    """Muestra el ranking de puntajes de mayor a menor."""
    ranking = cargar_ranking()  
    
    fuente = pygame.font.Font(None, 28) 
    pantalla.fill(COLORES["ROSA"])  

    texto_ranking = fuente.render("Ranking", True, COLORES["BLANCO"])
    texto_rect = texto_ranking.get_rect(center=(ANCHO // 2, ALTO // 6))
    pantalla.blit(texto_ranking, texto_rect)

    y_offset = ALTO // 4
    for i, (nombre, puntaje) in enumerate(ranking):
        texto = fuente.render(f"{i + 1}. {nombre} - {puntaje} puntos", True, COLORES["NEGRO"])
        pantalla.blit(texto, (ANCHO // 4, y_offset))
        y_offset += 30  

    boton_rect = pygame.Rect(ANCHO // 3, ALTO - 100, ANCHO // 3, 50)
    pygame.draw.rect(pantalla, COLORES["AZUL"], boton_rect)
    texto_boton = fuente.render("Volver", True, COLORES["BLANCO"])
    boton_texto_rect = texto_boton.get_rect(center=boton_rect.center)
    pantalla.blit(texto_boton, boton_texto_rect)

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if boton_rect.collidepoint(x, y):
                    return

                
def cargar_ranking():
    """Carga el ranking desde el archivo JSON y lo ordena usando el algoritmo Bubble Sort
    """
    with open('mejores_puntuaciones.json', 'r') as archivo:
        ranking = json.load(archivo)  
    ranking_lista = list(ranking.items())

    n = len(ranking_lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if ranking_lista[j][1] < ranking_lista[j+1][1]:  
                ranking_lista[j], ranking_lista[j+1] = ranking_lista[j+1], ranking_lista[j]
    return ranking_lista


def pantalla_final(mensaje, puntuacion):
    """Muestra la pantalla final con el mensaje y la puntuación final.

    La pantalla final muestra un mensaje personalizado y la puntuación final obtenida en el juego.
    El jugador puede cerrar la ventana al hacer clic en la X de la ventana.


    Args:
        mensaje (str): El mensaje que se muestra en la pantalla final.
        puntuacion (int): La puntuación final obtenida por el jugador.

    """
    pygame.init()
    pantalla = pygame.display.set_mode((800, 600))
    fuente = pygame.font.Font(None, 36) 

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pantalla.fill(COLORES["ROSA"]) 
        texto_mensaje = fuente.render(mensaje, True, COLORES["BLANCO"])
        rect_mensaje = texto_mensaje.get_rect(center=(400, 250))
        pantalla.blit(texto_mensaje, rect_mensaje)

        texto_puntuacion = fuente.render(f"Puntuación final: {puntuacion}", True, COLORES["BLANCO"])
        rect_puntuacion = texto_puntuacion.get_rect(center=(400, 300))
        pantalla.blit(texto_puntuacion, rect_puntuacion)

        pygame.display.flip()


