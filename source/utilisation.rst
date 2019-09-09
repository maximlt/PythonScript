Ecriture et exécution d'un script Python
========================================

Le style
--------

Commenter
*********

Commenter son code est **vraiment important**.
Il faut être concentré pour écrire du code, on doit assembler
les pièces d'un puzzle assez complexe. A ce moment-là, on a
une très bonne compréhension du code. Mais un drame se trame,
car un jour/une semaine/un mois plus tard, tout est oublié.
Commenter son code, **c'est avant tout se rendre un fier service**.

Lorsqu'on écrit un script, la première chose qu'on doit faire est
de le commenter. Avant même l'écriture d'une seule ligne de code.
Cela pourrait ressembler à ça:

.. code-block:: python

    """Une courte phrase qui dit ce que le script va faire.

    Ici, on précise les choses, en détaillant la logique
    du script, et l'utilisation qu'on imagine en faire.

    Utilisation: Décrire comment utiliser le script.

    Références: On peut rajouter ici des références utiles
    qu'on a trouvées sur internet.

    Dépendances: La version de Python et les dépendances
    qu'on imagine utiliser
    exemple: python 3.7, pandas 0.25

    Historique:
    - nom (date): création du script
    """

PEP8
****

``PEP8`` est le guide stylistique de Python. Son application
est très largement répandue.

Appliquer ``PEP8``, c'est prendre de bonnes habitudes et 
se faciliter la lecture du code qu'on peut sur internet, 
qui dans la majorité des cas suit ``PEP8``.

``PEP8`` est disponible `Link ici <https://www.python.org/dev/peps/pep-0008/>`_.

Ecrire un script
----------------

Un script Python est un simple fichier texte dont
l'extension est ``.py``. Par exemple, le fichier
``parsefile.py`` est un script Python.

Pour écrire du code dans un script Python, on peut
utiliser un éditeur de texte simple comme *Notepad*.
Des éditeurs plus évolués comme *Notepad++* 
permettent de changer la
couleur du texte en fonction de ce qu'il représente.
On utilisera ``Spyder`` qui est un logiciel dédié
à l'écriture du code en Python.

Exécuter un script
------------------

On peut exécuter un script Python depuis la **Command Prompt**.
La commande ``python parsefile.py`` va exécuter le code
contenu dans le fichier ``parsefile.py``.

Si le fichier contient des données d'entrée à adapter
suivant son application, on peut *hard-coder* ces données,
c'est-à-dire, on les écrit directement dans le script.

Le contenu du script pourrait ressembler à cela:

.. code-block:: python

    INPUTFILE = "inputfile.txt"
    do_something(INPUTFILE)
    ...

On peut aussi passer des arguments à la commande d'exécution
du script avec, par exemple, la commande 
``python parsefile.py inputfile.txt``. On peut récupérer
les arguments passés de cette manière, ici ``inputfile.txt``
directement depuis le code avec le module ``sys`` et son
attribut ``argv``. Cet attribut est une ``list``, son 
deuxième élément contient ``"inputfile.txt"``.

Le contenu de ce script pourrait ressembler à cela:

.. code-block:: python

    import sys
    inputfile = sys.argv[1]
    do_something(inputfile)
    ...
