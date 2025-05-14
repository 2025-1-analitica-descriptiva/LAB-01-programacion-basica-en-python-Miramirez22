"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    with open('files/input/data.csv', 'r') as file:
        lines = file.readlines()

    letter_values = {}

    for line in lines:
        columns = line.strip().split()
        if len(columns) > 2:
            letter = columns[0]
            value = int(columns[1])

            if letter not in letter_values:
                letter_values[letter] = [value, value]
            else:
                letter_values[letter][0] = max(letter_values[letter][0], value)
                letter_values[letter][1] = min(letter_values[letter][1], value)

    result = [(letter, values[0], values[1]) for letter, values in letter_values.items()]
    result = sorted(result, key=lambda x: x[0])
    return result