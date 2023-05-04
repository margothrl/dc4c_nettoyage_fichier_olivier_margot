import pandas as pd

#Étape 1 : supprimer toutes les lignes ayant au moins une cellule vide
df = pd.read_csv("test.csv").dropna()
df.to_csv("test.csv", index=False)

#Étape 2 : garder uniquement les colonnes : Period, Data_value et Series_title_2
#df = df.drop(columns=['Series_reference', 'Suppressed', 'STATUS', 'UNITS', 'Magnitude', 'Subject', 'Group', 'Series_title_1', 'Series_title_3', 'Series_title_4', 'Series_title_5'])

#Étape 3 : filtrer les résultats en ne gardant que les résultats avec Credit, Debit et Services dans la colonne Series_title_2