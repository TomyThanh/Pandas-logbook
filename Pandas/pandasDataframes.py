import numpy as np
import pandas as pd

np.random.seed(42)

spalten = ["W","X","Y","Z",]
zeilen = ["A","B","C","D","E"]

data = np.random.randint(-100,100,(5,4))

dataFrame = pd.DataFrame(data, zeilen, spalten) #Erstellt ein Dataframe (Wie eine Excel-Tabelle), (Werte, Zeilen, Spalten)

#Slicing und Indexierung
spalteW = dataFrame["W"] #Gibt die Spalte W aus, das eine Series ist
zweiSpalten = dataFrame[["W", "Z"]] #AUFPASSEN zwei [] Klammern
zeileA = dataFrame.loc["A"] #Gibt die Zeile A aus, das eine Series sit
zweiZeilen = dataFrame.loc[["A","E"]] #Gibt zwei Zeilen aus
zeileA2 = dataFrame.iloc[[0,1]] #Gibt die erste Zeile aus
zeileAbisC = dataFrame.iloc[0:3] #Gibt die erste bis zur dritten Zeile aus n:m (m wird nicht ausgegeben)
zeileSpaltenSlicing = dataFrame.loc[["A","D"], ["W", "Z"]] #Slicing von Zeilen und Spalten 
bedingteSpalteSlicing = dataFrame[dataFrame["X"] > 0] #Slicing von Werten in Spalte x ob größer als 0


#Methoden zu DataFrames
dataFrame["J"] = dataFrame["W"] + dataFrame["Y"] #Fügt eine neue Spalte zum Dataframe (Summe von Spalte W und Y)
dataFrameSpaltelöschen = dataFrame.drop("J", axis = 1) #Entfernt eine Spalte bei axis = 1 und wenn Zeile dann axis = 0
dataFrameZeilelöschen = dataFrame.drop("C", axis = 0) #Löscht eine Zeile bei axis = 0
bedingtesDataframe = dataFrame > 0 #Prüft Werte in Dataframe ob größer als 0 sind
bedingtesDataframe = dataFrame[dataFrame>0] #Gibt nur alle Werte, die die Bedingung erfüllen
bedingteSpalte = dataFrame["X"] > 0 #Prüft Werte in Spalte X ob größer als 0 und gib dann die Zeilen aus
zweiBedingungenSpalte = dataFrame[(dataFrame["W"]>0) & (dataFrame["Y"]>1)] #Prüft ob beide Bedingungen in den Spalte W oder Y zutrifft und gib dann die Zeilen aus & = und, | = oder

dataFrameReset = dataFrame.reset_index() #Setzt die Zeilen zurück und gibt die alten Zeilen als neue Spalte
newIndex = "BY", "BW", "NRW", "HI", "BE"
dataFrame.loc[len(dataFrame)] = .... #Erstellt eine neue Zeile
dataFrame = dataFrame.set_index("States") #Setzt den Index bzw. Zeilen zu "States"
dataFrame.transpose() #Vertauscht Zeile und Spalte

dataFrame.describe() #Gibt nützliche Informationen pro Spalte aus
dataFrame.info() #Gibt weitere nützliche Informationen wie z. B. dtype
dataFrame.dtypes() #Gibt die dtype der Spalten aus
