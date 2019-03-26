import json
with open("movies.json") as fichero:
    doc=json.load(fichero)
from funciones import peliculainfo
from funciones import peliculaactores
from funciones import peliculasfrase
from funciones import peliculasactor

while (True):
    print('''
    Elige una opcion:
    1-Listar el título, año y duración de todas las películas.
    2-Mostrar los títulos de las películas y el número de actores/actrices que tiene cada una.
    3-Mostrar las películas que contengan en la sinopsis dos palabras dadas.
    4-Mostrar las películas en las que ha trabajado un actor dado.
    5-Mostrar el título y la url del póster de las tres películas con una media de puntuaciones más alta y lanzadas entre dos fechas dadas.
    0-Salir''')
    opcion=int(input("Opcion: "))

        # Listar el título, año y duración de todas las películas.
    if opcion==1:
        for titulo,year,duracion in peliculainfo(doc):
            print ("_"*120)
            print ("Titulo:",titulo,"Año:",year,"Duración:",duracion)
            print ("")

        # Mostrar los títulos de las películas y el número de actores/actrices que tiene cada una.
    elif opcion==2:
        for titulo,actores in peliculaactores(doc):
            print ("_"*50)
            print ("Titulo:",titulo,"Nº de Actores:",actores)

        # Mostrar las películas que contengan en la sinopsis dos palabras dadas.
    elif opcion == 3:
        palabra1 = input("Dime una palabra:")
        palabra2 = input("Dime segunda palabra:")
        for titulo in peliculasfrase(doc,palabra1,palabra2):
            print (titulo)

        # Mostrar las películas en las que ha trabajado un actor dado.
    elif opcion == 4:
        actor = input("Dime un actor:")

        for pelis in peliculasactor(doc,actor):
            print (pelis)

    elif opcion == 0:
        break;
    else:
        print("No existe")
