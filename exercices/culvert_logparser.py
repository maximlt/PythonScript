# -*- coding: utf-8 -*-
"""Script pour récupérer les données d'un fichier log culvert

Description détaillée:
Le script analyse chaque ligne du fichier à la recherche des données sur
les culverts décrits pas le fichier. Le script affiche le nombre de culverts
trouvés dans le fichier, puis exporte les données au format csv.

Utilisation:
1. Modifier la variable CULVERT_FILE_PATH pour qu'elle indique le chemin vers
   le fichier log culvert. (r"path\to\file" si le chemin contient des
   backslashs)
2. Exécuter le script avec  `python culvert_logparser.py`

Historique:
- ML (10/09/2019): Création du script
"""
# Les imports se placent par convention tout au début du fichier.
# On importe pandas de la manière conventionnelle
import pandas as pd

###############################################################################
############################ Données d'entrée #################################
###############################################################################
CULVERT_FILE_PATH ="culvert_logfile.txt"
###############################################################################

# On déclare un dictionnaire des paramètres qu'on
# va stocker. Chaque "key" du dictionnaire contient
# une liste vide. On a pour objectif d'ajouter les
# informations qu'on trouve dans le fichier à
# chacune de ces listes.
culvert_data = {
    "branch": [],
    "name": [],
    "type": [],
    "diameter": [],
    "length": [],
    "manning": [],
    "upstream_chainage": [],
    "upstream_invert": []
}

# On ouvre le fichier en utilisant le keyword 'with'
# et la fonction 'open' à laquelle on passe le chemin
# du fichier et l'argument "r" (read) pour signifier qu'on
# souhaite uniquement lire le fichier.
# Utiliser 'with' et 'open' garantie que le fichier ouvert
# sera correctement fermé même si une erreur survient
# lorsqu'on travaille avec le fichier ouvert.
with open(CULVERT_FILE_PATH, "r") as f:
    # On crée un compteur qu'on va incrémenter
    # à chaque fois qu'on va trouver un *culvert*
    # dans le fichier texte.
    culvert_count = 0
    # On itère au travers de toutes les lignes du fichier.
    for line in f:
        # line réfère maintenant à la ligne en cours de lecture.
        # Il s'agit d'un objet `string`. Attention, il se
        # termine à chaque fois par "\n" qui est un caractère
        # spécial représentant un saut de ligne.

        # On incrémente le compteur si le texte "START CULVERT"
        # se trouve dans la ligne en cours de lecture
        if "START CULVERT" in line:
            culvert_count += 1

        # On vérifie si la ligne en cours de lecture démarre
        # part le texte "Culvert_branch".
        if line.startswith("Culvert_branch"):
            # Si oui, on enlève les éventuels espaces blancs
            # et caractères spéciaux ("\n", "\t") qui pourrait
            # se trouver au début et/ou à la fin --> strip()
            # Cette méthode retourne un nouvel objet *string*
            # On sépare ensuite la ligne suivant le délimiteur
            # " = ". --> split(" = "). Cette méthode retourne
            # une *list* de *strings*. Le deuxième et dernier
            # élément de cette *list* correspond au nom de
            # la branche. On y accède avec [1].
            # Finalement, on enlève les apostrophes à la fin
            # et au début du nom de la branche --> strip("'")
            # Cette méthode retourne un nouvel objet *string*
            # auquel est associé le nom branch.
            branch = line.strip().split(" = ")[1].strip("'")
            # On ajoute le nom de la branche à la liste de la
            # key "branch" du dictionnaire des sorties.
            culvert_data["branch"].append(branch)

        # On vérifie si la ligne en cours de lecture démarre
        # part le texte "Culvert_name".
        if line.startswith("Culvert_name"):
            # On stocke dans le dictionnaire le nom du culvert
            # en cours de lecture.
            name = line.strip().split(" = ")[1].strip("'")
            culvert_data["name"].append(name)
        # On vérifie si la ligne en cours de lecture démarre
        # part le texte "Culvert_params".
        if line.startswith("Culvert_params"):
            # On récupère l'ensemble des paramètres dans un objet
            # *list* nommé params
            params = line.strip().split(" = ")[1].split(",")
            # On unpack chacun des éléments de la liste (6)
            # On a maintenant 6 nouveaux noms à disposition
            # pour référencer les paramètres du culvert
            t, d, l, m, uc, ui = params
            # On ajoute les paramètres à leur liste dans le
            # dictionnaire.
            culvert_data["type"].append(t)
            culvert_data["diameter"].append(d)
            culvert_data["length"].append(l)
            culvert_data["manning"].append(m)
            culvert_data["upstream_chainage"].append(uc)
            culvert_data["upstream_invert"].append(ui)

# On affiche le nombre de culverts trouvés dans le fichier.
print(f"{culvert_count} culverts ont été trouvés!")

# Un DataFrame est créé à partir de toutes les données du dictionnaires.
df = pd.DataFrame(culvert_data)
# Les données extraites sont enregistrées dans un fichier csv.
# index=False évite d'écrire l'index du DataFrame dans le fichier,
# celui-ci n'étant pas utile ici.
df.to_csv("culvert_data.csv", index=False)
