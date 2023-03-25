"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""

# Para el conteo de elementos
from collections import Counter

# Para el ordenamiento de registros
from operator import itemgetter

# Cuando se usa una 'r' delante de una cadena, indica que
# la cadena se tratará como una cadena sin formato, lo que
# significa que las barras invertidas se tratarán como
# caracteres literales en lugar de caracteres de escape.

REL_PATH = r"Python\lab---python-basico-sebasnop\data.csv"
CLOUD_PATH = "/home/runner/work/lab---python-basico-sebasnop/lab---python-basico-sebasnop/data.csv"

# Va a cambiar según donde se esté trabajando
WORKING_ON_PC = False

if WORKING_ON_PC:
    DATA_PATH = REL_PATH
else:
    DATA_PATH = CLOUD_PATH

def open_data(data_path: str) -> list:
    """
    Obtiene un archivo de un path dado
    """
    with open(data_path, "r", encoding="utf-8") as file:
        data_opened = file.readlines()
    return data_opened

data = open_data(data_path=DATA_PATH)

# Limpieza de "\n" (saltos de línea)
data = [fila.replace("\n", "") for fila in data]

# Conversión de los strings (filas) a listas
data = [fila.split("\t") for fila in data]

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """

    segunda_columna = [int(fila[1]) for fila in data]

    return sum(segunda_columna)


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordenadas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """

    primera_columna = [fila[0] for fila in data]
    conteo = Counter(primera_columna)
    conteo_lista = list(conteo.items())

    sorted_conteo = sorted(conteo_lista, key=itemgetter(0))

    return sorted_conteo


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordenadas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """

    columnas_1and2 = [(fila[0], int(fila[1])) for fila in data]

    diccionario_p3 = {}

    def agregar_diccionario_p3(tupla: tuple):
        clave = tupla[0]
        numero = tupla[1]

        if clave in diccionario_p3:
            diccionario_p3[clave].append(numero)
        else:
            diccionario_p3[clave] = [numero]

    # Se asigna cada entrada del diccionario a donde debe estar
    for fila in columnas_1and2:
        agregar_diccionario_p3(fila)

    resultados = [(clave, sum(elementos)) for clave, elementos in diccionario_p3.items()]
    sorted_resultados = sorted(resultados, key=itemgetter(0))

    return sorted_resultados


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """

    # Columna de fechas YYYY-MM-DD
    columna_3 = [fila[2] for fila in data]

    meses = [fecha.split('-')[1] for fecha in columna_3]

    conteo = Counter(meses)
    conteo_lista = list(conteo.items())

    sorted_conteo = sorted(conteo_lista, key=itemgetter(0))

    return sorted_conteo


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """

    columnas_1and2 = [(fila[0], int(fila[1])) for fila in data]

    # Tendrá la estructura "Letra": [max, min]
    diccionario_p5 = {}

    def verificar_diccionario_p5(tupla: tuple):
        clave = tupla[0]
        numero = tupla[1]

        if clave in diccionario_p5:
            max_actual, min_actual = diccionario_p5[clave]
            if numero < min_actual:
                diccionario_p5[clave][1] = numero
            if numero > max_actual:
                diccionario_p5[clave][0] = numero
        else:
            diccionario_p5[clave] = [numero, numero]

    for fila in columnas_1and2:
        verificar_diccionario_p5(fila)

    resultados = [(clave, elementos[0], elementos[1])
                    for clave, elementos in diccionario_p5.items()]

    sorted_resultados = sorted(resultados, key=itemgetter(0))

    return sorted_resultados


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """

    columna_5 = [fila[4] for fila in data]

    # Obtiene los datos de forma ['jjj:12', 'bbb:3']
    pares_sep = [fila.split(",") for fila in columna_5]

    # Una fila estaba siendo ['jjj:12', 'bbb:3']
    # Un par estaba siendo 'jjj:12'
    key_value_sep = [(par.split(":")[0], int(par.split(":")[1]))
                    for fila in pares_sep for par in fila]

    # Tendrá la estructura "Letra": [min, max]
    diccionario_p6 = {}

    for letras, numero in key_value_sep:
        if letras in diccionario_p6:
            min_actual, max_actual = diccionario_p6[letras]
            if numero < min_actual:
                diccionario_p6[letras][0] = numero
            if numero > max_actual:
                diccionario_p6[letras][1] = numero
        else:
            diccionario_p6[letras] = [numero, numero]

    resultados = [(clave, elementos[0], elementos[1])
                    for clave, elementos in diccionario_p6.items()]

    sorted_resultados = sorted(resultados, key=itemgetter(0))

    return sorted_resultados

def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """

    columnas_2and1 = [(int(fila[1]), fila[0]) for fila in data]

    diccionario = {}

    for numero, letra in columnas_2and1:
        if numero in diccionario:
            diccionario[numero].append(letra)
        else:
            diccionario[numero] = [letra]

    resultados = [(clave, elementos) for clave, elementos in diccionario.items()]
    sorted_resultados = sorted(resultados, key=itemgetter(0))

    return sorted_resultados


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """

    columnas_2and1 = {(int(fila[1]), fila[0]) for fila in data}

    diccionario = {}

    for numero, letra in columnas_2and1:
        if numero in diccionario:
            diccionario[numero].append(letra)
        else:
            diccionario[numero] = [letra]

    resultados = [(clave, sorted(elementos)) for clave, elementos in diccionario.items()]

    sorted_resultados = sorted(resultados, key=itemgetter(0))

    return sorted_resultados


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """

    columna_5 = [fila[4] for fila in data]

    # Pares nnn:000 separados
    pares_sep = [fila.split(",") for fila in columna_5]

    # Obtener solo las letras nnn de un par nnn:000
    solo_letras = [par.split(":")[0] for fila in pares_sep for par in fila]

    conteo = Counter(solo_letras)
    conteo_lista = list(conteo.items())

    sorted_conteo = sorted(conteo_lista, key=itemgetter(0))
    conteo_diccionario = dict(sorted_conteo)

    return conteo_diccionario


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """

    resultado = [
        (
            fila[0],
            len(fila[3].split(",")),
            len(fila[4].split(","))
        )
        for fila in data]

    return resultado


def pregunta_11():
    """
    Retorne un diccionario que contenga la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """

    columnas_2and4 = [[int(fila[1]), fila[3].split(",")] for fila in data]

    diccionario = {}

    for fila in columnas_2and4:
        numero = fila[0]

        if numero != 0:
            letras = fila[1]

            for letra in letras:
                if letra in diccionario:
                    diccionario[letra] += numero
                else:
                    diccionario[letra] = numero

    sorted_diccionario = dict(sorted(diccionario.items()))

    return sorted_diccionario


def pregunta_12():
    """
    Genere un diccionario que contenga como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """

    columnas_1and5 = [[fila[0], fila[4].split(",")] for fila in data]

    diccionario = {}

    for fila in columnas_1and5:
        letra = fila[0]
        pares = fila[1]

        numeros = [int(par.split(":")) for par in pares]
        suma = sum(numeros)

        if letra in diccionario:
            diccionario[letra] += suma
        else:
            diccionario[letra] = suma

    sorted_diccionario = dict(sorted(diccionario.items()))

    return sorted_diccionario
