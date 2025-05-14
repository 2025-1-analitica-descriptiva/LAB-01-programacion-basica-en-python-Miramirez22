"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """
    
    with open('files/input/data.csv', 'r') as file:
        lines = file.readlines()

    letter_count = {}

    
    for line in lines:
        columns = line.strip().split()
        if len(columns) > 0:  
            letter = columns[0]  
            if letter in letter_count:
                letter_count[letter] += 1  
            else:
                letter_count[letter] = 1  

    
    sorted_letter_count = sorted(letter_count.items())

    return sorted_letter_count