import numpy as np
import pandas as pd

#Weitere nützliche Operatoren für Pandas

dfOne = pd.DataFrame({"k1":["A","A","B","B","C","C"],
                      "col1":[100,200,300,300,400,500],
                      "col2":["NY","CA","WA","WA","AK","NV"]})

dfOneAnzahlunique = dfOne["col2"].nunique() #Gibt die Anzahl der einzigartigen Spalten an
dfOneAnzahl = dfOne["col2"].value_counts() #Gibt die Anzahl der Spalten-Kategorien
dfOneDuplikatelöschen = dfOne.drop_duplicates() #Löscht die Duplikate der Spalten
dfOneNeue = dfOne["Neue Spalte"] = dfOne["col1"] * 10 #Fügt eine neue Spalte hinzu
dfOneIndexMax = dfOne["col1"].idxmax() #Gibt den Index des maximalen Werts
dfOneIndexMin = dfOne["col1"].idxmin() #Gibt den Index des minimalen Werts
dfOneSpalten = dfOne.columns #Gibt die Spalten an
dfOneZeilen = dfOne.index #Gibt die Zeilen/Index an
dfOneSortiert = dfOne.sort_values("col2") #Sortiert die Werte nach col2
dfOneBinär = pd.get_dummies(dfOne["k1"]) #Wandelt die Werte in Binär bzw. boolean
dfAnfangsbuchstabe = dfOne[dfOne["col2"].str.startswith(("W","N"))] #Filtert alle Werte, die mit M oder B anfangen


#Komplexere Methoden
def grabFirstLetter(state):
    return state[0]

dfOne["First Letter"] = dfOne["col2"].apply(grabFirstLetter) # .apply() führt die grabFirstLetter()-Funktion aus


def complexLetter(state):
    if state[0] == "W":
        return "Washington"
    else:
        return "Error 404"

dfOne["State Check"] = dfOne["col2"].apply(complexLetter) # .apply() führt die Funktion complexLetter()-Funktion

#Mapping
dfOnek1NewValues = dfOne["k1"].map({"A":1,"B":2,"C":3}) #Weist die Werte einer Spalte neue Werte hinzu


#Dataframes zusammenfügen
features = pd.DataFrame({"A":[100,200,300,400,500], 
                         "B":[12,13,14,15,16]})
predictions = pd.DataFrame({"pred":[0,1,1,0,1]})
features = pd.concat([features, predictions], axis = 1) #Kombiniert die beiden Dataframes axis = 1
