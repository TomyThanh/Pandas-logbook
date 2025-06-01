import numpy as np
import pandas as pd

#Fehlende Daten / Missing Values

dataframe = pd.DataFrame({"A":[1,2,np.nan,4],
                          "B":[5,np.nan,np.nan,8],
                          "C":[10,20,30,40]})

#Entfernen von Fehlenden Werten
dataframekeinNaN = dataframe.dropna(axis = 1) #Entfernt alle Zeilen oder Spalten mit axis = 0 | 1, die einen Numpy-NaN Wert haben
dataframeThreshold = dataframe.dropna(thresh=2) #Entfernt alle Zeilen oder Spalte, aber entfernt nicht wenn 2 gültige Werte da sind


#Befüllen von Fehlenden Werten
dataframeBefüllt = dataframe.fillna(value="Füller") #Füllt alle NaN-Werte mit value = "Füller"
dataframeDurchschnitt = dataframe.mean()
dataframeDurchschnittFill = dataframe.fillna(dataframeDurchschnitt) #Füllt alle NaN-Werte mit dem Durchschnitt deren Spalten
