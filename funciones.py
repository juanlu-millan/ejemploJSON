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

def peliculainfo(doc):
    for i in doc:
        listapelis = []
        listaactores = []
        listapelis.append(i["title"])
        listaactores.append(len(i["actors"]))
    return zip (listapelis,listaactores)
