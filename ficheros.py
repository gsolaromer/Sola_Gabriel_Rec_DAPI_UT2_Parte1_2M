def process_class():

    '''Función que escribe un programa que lea un fichero CSV 
    con las notas de un grupo de alumnos/as 
    en una unidad de trabajo de un módulo y los almacene.

    Parámetros:
        - Fichero class.csv
        - Funciones para leer e imprimir fichero

    Salida:
        - Datos del fichero ordenados en una línea cada alumno
    '''

    with open("class.csv","r") as file:
        x = file.readlines()
        print(x)

    print()
    for i in range(len(x)):
        print(x[i])

    print( len(x[1]))

    return

process_class()