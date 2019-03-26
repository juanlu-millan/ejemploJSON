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
