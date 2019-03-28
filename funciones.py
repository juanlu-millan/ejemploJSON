import json

def peliculainfo(doc):
    listapelis = []
    listyear = []
    listatiempo  = []
    for i in doc:
        listapelis.append(i["title"])
        listyear.append(i["year"])
        listatiempo.append(i["duration"])
    return zip (listapelis,listyear,listatiempo)

def peliculaactores(doc):
    listapelis = []
    listaactores = []
    for i in doc:
        listapelis.append(i["title"])
        listaactores.append(len(i["actors"]))
    return zip (listapelis,listaactores)

def peliculasfrase(doc,palabrauno,palabrados):
    listafrase = []
    for i in doc:
        if palabrauno and palabrados in i["storyline"]:
            listafrase.append(i["title"])
    return listafrase

def peliculasactor(doc,actor):
    listaactor = []
    for i in doc:
        for a in i["actors"]:
            if a == actor:
                listaactor.append(i["title"])
    return listaactor

def fechapeli(doc,fechasinicio,fechasfin):
    toppuntos = []
    peliculasfecha = []
    fechainicio = fechasinicio.replace("-","")
    fechafin = fechasfin.replace("-","")

    for i in doc:
        fechapeli = i["releaseDate"].replace("-","")
        if fechainicio <= fechapeli and fechapeli <= fechafin:
            puntuacion = sum(i["ratings"])/len(i["ratings"])
            peliculasfecha.append([i["title"],round(sum(i["ratings"])/len(i["ratings"]),2),i["posterurl"]])
            toppuntos.append(round(puntuacion,2))
            puntosordenados = sorted(toppuntos)
            puntosordenados.reverse()

    pelifinal = []
    posterfinal =[]
    for puntos in puntosordenados:
        for pelistop in peliculasfecha:
            if puntos == pelistop[1]:
                pelifinal.append(pelistop[0])
                posterfinal.append(pelistop[2])
    return zip (pelifinal[0:3],posterfinal[0:3])
