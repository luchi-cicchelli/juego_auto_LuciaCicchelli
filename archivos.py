import json
import os

def guardar_partida(nombre_usuario, puntuacion):
    """ Guarda la partida del jugador en un archivo de texto.

    La partida se guarda en el archivo partidas.txt, añadiendo el nombre del jugador
    y su puntuación al final del archivo en un formato txt.

    Args:
        nombre_usuario (str): El nombre del jugador.
        puntuacion (int): La puntuación obtenida por el jugador en la partida.

    """
    archivo = 'partidas.txt'
    with open(archivo, 'a') as archivo_txt:
        archivo_txt.write(f"{nombre_usuario},{puntuacion}\n")
    
def guardar_mejor_puntuacion(nombre_usuario, puntuacion):
    """Guarda la mejor puntuación del jugador en un archivo JSON.

    Si el jugador ya tiene una puntuación registrada, se actualiza si la nueva puntuación es mayor.
    Si el jugador no tiene una puntuación registrada, se guarda por primera vez.


    Args:
        nombre_usuario (str): El nombre del jugador.
        puntuacion (int): La puntuación obtenida por el jugador.
    """
    archivo_json = "mejores_puntuaciones.json"
    if os.path.exists(archivo_json):
        with open(archivo_json, "r") as archivo:
            datos = json.load(archivo)
    else:
        datos = {}

    if nombre_usuario not in datos or puntuacion > datos[nombre_usuario]:
        datos[nombre_usuario] = puntuacion
        with open(archivo_json, "w") as archivo:
            json.dump(datos, archivo, indent=4)