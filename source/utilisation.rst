Écriture et exécution d'un script
===================================

Le style
--------

Commenter
*********

Commenter son code est **essentiel**. Cela permettra aux personnes liront 
le code de mieux le comprendre (pour le modifier par exemple) et
cela permettra aussi à l'auteur du code de se rappeler plus rapidement des spécificités de celui-ci.
Commenter son code c'est donc **avant tout se rendre service** pour éviter de perdre du temps plus tard.

Ainsi lorsqu'on écrit un script, la première chose à faire est
de le commenter, **avant même l'écriture d'une seule ligne de vrai code**.
On pourrait rajouter au début de chaque script qu'on écrit la ``docstring`` suivante:

.. code-block:: python

    """Une courte phrase qui dit ce que le script va faire.

    Ici, on précise les choses, en détaillant la logique
    du script, et l'utilisation qu'on imagine en faire.

    Utilisation: Décrire comment utiliser le script.

    Références: On peut rajouter ici des références utiles
    (liens internet par exemple).

    Dépendances: La version de Python et les dépendances
    sur lesquelles le script va s'appuyer.
    exemple: python 3.7, pandas 0.25

    Historique:
    - nom (date): création du script
    """

PEP8
****

``PEP8`` est le guide stylistique de Python. Son application
est très largement répandue.

Appliquer ``PEP8``, c'est prendre de bonnes habitudes et 
se faciliter la lecture du code qu'on peut trouver sur internet, 
qui dans la majorité des cas suit ce guide.

Le guide ``PEP8`` est disponible `ici <https://www.python.org/dev/peps/pep-0008/>`_.

Écrire un script
-----------------

Un script Python est un simple fichier texte dont
l'extension est ``.py``. Par exemple, le fichier
``parsefile.py`` est un script Python.

Pour écrire du code dans un script Python, on peut
utiliser un éditeur de texte simple comme *Notepad*.
Des éditeurs plus évolués comme *Notepad++* 
permettent de changer la couleur du texte en fonction de ce qu'il représente.
On utilisera **Spyder** qui est un logiciel dédié
à l'écriture du code en Python.

Exécuter un script
-------------------

Depuis Spyder
*************

On peut ouvrir un script Python dans **Spyder** puis l'exécuter:

* Ligne par ligne avec la touche ``F9``,
* Une sélection spécifique (une partie d'une ligne, plusieurs lignes, etc.) avec la touche ``F9``,
* Une cellule encadrée par le symbole ``# %%`` avec la combinaison ``Ctrl + Entrée``,
* Entièrement avec la touche ``F5`` ou en cliquant sur la flèche verte.


Depuis l'Anaconda Prompt
************************

Il faut ouvrir la console **Anaconda Prompt** et s'assurer que l'on se trouve
bien dans un environnement **conda** permettant d'exécuter le script. On activera l'environnement avec:

   .. code::
  
       conda activate parser_env

La commande suivante va exécuter le code contenu dans le fichier ``parsefile.py`` avec la version de **Python**
installée dans l'environnement *parser_env*. Il faudra que les dépendances du script (**pandas** par exemple)
soient installées au préalable dans l'environnement (``conda install pandas``).

   .. code::
  
       python parsefile.py


Si le fichier contient des données d'entrée à adapter
suivant son application, on peut *hard-coder* ces données,
c'est-à-dire, on les écrit directement dans le script.

Le contenu du script pourrait ressembler à cela:

.. code-block:: python

    ####### INPUT DATA #########
    INPUTFILE = "inputfile.txt"
    ############################
    do_something(INPUTFILE)

On peut aussi passer des arguments à la commande d'exécution
du script avec, par exemple, la commande 
``python parsefile.py inputfile.txt``. Ici, ``inputfile.txt`` est un argument 
supplémentaire qui sera utilisé par le script ``parsefile.py``. On peut récupérer
ce genre d'argument directement depuis le code avec le module ``sys`` et son
attribut ``argv``. Cet attribut est une ``list``, son 
deuxième élément contiendra ``"inputfile.txt"``.

Le contenu de ce script pourrait ressembler à cela:

.. code-block:: python

    import sys

    # Lecture de l'argument passé à la ligne de commande
    inputfile = sys.argv[1]

    do_something(inputfile)

Depuis un fichier batch
************************

L'exemple ci-dessous montre comment adapter un fichier **batch** (extension en *.bat*)
pour qu'il active un environnement conda, exécute un script Python et désactive conda.

Une fois adapté (chemin vers le dossier d'installation de *Miniconda*, nom de l'environnement à activer et chemin du
script à exécuter), on peut enregistrer ce fichier **batch** et l'exécuter directement depuis la **Command Prompt** (il
n'est pas nécessaire de l'exécuter depuis l'**Anaconda Prompt**).


.. code-block:: bat

    @echo off

    rem Chemin ver le dossier racine de Miniconda
    set CONDAPATH=C:\path\to\Miniconda
    rem Nom de l'environnement à activer (e.g. gis, datascience, etc.)
    set ENVNAME=parsefile_env

    call %CONDAPATH%\Scripts\activate.bat %CONDAPATH%\envs\%ENVNAME%

    python parsefile.py

    call conda deactivate
    rem Désactive l'environnement base
    call conda deactivate