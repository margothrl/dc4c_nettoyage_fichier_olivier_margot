import pandas as pd

#En suivant la consigne, étape par étape, on s'est rendu compte qu'il fallait réadapter l'odre des tâches pour obtenir le bon rendu. 
# Voici donc comment nous avons fait :

#Étape 1 : garder uniquement les colonnes : Period, Data_value et Series_title_2
#df = pd.read_csv("test.csv")
#df = df.drop(columns=["Series_reference"]) # supprimer la colone 1 pour tester
#df = df.drop(columns=['Suppressed', 'STATUS', 'UNITS', 'Magnitude', 'Subject', 'Group', 'Series_title_1', 'Series_title_3', 'Series_title_4', 'Series_title_5']) #supprimer les autres colones
#df.to_csv("test.csv", index=False)

#Étape 2 : filtrer les résultats en ne gardant que les résultats avec Credit, Debit et Services dans la colonne Series_title_2
#df = pd.read_csv("test.csv")
#df = df[df.Series_title_2.isin(["Credit", "Debit", "Services"])]
#df.to_csv("test.csv", index=False)

#Étape 3 : ajouter une colonne id, auto-incrémenté
#df = pd.read_csv("test.csv") 
#df = df[df.Series_title_2.isin(["Credit", "Debit", "Services"])] 
#df.insert(0, "id", range(1, len(df)+1)) 
#df.to_csv("test.csv", index=False)

#Étape 4 : supprimer toutes les lignes ayant au moins une cellule vide
#df = pd.read_csv("test.csv").dropna()
#df.to_csv("test.csv", index=False)

#Étape 5 : écrire le nouveau jeu de donnée dans un fichier result.csv
df = pd.read_csv("test.csv") 
df.to_csv("result.csv", index=False)
