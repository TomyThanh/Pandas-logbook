import pandas as pd

# Beispiel-Daten für Universitäten in Nevada mit verschiedenen Jahren
data = {
    "Sector": ["Public", "Public", "Private", "Public", "Private"],
    "University": [
        "University of Nevada, Reno",
        "University of Nevada, Las Vegas",
        "Sierra Nevada University",
        "College of Southern Nevada",
        "Nevada State College"
    ],
    "Year": [2022, 2023, 2023, 2024, 2024],  # Verschiedene Jahre
    "Completions": [5000, 7000, 800, 3000, 1200],
    "Location": ["Reno, NV", "Las Vegas, NV", "Incline Village, NV", "Las Vegas, NV", "Henderson, NV"]
}

df = pd.DataFrame(data)

# Groupby Splittet alle Zeilen und fügt die Zeilen zusammen und kombiniert diese.
# Groupby "Year" und den Mittelwert berechnen
df_grouped = df.groupby("Year").mean(numeric_only=True) #.sum() ; .min() oder .max() geht auch
dfDoubleGrouped = df.groupby(["Year", "Sector"]).mean(numeric_only=True) #Nimmt zwei Spalten
print(df)


#Methoden zu df.groupby
dfSortiert = df.groupby("Year").mean(numeric_only=True).sort_index(ascending=False) #Sortiert die Werte absteigend oder aufsteigend
dfInfos = df.groupby("Year").describe() #Gibt die wichtigsten Infos der Gruppen
print(dfInfos)
