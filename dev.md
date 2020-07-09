# Construction du tutoriel

## Conversion des notebooks en scripts python

Les notebooks servent à la création du site. Les scripts peuvent être utilisés directement par Spyder.
Le package `Jupytext` permet d'effectuer la conversion avec la commande:

``jupytext --to py:percent --opt comment_magics=false file.ipynb``

