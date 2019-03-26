import json
with open("movies.json") as fichero:
    doc=json.load(fichero)
from funciones import peliculainfo

while (True):
    print('''
    Elige una opcion:
    1-
    2-
    3-
    4-
    5-
    0-Salir''')
    opcion=int(input("Opcion: "))
    if opcion==1:
        # Listar el título, año y duración de todas las películas.
        for titulo,year,duracion in peliculainfo(doc):
            print ("_"*120)
            print ("Titulo:",titulo,"Año:",year,"Duración:",duracion)
            print ("")

    elif opcion==2:
        # Mostrar los títulos de las películas y el número de actores/actrices que tiene cada una.
        for titulo,actores in peliculainfo(doc):
            print ("_"*50)
            print ("Titulo:",titulo,"Nº de Actores:",actores)

    elif opcion == 0:
        break;
    else:
        print("No existe")
