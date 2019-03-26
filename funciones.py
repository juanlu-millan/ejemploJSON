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

def peliculasfrase(doc):
    listafrase = []
    for i in doc:
        if palabra1 and palabra2 in i["storyline"]:
            listafrase.appendi(i["title"])
