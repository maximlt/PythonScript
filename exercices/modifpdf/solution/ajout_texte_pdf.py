"""Script pour récupérer les données d'un fichier log culvert

Description détaillée:
Le script lit d'abord les données d'un fichier CSV. Ensuite, il ouvre un fichier 
PDF et ajoute à page le texte formaté extrait du fichier CSV et enregistre le nouveau
fichier PDF.

Utilisation:
1. Modifier les variables PDF_FILE_PATH et CSV_FILE_PATH pour qu'elles indiquent
   le chemin vers les fichiers CSV et PDF. (r"path\to\file" si le chemin contient des
   backslashs)
2. Exécuter le script avec `python ajout_texte_pdf.py` ou F5 dans Spyder.

Dépendances:
- python 3.7
- PyMuPDF 1.17.3

Historique:
- ML (09/07/2020): Création du script
"""
# Les imports se placent par convention tout au début du fichier.
# Import du module CSV de la librairie standard dédié à la gestion des fichiers CSV
import csv
# Import du module système qui permet, entre autres, de quitter le programme
import sys
# Import de PyMuPDF (son nom d'import est différent)
import fitz

###############################################################################
############################ Données d'entrée #################################
###############################################################################
CSV_FILE_PATH = r"..\shapes.csv"
PDF_FILE_PATH = r"..\shapes.pdf"
OUTPUT_PDF_FILE_PATH = r"..\shapes_with_text.pdf"
###############################################################################

# Indique visuellement le départ de l'exécution du script.
print("Starting...")

# Création de listes vides prêtes à contenir les données du fichier CSV.
shape_ids = []
shape_descriptions = []

# Ouverture du fichier texte
with open(CSV_FILE_PATH, mode="r", encoding="utf-8") as csv_file:
    # On utilise l'object DictReader du module CSV qui suppose que la première
    # ligne du fichier CSV est une ligne d'en-tête, ce qui est le cas ici.
    csv_reader = csv.DictReader(csv_file)
    # On peut itérer sur cet objet, et extraire ligne par ligne les données.
    for row in csv_reader:
        shape_ids.append(row["id"])
        shape_descriptions.append(row["description"])


# On ouvre le fichier PDF dans un context manager fourni par la fonction open de PyMuPDF
with fitz.open(PDF_FILE_PATH) as pdf:

    # On vérifie ici que le nombre de page du fichier PDF correspond bien
    # au nombre d'entrée dans le fichier CSV. Sinon on quitte le programme.
    if len(pdf) != len(shape_ids):
        print("Le fichier CSV et le fichier PDF ne contiennent pas le même nombre d'éléments.")
        sys.exit()  # Arrêt du script
    
    # On effectue une boucle au travers des éléments du CSV et des pages du fichier PDF
    for shape_id, shape_description, page in zip(shape_ids, shape_descriptions, pdf):
        # Création du texte à rajouter, \n permet de sauter des lignes
        text = f"ID: {shape_id}\nType: {shape_description}\nAjouté par PyMuPDF"
        # Ajout du texte à chaque page.
        # On note que cela ne modifie pas directement le fichier ouvert, cela enregistre
        # dans la mémoire de nouvelles pages PDF.
        page.insertText(
            fitz.Point(100, 50),  # Position du texte
            text,
            fontsize=10,
            color=(0, 0, 1)  # bleu
        )

    # Lorsque la boucle est terminée, on enregistre le fichier PDF sous un nouveau nom.
    output_pdf_file = r"..\shapes_with_text.pdf"
    pdf.save(OUTPUT_PDF_FILE_PATH)

# Indique visuellement que le script s'est bien executé jusqu'au bout.
print("Done!")