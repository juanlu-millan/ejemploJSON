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

    elif opcion == 0:
        break;
    else:
        print("No existe")
