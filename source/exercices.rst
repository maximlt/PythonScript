Exercices
==========

Récupération d'informations dans un fichier et analyse
--------------------------------------------------------

L'exercice proposée consiste à analyser un fichier *log*. Ce
genre de fichier contient souvent beaucoup de données qui
sont difficiles à lire et analyser directement. Le script à
coder va s'occuper d'extraire le contenu du fichier et
de l'enregistrer au format CSV. L'objectif est ensuite d'analyser
plus en profondeur les données, pour afficher des informations,
créer une figure et enregistrer des données transformées.

Le fichier log contient des données sur des *culverts*. Chaque *culvert*
est décrit dans un bloc comme le suivant:

.. code-block::

    ******************************START CULVERT******************************
    Culvert_branch = 'Branch_1'
    Culvert_name = 'OH_1'
    Culvert_params = concrete,0.8,18.167797243453975,0.015,85.87233511355132,199.94657475951888
    ******************************END CULVERT******************************

La première ligne marque le début du bloc de définition
d'un *culvert*.
Le nom de la *branch* à laquelle appartient le *culvert* défini est
défini sur la deuxième ligne, le nom du *culvert* sur
la troisième ligne. La quatrième ligne contient une liste
de 6 paramètres du culvert: *type*, *diameter*, *length*, *manning*,
*upstream chainage*, *upstream invert*.
La cinquième ligne marque la fin du bloc de définition.

Le fichier log peut être téléchargé `ici <https://raw.githubusercontent.com/maximlt/PythonScript/master/exercices/loganalysis/culvert_logfile.txt>`__.

Deux scripts sont à créer. Le premier s'occupera de:

* lire le fichier log
* récupérer toutes les données de chaque *culvert*
* afficher le nombre de *culverts* que contient le fichier log
* enregistrer ces données dans un fichier au format CSV 

Le deuxième script s'occupera de:

* lire le fichier CSV enregistré par le script précédent
* supprimer les données liés au paramètres *manning*
* convertir le paramètre *diameter* de *m* en *mm*
* afficher le diamètre moyen de tous les *culvert*
* afficher le diamètre moyen des *culverts* dont le type est *concrete*
* créer et enregistrer un camembert de la répartition
  des *culverts* suivant leur type
* déterminer pour chaque *culvert* son paramètre *downstream chainage*
  en fonction des paramètres *upstream chainage* et *length*
* enregistrer les données (incluant les données transformées et 
  les données ajoutées) dans un fichier au format CSV

Une solution à l'exercice est proposée `ici <https://github.com/maximlt/PythonScript/tree/master/exercices/loganalysis/solution>`__.

Ajout de texte à un fichier PDF
--------------------------------

Ce deuxième exercice consiste à ajouter du texte sur chaque page d'un fichier PDF.
Les données à rajouter sont lues depuis un fichier CSV, il s'agit d'un numéro et 
d'une description. Le package à utiliser pour effectuer l'opération sur le fichier PDF
est `PyMuPDF <https://pymupdf.readthedocs.io/en/latest/>`__.

Le script à créer devra donc:

* lire le fichier CSV pour en extraire les données,
* enregistrer un nouveau fichier PDF agrémenté du texte à rajouter.

Les données nécessaires à l'exercice proposé sont disponibles `ici <https://github.com/maximlt/PythonScript/tree/master/exercices/modifpdf>`__:

* le fichier PDF est composé de trois pages qui affichent des formes différentes (rectangle, triangle et un cercle),
* le fichier CSV contient la description de ces formes et un identifiant.

L'objectif pratique est d'ajouter en haut de chaque page l'identifiant et la description de la forme.

Une solution à l'exercice est proposée `ici <https://github.com/maximlt/PythonScript/tree/master/exercices/modifpdf/solution>`__.
