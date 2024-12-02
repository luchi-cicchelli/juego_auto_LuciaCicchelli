def generar_mapa_carretera(filas, columnas):
    """Genera un mapa de carretera representado por una matriz de 0 y 1.

    Cada celda en la matriz puede ser un 0 o un 1, donde los 1 representan las zonas de la carretera
    y los 0 las zonas vacías o sin carretera. La matriz es de tamaño filas x columnas. 
    Los 1 se colocan en las posiciones donde tanto el índice de fila es par como el índice de columna
    es múltiplo de 3.

    Args:
        filas (int): El número de filas del mapa.
        columnas (int): El número de columnas del mapa.

    Returns:
        lista: Una lista de listas (matriz) que representa el mapa de la carretera.
              Los valores de la matriz son 0s y 1s, donde 1 representa una sección de la carretera.
    """
    mapa = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            if i % 2 == 0 and j % 3 == 0:  
                fila.append(1)  
            else:
                fila.append(0) 
        mapa.append(fila)
    return mapa

def mostrar_mapa(mapa):
    """  Muestra el mapa de la carretera en forma de texto. Esta función imprime cada fila del mapa, donde los 1 y 0 son representados
    como caracteres en cada celda. Las filas se separan por saltos de línea.

    Args:
        mapa (list): El mapa de la carretera representado como una lista de listas,
                     donde cada elemento es un 0 o un 1.
    """
    for fila in mapa:
        print(' '.join(str(x) for x in fila))
