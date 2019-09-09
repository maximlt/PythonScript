# -*- coding: utf-8 -*-
"""Script pour analyser des données de culverts enregistrées dans un
fichier csv.

Description détaillée:
Le script ouvre le fichier csv, supprime les données "manning", convertit
les diamètres de m en mm, affiche le diamètre moyen, affiche le diamètre
moyen des culverts en béton, enregistre un camember de la répartition 
des culverts par type, calcule le PK de l'aval de chaque culvert, puis
enregistre le tableau des données transformées dans un fichier csv.

Utilisation:
1. Modifier la variable CULVERT_DATAFILE_PATH pour qu'elle indique le
   chemin vers le fichier data culvert. (r"path\to\file" si le chemin
   contient des backslashs)
2. Exécuter le script avec  `python culvert_dataanalysis.py`

Historique:
- ML (10/09/2019): Création du script
"""
import pandas as pd


###############################################################################
############################ Données d'entrée #################################
###############################################################################
CULVERT_DATAFILE_PATH ="culvert_data.csv"
###############################################################################

# On crée un DataFrame en lisant le fichier d'entrée.
df = pd.read_csv(CULVERT_DATAFILE_PATH)
# On retire la colonne "manning"
df = df.drop(columns=["manning"])
# On multiplie par 1000 chaque valeur de la colonne "diamètre" pour
# les convertir de m en mm.
df["diameter"] = df["diameter"] * 1000
# On calcule le diamètre moyen des culverts
diameter_mean = df["diameter"].mean()
# Et on affiche le résultat, arrondi à deux décimales après la virgule
print(f"Diamètre moyen: {round(diameter_mean, 2)} mm")
# On calcule le diamètre moyen des culverts de type concrete
diameter_conc_mean = df[df["type"] == "concrete"]["diameter"].mean()
# Et on affiche le résultat, arrondi à deux décimales après la virgule
print(f"Diamètre moyen béton: {round(diameter_conc_mean, 2)} mm.")

# On calcule le nombre de culverts par type
count_per_type = df["type"].value_counts()
# On crée un camembert pour montrer la répartition des culverts par type
ax = count_per_type.plot.pie()
fig = ax.get_figure()
# Et on l'enregistre
fig.savefig("culvert_per_type.png")

# On ajoute une colonne downstream_chainage
df["downstream_chainage"] = df["upstream_chainage"] + df["length"]

# On enregistre les données dans un fichier csv
df.to_csv("culvert_analysis.csv")

