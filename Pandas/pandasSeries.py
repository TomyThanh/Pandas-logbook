import numpy as np
import pandas as pd

labels = ["a", "b", "c"]
myList = [10,20,30]
array = np.array([10,20,30])
d = {"a": 10, "b":20, "c": 30}

seriesmitArray = pd.Series(array, labels) #pd.Series erstellt eine Pandas-Series data ist der Inhalt und Index ist die Position
seriesDictionary = pd.Series(d) #Dictionary wird in Pd-Series umgewandelt
seriesmitStrList = pd.Series(labels) #Kann auch string-Werte in eine Series tun.

#Beispiele

salesQ1 = pd.Series(data=[250,450,200,150], index = ["Deutschland", "Österreich", "Schweiz", "Frankreich"])


salesQ2 = pd.Series(data=[260,500,200,210], index = ["Polen", "USA", "Schweiz", "Frankreich"])

indexierung1 = salesQ1["Schweiz"] #Index wie bei Dictionaries

summeSales = salesQ1 + salesQ2 #Addiert beide Series





