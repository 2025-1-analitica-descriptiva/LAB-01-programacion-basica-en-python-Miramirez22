"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.


    Rta/
    214

    """
    with open('files/input/data.csv', 'r') as file:
        lines = file.readlines()

    total_sum = 0

    for line in lines:
        columns = line.strip().split()
        if len(columns) > 2:
            try:
                total_sum += int(columns[1])
            except ValueError:
                continue

    return total_sum