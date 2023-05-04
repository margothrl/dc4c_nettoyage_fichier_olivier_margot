import pandas as pd

#En suivant la consigne, étape par étape, on s'est rendu compte qu'il fallait réadapter l'odre des tâches pour obtenir le bon rendu. 
# Voici donc comment nous avons fait :

#Étape 1 : garder uniquement les colonnes : Period, Data_value et Series_title_2
df = df.drop(columns=['Series_reference', 'Suppressed', 'STATUS', 'UNITS', 'Magnitude', 'Subject', 'Group', 'Series_title_1', 'Series_title_3', 'Series_title_4', 'Series_title_5'])

#Étape 2 : filtrer les résultats en ne gardant que les résultats avec Credit, Debit et Services dans la colonne Series_title_2

#Étape 3 : ajouter une colonne id, auto-incrémenté

#Étape 4 : supprimer toutes les lignes ayant au moins une cellule vide
#df = pd.read_csv("test.csv").dropna()
#df.to_csv("test.csv", index=False)

#Étape 5 : écrire le nouveau jeu de donnée dans un fichier result.csv