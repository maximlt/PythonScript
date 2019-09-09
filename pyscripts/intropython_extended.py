# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     comment_magics: false
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.2'
#       jupytext_version: 1.2.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Introduction pas à pas de Python [version étendue]

# %% [markdown]
# Ce notebook constitue une **rapide introduction à Python**. Le langage est découvert en exécutant un grand nombre de simples et courtes lignes de code. L'objectif est d'entrapercevoir la manière dont Python fonctionne afin d'éviter de tomber dans les pièges classiques des débutants.
#
# Cette approche est inspirée des tutoriels [Python by immersion](https://www.youtube.com/watch?v=F6yLRM3b0q8) et [Python Epiphanies](https://www.youtube.com/watch?v=-kqZtZj4Ky0) créés par Stuart Williams.

# %% [markdown]
# ## Indentation

# %% [markdown]
# ---
#
# *Tout est dans le style*
#
# ---

# %% [markdown]
# Python a été conçu de manière à être facile à lire, partant du principe qu'on passe plus de temps à lire du code qu'à en écrire. Cela se matérialise par l'importance de l'**indentation** (décalage d'une ligne de code vers la droite). L'indentation du code détermine en partie sa structure. Dans l'exemple ci-dessous, les deux instructions `print` sont situées au même niveau d'indentation.

# %%
print("Hey")
print("you")

# %% [markdown]
# Le code est exécuté normalement. La deuxième instruction du code suivant a été décalée de deux espaces, le code ne peut tout simplement plus être exécuté car cette structure n'a aucun sens pour Python.

# %%
print("Hey")
  print("you")

# %% [markdown]
# L'utilité de l'indentation est plus évidente dans le cas de blocs logiques, tel qu'un bloc `for`. Le code ci-dessous s'exécute correctement.

# %%
for i in [1, 2, 3]:
    print(i)  # L'indentation est de 4 espaces en général.

# %% [markdown]
# Alors que le code ci-dessous ne peut pas être exécuté, les instructions sous la ligne `for` n'étant pas indentées. Comme on peut le voir, c'est le code du dessus qui est le plus facile à lire, l'indentation nous aide à comprendre la structure logique du code.

# %%
for i in [1, 2, 3]:
print(i)

# %% [markdown]
# Afin de définir les boucles et autres structures de contrôle, d'autres langages utilisent des symbôles (`{}`, `()`). En choisissant d'utiliser l'indentation au lieu de symboles, Python a faix le choix du code **épuré**.

# %% [markdown]
# ## Commentaires et `pass`

# %% [markdown]
# ---
#
# *Fainéant*
#
# ---

# %% [markdown]
# Les commentaires sont des lignes qui débutent par un signe `#`. Ces lignes-là sont ignorées par l'interpréteur.

# %%
# Ceci est un commentaire.

# %%
# On
# peut
# les
# enchaîner

# %%
###### Ceci aussi est un commentaire.

# %% [markdown]
# On peut rajouter un commentaire à la suite d'un code valide (séparé de deux espaces par convention).

# %%
3.14  # Ceci est aussi un commentaire.

# %% [markdown]
# Le *keyword* **pass** fait comme son nom l'indique, il passe son tour.

# %%
pass

# %% [markdown]
# ## Objets

# %% [markdown]
# ---
#
# *Tout est un objet!*
#
# ---

# %% [markdown]
# Exécuter les instructions simples ci-dessous peut faire penser que Python ne fait rien de plus qu'une simple calculette.

# %%
3.4

# %%
3.4 + 4

# %% [markdown]
# Pourtant, beaucoup de choses se passent!

# %%
dir(3.4)

# %% [markdown]
# La **fonction** `dir` retourne une liste de tous les **attributs** d'un **objet**. La liste ci-dessus montre donc tous les attributs de l'objet `3.4`. Les derniers attributs affichés, dont `is_integer`, nous indiquent que Python a compris que ``3.4`` est un nombre. On peut le vérifier en inspectant la valeur de l'attribut `__class__`. **Pour accéder à la valeur d'un attribut, on rajout un point `.` après l'objet suivi du nom de l'attribut.**

# %%
3.4.__class__

# %% [markdown]
# `float` est un type d'objet qui représente les nombres réels.  Mais plutôt que de vérifier le type d'un objet en accédant à son attribut *\_\_class__*,  on peut utiliser la fonction `type`. Cette fonction, comme `dir`, fait partie des fonctions dites **built-in** car faisant parties intégrantes de Python (il n'y a pas besoin  d'importer quoi que ce soit pour les appeler). On va voir plusieurs de ces fonctions dans la suite du notebook.

# %%
type(3.4)

# %% [markdown]
# On a donc vu que lorsqu'on exécute `3.4`, Python ne fait pas juste qu'afficher ce nombre mais l'interprète comme un objet de type `float` doté de nombreux attributs. Que se passe-t-il alors lorsqu'on exécute `3.4 + 4`?

# %%
3.4.__add__(4)

# %% [markdown]
# L'addition que nous avons écrite est en fait exécutée par l'instruction ci-dessus. Python voit que nous avons écrit un `+` après `3.4`, il cherche alors l'attribut **dunder** (racourci de *d*ouble *under*score donné aux **attributs** qui débutent et terminent par `__`) `__add__` dans la liste des attributs de ``3.4``. L'attribut `__add__` des `floats` est en fait une **méthode** qui est capable de faire une action, dans ce cas-là, une addition. Lorsque Python trouve l'attribut `__add__` de `3.4`, il l'appelle avec l'**argument** `4`. La valeur retournée est le résultat de l'addition.

# %% [markdown]
# Python n'est donc évidemment pas qu'une simple calculatrice. Lorsqu'il évalue les **expressions** qu'on lui donne, il crée des objets dotés d'un type et d'attributs. Ces attributs sont soit équivalent à des propriétés, comme `__class__`, soit des méthodes, comme `__add__`. **Cette mécanique est présente partout dans le langage, celui-ci travaille en effet beaucoup pour nous**. Il faut aussi noter que Python s'occupe d'allouer et libérer la mémoire à notre place.

# %%
type(3.4.__add__)

# %% [markdown]
# Chaque objet créé a sa propre **identité** définie comme son adresse physique dans la mémoire.

# %%
id(3.4)

# %%
id(3.4)

# %%
id(4)

# %% [markdown]
# ``dir`` et ``id`` sont des fonctions **qu'on n'utilise jamais dans un script mais qui sont très utiles pour apprendre Python et inspecter des objets**.

# %%
type(dir)

# %%
type(id)

# %% [markdown]
# Une fonction est aussi un objet (tout est un objet!) avec ses propres attributs, un type et une identité.

# %%
dir(dir)

# %%
id(dir)

# %%
id(dir)

# %% [markdown]
# ## Erreurs

# %% [markdown]
# ---
#
# *Antifragilité*
#
# ---

# %% [markdown]
# Lorsqu'on écrit du code en Python et qu'on l'exécute pour la première fois, **il est habituel de voir un message d'erreur apparaître**. Ces erreurs nous indiquent ce qui ne fonctionne pas dans le code, et nous oriente pour résoudre le bug qui a causé l'erreur. Python dispose d'un grand nombre de genres d'erreur, à force de les déclencher on s'habitue à les reconnaître et on comprend de plus en plus rapidement d'où vient le problème.

# %%
type(1)
 type(2)  # L'espace déclenche l'erreur

# %%
1
3 +)°^ 3  # Cette suite de symboles n'a aucun sens

# %% [markdown]
# Les erreurs `IntendationError` et `SyntaxError` nous indique que le code n'a pas été écrit correctement. L'interpréteur analyse tout le code qu'on a écrit, s'il détecte ce genre d'erreur, il nous l'indique et **n'exécute aucune ligne de code**. Toutes (?) les autres erreurs qu'on peut avoir surviennent **pendant l'exécution du code** (runtime).

# %% [markdown]
# ## `print` et `help`

# %% [markdown]
# ---
#
# *Pour y voir plus clair*
#
# ---

# %% [markdown]
# ``print`` affiche les objets passés à la fonction. ``help`` affiche l'aide d'un objet.

# %%
print(3.4, 4, 5, 1, 0)

# %%
help(print)

# %%
dir(print)

# %%
print.__doc__

# %% [markdown]
# `print` est un objet et a donc des attributs. Son attribut `__doc__` est sa **docstring** qui est un texte décrivant la fonction. C'est ce texte que la fonction `help` affiche.
#
# On va beaucoup utiliser la fonction `print`. Le début de sa définition est `print(value, ..., sep=' ')`:
#
# * `value, ...`: `print` accepte un nombre illimité d'arguments séparés par une virgule

# %%
print(3.4, 4, 6, 103, 3030, 0, 0)

# %% [markdown]
# * `sep=' '`: l'espacement par défaut entre deux valeurs affichées par `print` est un espace, on peut le changer en spécifiant le paramètre `sep`

# %%
print(3.4, 4, 6, 103, 3030, 0, 0, sep="  :)   ")

# %%
# "\n" est interprété comme un retour à la ligne
print(3.4, 4, 6, 103, 3030, 0, 0, sep="\n")

# %%
# "\t" est interprété comme une tabulation
print(3.4, 4, 6, 103, 3030, 0, 0, sep="\t")

# %% [markdown]
# ## Keywords

# %% [markdown]
# ---
#
# *Un peu de liant*
#
# ---

# %% [markdown]
# Avec l'indentation, les **keywords** structurent le langage. On utilisera principalement les suivants:
#
# * Le vide: `None`
# * Booléens: `True`, `False`
# * Opérations booléennes: `and`, `or`, `not`
# * Appartenance: `in`, `not in`
# * Identification: `is`, `is not`
# * Boucles: `for`, `while` `break`, `continue`, `pass`, 
# * Conditions: `if`, `elif`, `else`
# * Fonctions: `def`, `return`
# * Import: `import`, `from`, `as`
# * Déférencement: `del`
# * Pas d'action: `pass`

# %%
help("keywords")

# %% [markdown]
# Les **keywords** sont des **mots réservés**, aucun objet ne peut avoir un nom qui fait partie des **keywords**.

# %%
True = 2

# %%
true = 2  # On peut faire ça, mais c'est maladroit!

# %%
and = 3

# %%
AND = 3  # Toujours autant maladroit!

# %%
help(for)

# %%
help("for")

# %% [markdown]
# A part `True`, `False` et `None`, les **keywords** ne sont pas des objets.

# %%
type(and)

# %%
print(type(True), type(False), type(None))

# %% [markdown]
# ## Opérateurs principaux

# %% [markdown]
# ---
#
# *Pas que pour les maths!*
#
# ---

# %%
3.4 + 4

# %%
3.4 - 4

# %%
3.4 * 4

# %%
3.4 / 4

# %%
11 // 4

# %%
(11).__floordiv__(4)

# %%
11 % 4

# %%
(11 // 4) * 4 + (11 % 4)

# %%
11 // 4 * 4 + 11 % 4  # Moins facile à lire

# %%
3.4 > 4

# %%
3.4 < 4

# %%
3.4 <= 4

# %%
3.4 >= 4

# %%
2 < 5 < 10

# %%
3 > 2 >= 10

# %%
3.4 == 4

# %%
3.4.__eq__(4)

# %%
3.4 != 4

# %%
4 == 4

# %% [markdown]
# Les symboles *opérateurs* ne sont pas des objets.

# %%
type(==)

# %% [markdown]
# ## Nommer

# %% [markdown]
# ---
#
# *Poser des post-its par-ci, par-là*
#
# ---

# %% [markdown]
# Jusqu'à présent les objets qui ont été utilisés sont supprimés aussitôt générés par Python. On peut les garder à notre disposition en leur assignant un nom.

# %%
height = 1.73

# %%
height

# %%
type(height)

# %%
id(height)

# %%
id(height)

# %%
print(height, height, height)

# %% [markdown]
# Regardez bien les trois instructions ci-dessous, **quelle est la valeur finale de `x`**?

# %%
x = 2
y = x
y = 4

# %%
print(x, y)

# %% [markdown]
# On aurait pu croire que `x` valait `4` à la fin des trois instructions, mais non. **Les noms en Python sont juste des références aux objets**, on peut les comparer à des **post-its**.

# %%
x = 2
# L'objet 2 est créé, un post-it avec inscrit *x* lui est aposé.
print("x =", x, " / id(x):", id(x))
y = x
# Un second post-it est aposé sur l'objet 2, il y est inscrit *y*.
print("x =", x, " / id(x):", id(x), "  ---  y =", y, " / id(y):", id(y))
# Aucun objet n'est créé lors de cette instruction.
y = 4
# L'objet 4 est créé, comme un nom ne peut référé qu'à un seul objet
# le post-it *y* qui était sur l'objet 2 est supprimé et un nouveau
# post-it *y* est aposé sur l'objet 4.
print("x =", x, " / id(x):", id(x), "  ---  y =", y, " / id(y):", id(y))

# %% [markdown]
# Une fois que des références aux objets ont été créées, celles-ci sont rajoutées au **namespace**. On peut en voir le contenu avec la fonction `dir`.

# %%
print(dir())

# %% [markdown]
# Dans une console IPython ou dans un notebook, le **namespace** est occupé par beaucoup de références qui ne nous intéressent pas. Les commandes magiques `%who` et `whos` permettent de voir uniquement celles que nous avons créées nous-mêmes.

# %%
%who

# %%
%whos

# %% [markdown]
# Ainsi, lorsqu'on l'on fait référence à un objet par un de ses noms, Python cherche dans le **namespace** la référence de cet objet et utilise la donnée qui lui est associée.

# %%
height

# %%
poids

# %% [markdown]
# Comme `poids` n'est pas une référence du **namespace** (on peut aussi dire que la variable `poids` n'a pas encore été définie), l'interpréteur retourne une **erreur**.
#
# On peut déréférencer un élément du **namespace** avec une **instruction** utilisant le *keyword* `del`.

# %%
# On enlève le post-it *height* de l'objet 1.73,
# celui-ci n'est plus accessible à la suite de ça.
del height

# %%
%who

# %%
del height

# %%
height

# %% [markdown]
# On peut déférencer tous les éléments du **namespace** avec la commande magique `%reset -f`.

# %%
%reset -f

# %%
%whos

# %% [markdown]
# ## Importer

# %% [markdown]
# ---
#
# *Batteries included*
#
# ---

# %% [markdown]
# Nous avons pour l'instant vu que nous avions à disposition des fonctions **built-in**, des **keywords** et des **opérateurs**. Un mécanisme permet d'**importer des objets supplémentaires dans le code**, comme des fonctions.

# %%
import math

# %% [markdown]
# `math` est un **module** de la **standard library**. La **standard library** est une grande collection de modules livrés avec Python, c'est pourquoi on associe souvent l'expression *Batteries Included* au langage.

# %%
%whos

# %% [markdown]
# `math` est le module dédié aux opérations mathématiques. En exécutant `import math`, on a rajouté au *namespace* le nom `math`, celui-ci faisant référence à un objet de type `module`.

# %%
type(math)

# %%
id(math)

# %%
print(dir(math))

# %% [markdown]
# On peut voir que le module contient les attributs `sqrt` (racine carrée) et `pi`. On accède à ces attributs en rajoutant un `.` après `math`.

# %%
math.sqrt

# %%
math.pi

# %%
type(math.sqrt)

# %%
type(math.pi)

# %%
math.sqrt(math.pi)

# %% [markdown]
# On peut importer un module et les objets qu'il contient de plusieurs manières:
#
# * `from math import *` importe tout le contenu du module `math`. **Cette méthode n'est pas recommandée** car elle vient rajouter beaucoup de références au *namespace*.

# %%
%reset -f

# %%
from math import *

# %%
%who

# %%
sqrt(pi)

# %% [markdown]
# * `import math as m` importe le module `math` avec pour référence `m` et non `math`. Cette méthode peut être utilisé lorsque le nom du module est très long, ou si ce nom va être répété à de très nombreuses reprises. Trois examples classiques étant `import numpy as np`, `import pandas as pd`, `import matplotlib.pyplot as plt`.

# %%
%reset -f

# %%
import math as m

# %%
math

# %%
m

# %%
%whos

# %%
m.sqrt(m.pi)

# %% [markdown]
# * `from math import sqrt, pi` importe seulement les objets `sqrt` et `pi`.

# %%
%reset -f

# %%
from math import sqrt, pi

# %%
%whos

# %%
sqrt(pi)

# %% [markdown]
# * `from math import sqrt as racinecarree` importe directement la fonction `sqrt` du module `math` sous la référence `racinecarree`.

# %%
%reset -f

# %%
from math import sqrt as racinecarree

# %%
%whos

# %%
racinecarree(4)

# %%
sqrt(4)

# %% [markdown]
# **Des méthodes d'import montrées ci-dessus, c'est la première, `import math`, qui doit être préférée.** Elle permet en effet de savoir depuis quel module proviennent les fonctions qu'on utilise.

# %%
%reset -f

# %% [markdown]
# ## Modules et packages
#

# %% [markdown]
# ---
#
# *Batteries included in batteries*
#
# ---

# %% [markdown]
# Les **modules** sont matérialisés par des **fichiers textes dont l'extension est ``.py``**. Lorsqu'on importe un module, **le code qu'il contient est exécuté**. Les objets qui sont créés dans ce module sont donc accessibles.

# %%
%%writefile dummymodule.py
"""Un tout petit module."""
print("hello world")
x = 2

# %%
import dummymodule

# %%
dummymodule.x

# %% [markdown]
# **!!! Attention !!!** **Importer un module déjà importé ne réexécute pas son code.**

# %%
import dummymodule

# %%
dummymodule.x

# %% [markdown]
# **Si on modifie le code d'un module** qu'on utilise pendant qu'on écrit un script, **il faut penser à forcer son import**. On peut utiliser le module ``importlib`` pour importer à chaque fois le module modifié.

# %%
import importlib
importlib.reload(dummymodule)

# %% [markdown]
# Les modules sont aussi des objets (*tout est un objet*).

# %%
type(dummymodule)

# %%
dir(dummymodule)

# %%
dummymodule.__name__

# %%
dummymodule.__file__

# %%
dummymodule.__doc__

# %%
help(dummymodule)

# %%
dummymodule?

# %% [markdown]
# Lorsqu'il tente d'importer quelque chose, Python cherche dans une liste de dossier qu'on retrouve dans la référence `sys.path`. Cette liste contient **le dossier courant**.

# %%
import sys
sys.path

# %% [markdown]
# Les modules de la *standard library* écrits en Python (il y a aussi des modules écrits en `C`) sont visibles sur [GitHub](https://github.com/python/cpython/tree/3.7/Lib). Dans ce dossier on trouve aussi des sous-dossiers qui contiennent des fichiers ``.py`` et un fichier ``__init__.py``. Ces dossiers-là sont des **packages** qu'on peut aussi importer.

# %%
import email

# %%
type(email)

# %%
dir(email)

# %%
email.__package__

# %%
email.__path__

# %%
email.__file__

# %%
email.__doc__

# %%
help(email)

# %%
import email.message

# %%
type(email.message)

# %%
email.message.__file__

# %%
email.message.__package__

# %%
import email.mime

# %%
email.mime.__package__

# %%
dir(email.mime)

# %%
help(email.mime)

# %%
from email.mime import audio

# %%
type(audio)

# %%
audio.__file__

# %% [markdown]
# Voici une **très courte liste** de modules utiles.

# %%
import sys
sys.executable

# %%
sys.version

# %%
import os
os.getcwd()

# %%
import time
t1 = time.time()
time.sleep(2)
t2 = time.time()
print(t2 - t1)

# %%
import datetime
guess = datetime.datetime(2019, 9, 10, 10, 5, 14)
now = datetime.datetime.now()
diff = now - guess
print("Je me suis trompé de", diff.seconds, "secondes.")

# %%
import random
random.random()

# %%
random.randint(10, 20)

# %%
random.choice(["a", "b", "c"])

# %%
random.sample([1, 2, 3, 4], 3)

# %%
random.gauss(10, 3)

# %%
import pathlib
current_directory = pathlib.Path.cwd()
current_directory

# %%
list(current_directory.glob("*"))

# %%
import collections
collections.Counter("aaabbbbbbbbbbbbbcccddddee").most_common()

# %%
%reset -f
!del /f dummymodule.py

# %% [markdown]
# ## Conditions `if` et booléens

# %% [markdown]
# ---
#
# *Avec des si*
#
# ---

# %% [markdown]
# Le bloc sous une instruction ``if`` est exécuté entièrement si la condition (expression) qui suit le ``if`` est évaluée comme *vraie*.

# %%
if True:
    print("Executed")

# %%
if False:
    print("Not executed")

# %%
diameter = 2
if diameter > 1:
    print(diameter)

# %% [markdown]
# On peut rajouter d'autres conditions avec les *keywords* ``elif`` et ``else``.

# %%
age = 150
if age < 18:
    print("Sorry you're not allowed to drive.")
elif 18 <= age < 80:
    print("Let's drive!")
elif 80 <= age < 122:
    print("Please please please strop driving please!")
else:
    print("Is that you Jeanne?")

# %% [markdown]
# On peut assigner le résultat d'un comparaison à une référence et on peut combiner plusieurs comparaisons avec les *keywords* `and` et `or`?

# %%
age1 = 10
age2 = 54
condition1 = 18 <= age1 < 80
condition2 = 18 <= age2 < 80
condition1 and condition2

# %%
True and True

# %%
True or True

# %%
False and False

# %%
False or False

# %%
False and True

# %%
True and False

# %%
False or True

# %%
True or False

# %%
print(type(condition1), type(condition2))

# %% [markdown]
# `True` et `False` sont des **booléens**. Dans les versions précédentes, `1` était utilisé pour représenter ce qui était vrai, et `0` pour ce qui était faux. On hérite de ce comportement aujourd'hui.

# %%
True + 3

# %%
False + False

# %% [markdown]
# Tous les objets de Python sont en fait soit vrai ou faux. On peut vérifier s'ils sont **truthy** ou **falsy** avec la fonction `bool`.

# %%
bool(3.14)

# %%
if 3.14:
    print("3.14")

# %%
bool(0)

# %%
if 0:
    print("0")

# %%
bool(1)

# %%
if 1:
    print("1")

# %%
bool(print)

# %%
if print:
    print("Never do that please!")

# %%
bool(None)

# %%
if not None:
    print("Pas vide")

# %%
%reset -f

# %% [markdown]
# ## Texte

# %% [markdown]
# ---
#
# *Du blabla*
#
# ---

# %% [markdown]
# Le texte est représenté par des objets de type `string`. On encadre le texte des symboles `"` ou `'` ou `"""` ou `'''` pour créer un objet `string`.

# %%
"Bob"

# %%
'Bob'

# %%
"""Bob"""

# %%
'''Bob'''

# %%
type("Bob")

# %%
print("'")

# %%
print('"')

# %% [markdown]
# On peut les **additionner** et les **démultiplitier**.

# %%
"Bob" + "Bill"

# %%
"Bob" * 3

# %%
3 * "Bob"

# %%
"Bob" - "Bill"

# %%
"Bob" / 3

# %% [markdown]
# Il est possible de créer une `string` vide.

# %%
""

# %%
"Bob" + "" + "Bill"

# %% [markdown]
# Le **caractère backslash `\` déclenche un comportement spécial**: l'interpréteur regarde le caractère qui suit et voit si la combinaison des deux caractères forme ou non un caractère spécial, si oui, celui-ci est représenté.

# %%
# \n --> Retour à la ligne
# \t --> Tabulation

print("Bob\tBill\nBill\tBob")

# %% [markdown]
# Le caractère `\` a donc un effet particulier. Cela rend plus difficile la représentation d'un chemin vers un dossier ou un fichier sous Windows. On annule l'effet particulier de `\` en rajoutant le préfixe `r` (pour **r**aw) devant le premier guillemet de la `string`.

# %%
print(r"user\me\names.txt")  # OK

# %%
print("user\me\names.txt")  # not OK

# %% [markdown]
# On peut créer une `string` sur plusieurs lignes:
# * en insérant des `\n` dans le texte pour représenter les sauts de ligne
# * en créant l'objet `string` directement avec trois guillemets `"""`
#
# La deuxième option rajoute automatiquement des `\n` à chaque saut de ligne.

# %%
print("bla bla\nbla bla\nbla bla")

# %%
"""bla bla
bla bla
bla bla"""

# %%
print("""bla bla
bla bla
bla bla""")

# %% [markdown]
# Si on doit écrire un long texte dans le code, on peut couper la définition du texte avec un `\` ajouté à la fin de chaque ligne.

# %%
"Ceci est un long texte. Cela peut être un message \
d'erreur. Lorsqu'un si long texte est défini, il est utile de \
le couper avec un backslash à la fin de chaque ligne \
pour éviter d'avoir une instruction qui aille \
à l'encontre de PEP8."

# %% [markdown]
# On peut vérifier si deux `strings` sont égales avec l'*opérateur* égalité `==`. Pour vérifier si une partie d'une `string` se trouve dans une autre, on utilise le *keyword* `in`.

# %%
"Bob" == "Bill"

# %%
"Bob".__eq__("Bill")

# %%
"Bob" != "Bill"

# %%
"Bob" == 'Bob' == """Bob"""

# %%
"Bill" in "Bob and Bill"

# %%
"Bob and Bill".__contains__("Bill")

# %%
"John" in "Bob and Bill"

# %%
"Bill" not in "Bob and Bill"

# %% [markdown]
# Les `strings` possèdent beaucoup de méthodes pour les analyser et transformer. Lorsqu'une méthode a pour objectif de transformer une `string` elle retourne un nouvel objet `string` qui est version transformée de la `string` initiale. Elles ne le modifient pas directement l'objet initial. En effet, **les `strings` sont des objets immutables**.

# %%
name = "bob"
print(dir(name))

# %%
name.upper()

# %%
name

# %%
name.title()

# %%
name.replace("o", "a")

# %%
txt = "   espaces avant et espaces après      "
txt.strip()

# %% [markdown]
# `strip` enlève par défaut les espaces au début et à la fin de la `string`. Les espaces comprennent les sauts de ligne et les tabulations.

# %%
import string
string.whitespace

# %%
txt.rstrip()

# %%
txt.lstrip()

# %%
sentence = "quel beau temps"
words = sentence.split()
words

# %%
help(str.split)

# %%
sentence.split("l")

# %%
" ".join(words) 

# %%
help(str.join)

# %% [markdown]
# On peut **enchaîner les méthodes** tant qu'on **fait attention à ce que la méthode qui suit accepte est bien une méthode de l'objet retourné par la méthode qui précède**. Dans l'exemple ci-dessous, la méthode `strip` est bien un méthode de l'objet `sentence` qui est de type `string`, elle retourne un objet `string` qui possède bien une méthode `replace`, celle-ci retourne un nouvel objet `string` qui possède bien une méthode `split`, celle-ci retourne finalement une liste.

# %%
modified_sentence = sentence.strip("qs").replace("e", "i").split()
modified_sentence

# %%
%reset -f

# %% [markdown]
# ## F-String

# %% [markdown]
# ---
#
# *Du joli blabla*
#
# ---

# %% [markdown]
# Les `f-strings` sont des objets de type `string` qu'on peut formater.  Il faut rajouter un préfixe `f` devant le premier guillemet, puis ensuite, à l'intérieur, il faut entourer de symboles `{}` les expressions qu'on souhaite formater afin qu'elles soient directement évaluées par Python, qui construit notre objet `string`.

# %%
age = 28
f"J'ai {age} ans"

# %%
type(age)

# %%
"J'ai " + age + " ans"

# %%
age = 28
limite_d_age = 25
if age > limite_d_age:
    print(
        f"Tu as {age} ans, la limite d'âge étant à {limite_d_age}, tu"
        f" as donc {age - limite_d_age} ans de plus que la limite. Tout"
        f" va maintenant être plus cher pour toi!"
    )

# %% [markdown]
# Cette manière de formater les ``strings`` est assez récente (Python 3.6) et est **vraiment pratique et facile à utiliser**. Il existe deux autres manières de formater des `strings` qu'on retrouve encore souvent sur internet.

# %%
"J'ai %s ans" % (age) 

# %%
"J'ai {} ans".format(age)

# %%
%reset -f

# %% [markdown]
# ## Convertir `float`, `int` et `str`

# %% [markdown]
# ---
#
# *Nombre <---> Texte <---> Nombre*
#
# ---

# %% [markdown]
# Les fonctions `int`, `float` et `str` tentent de convertir les objets qu'on leur donne. Elles **retournent une erreur `ValueError` si elles échouent**, et l'objet converti si elles réussissent.

# %%
int(3.7)

# %%
float(4)

# %%
str(3)

# %%
int("Bob")

# %%
x = "3"
print(type(x))
x = int(x)
print(type(x))

# %%
"Bob" + 3

# %%
"Bob " + str(3)

# %%
# print convertit automatiquement les objets en string.
print("Bob", 3)

# %%
%reset -f

# %% [markdown]
# ## Indexing et Slicing

# %% [markdown]
# ---
#
# *A piece of cake*
#
# ---

# %% [markdown]
# Certains objets comme les objets de type `string` sont des **séquences**. On peut obtenir n'importe quel item de l'objet grâce à son index numérique (**indexing**), on peut aussi obtenir directement plusieurs items (**slicing**). **Le premier item d'une séquence a toujours l'index 0 en Python (0-based)**.

# %%
txt = "Bill"

# %%
txt[0]

# %%
txt.__getitem__(0)

# %%
txt[1]

# %%
txt[2]

# %%
txt[3]

# %%
txt[4]

# %%
txt[-1]

# %%
txt[-2]

# %%
txt[-3]

# %%
txt[-4]

# %%
txt[-5]

# %% [markdown]
# **On peut connaître le nombre d'items d'une séquence avec la fonction `len`.**

# %%
help(len)

# %% [markdown]
# Lorsqu'on passe un objet `string` à la fonction `len`, on obtient le nombre de caractères de l'objet.

# %%
len(txt)

# %%
txt.__len__()

# %%
len("")

# %%
len(" ")

# %% [markdown]
# Attention au comportement spécial du backslash `\`.

# %%
len("\t")

# %%
len("\n")

# %%
len("\t")

# %%
len(r"\n")

# %%
len("Bob and Bill")

# %%
len(3.4)

# %% [markdown]
# On ne peut pas modifier un item d'une `string` à partir de son index. En fait, il est simplement **impossible** de modifier un objet `string`, il faut forcément en créer un nouveau. Un objet qui ne peut pas être modifié est dit **immutable**.

# %%
txt[0] = "A"

# %% [markdown]
# Pour obtenir plusieurs caractères d'un objet `string`, on utilise la syntaxe `[start:stop:step]` où `start` et `stop` sont des index, et `step` l'écart entre deux caractères. Par défaut, `start` est le premier index (`[0]`), `stop` est le dernier index, et `step` est égal à 1. L'élément à **l'index `start` est inclus** dans l'objet `string` retourné, l'élément à **l'index `stop` est exclus**.

# %%
numbers = "013456789"
numbers[3::]

# %%
numbers[3:]

# %%
numbers[-1:]

# %%
numbers[50::]

# %%
numbers[:8]

# %%
numbers[3:8]

# %%
numbers[3:4]

# %%
numbers[3:3]

# %%
numbers[3:50]

# %%
numbers[::1]

# %%
numbers[::]

# %%
numbers[::2]

# %%
numbers[::100]

# %%
numbers[::-1]

# %%
numbers[::-2]

# %%
numbers[3:8:3]

# %%
numbers[3:8:-1]

# %%
numbers[8:3]

# %%
numbers[8:3:-1]

# %%
numbers[:3:-1]

# %%
numbers[-3:-8:-1]

# %%
numbers.__getitem__(slice(-3, -8, -1))

# %%
%reset -f

# %% [markdown]
# ## Listes et Tuples

# %% [markdown]
# ---
#
# *Maîtres de l'ordre*
#
# ---

# %% [markdown]
# Les objets de type `list` et `tuple` sont des **containers**. Ces deux types d'objet sont, comme les objets de type `string`, des **séquences**. Ils peuvent contenir **n'importe quel type d'objet**.
#
# Les `lists` et les `tuples` sont **très pratiques et utilisés partout** dans le langage Python.

# %%
shopping = ["banana", "beer", "chocolate", "tomato", "salad"]

# %%
type(shopping)

# %%
print(dir(list))

# %% [markdown]
# L'objet retourné par la fonction `dir` est une `list`.

# %%
type(dir(list))

# %% [markdown]
# On peut accéder à chaque item d'une `list` par son index numérique.

# %%
shopping[0]

# %%
shopping.__getitem__(0)

# %% [markdown]
# L'index `-1` est un raccourci pour indiquer le **dernier item**. `-2` indique l'avant-dernier item, etc.

# %%
shopping[-1]

# %%
shopping[1:4:2]

# %% [markdown]
# La syntaxe `::-1` permet d'inverser la `list` originale.

# %%
shopping[::-1]

# %%
len(shopping)

# %%
len([])

# %% [markdown]
# Alors qu'on définit une `list` en entourant ses items de `[]`, on définit un tuple en entourant ses items de `()`.

# %%
shopping = ("banana", "beer", "chocolate", "tomato", "salad")

# %%
type(shopping)

# %% [markdown]
# On accède aux items d'un `tuple` comme on accède aux items d'une `list`.

# %%
shopping[0]

# %%
shopping[-1]

# %%
shopping[1:4:2]

# %%
shopping[::-1]

# %%
shopping(mess)

# %%
len(())

# %% [markdown]
# Une `list` ou dans un `tuple` peuvent faire référence à **n'importe quel type d'objet**.

# %%
import math
big_mess = [2, 2.33, "string", print, math, ["Bob", "Bill"]]
big_mess

# %%
import math
big_mess = (2, 2.33, "string", print, math, ["Bob", "Bill"])
big_mess

# %% [markdown]
# **Les `lists` et les `tuples` ne contiennent aucun objet, ils contiennent en fait des références à d'autres objets.**

# %%
pi = 3.14

# %%
l = [pi]

# %%
print(f"""\
{'ID de l:':15}{id(l)}
{'ID de pi:':15}{id(pi)}
{'ID de l[0]:':15}{id(l[0])}
""")

# %% [markdown]
# Comme les `strings`, les `tuples` sont des **immutables**.

# %%
ages[0] = 55

# %% [markdown]
# Au contraire, les `lists` sont des **mutables**. Il est donc autorisé de changer les éléments qu'elles contiennent, d'en supprimer ou d'en rajouter.

# %%
shopping = ["banana", "beer", "chocolate", "tomato", "salad"]
print(id(shopping), shopping)

# %%
shopping[0] = "apple"
print(id(shopping), shopping)

# %%
shopping.append("cucumber")
print(id(shopping), shopping)

# %%
shopping.append("pasta")
print(id(shopping), shopping)

# %%
del shopping[-1]
print(id(shopping), shopping)

# %%
del shopping[-2:]
print(id(shopping), shopping)

# %%
shopping.extend(["egg", "bread", "jam"])
print(id(shopping), shopping)

# %%
shopping.insert(0, "salt")
print(id(shopping), shopping)

# %% [markdown]
# Les `lists` et les `tuples` supportent les opérateurs `in`, `not in`, `==`, `!=`, `+` et `*`.

# %%
"egg" in shopping

# %%
"rice" not in shopping

# %%
shopping == ["egg", "chocolate"]

# %%
shopping != ["egg", "chocolate"]

# %%
["egg"] == ("egg")

# %%
["egg", "chocolate"][0] == ("egg", "chocolate")[0]

# %%
["Bob"] == ["Bill"]

# %%
[[["Bob"]]]

# %%
[[["Bob"]]][0][0][0]

# %%
[[["Bob"]]] == [[["Bill"]]]

# %%
["Bob"] + ["Bill"]

# %%
("Bob",) + ("Bill",)

# %%
["Bob", "Bill"] * 3

# %%
("Bob", "Bill") * 3

# %%
[] * 3

# %%
[[]] * 3

# %% [markdown]
# On peut transformer les `lists` en `tuples` et vice versa avec les fonctions `tuple` et `list`.

# %%
l = ["Bob", "Bill"]
t = tuple(l)
print(type(t), t)

# %%
t = ["Bob", "Bill"]
l = list(t)
print(type(l), l)

# %% [markdown]
# Les méthodes `count` et `index` peuvent être utiles. Elles sont communes aux `lists` et `tuples`.

# %%
[1, 2, 3, 3, 3, 4, 5].count(3)

# %%
[1, 2, 3, 3, 3, 4, 5].count(6)

# %%
[1, 2, 3, 3, 3, 4, 5].index(4)

# %%
[1, 2, 3, 3, 3, 4, 5].index(3)

# %%
[1, 2, 3, 3, 3, 4, 5].index(6)

# %% [markdown]
# La fonction `sorted` permet de trier une `list` ou un `tuple`. Elle retourne un nouvel objet qui est une `list`.

# %%
sorted([3, 1, 2])

# %% [markdown]
# Par défaut les items sont retournés dans l'ordre ascendant, on inverser l'ordre avec le paramètre `reverse`. 

# %%
sorted((3, 1, 2), reverse=True)

# %% [markdown]
# On peut trier des `strings` mais il faut faire attention à aux différences entre minuscules, capitales et nombres.

# %%
sorted(["Donald", "Bob", "Bill"])

# %%
"D" > "B"

# %%
"D" > "d"

# %%
"z" > "A"

# %%
"Z" > "0"

# %% [markdown]
# Le paramètre `key` accepte comme argument une fonction, cette fonction est appliquée à chaque item de l'objet initial et le tri est effectué sur la base des résultats de la fonction. Dans l'exemple ci-dessous, les `strings` que contient le `tuple` sont ordonnées en fonction de leur longueur grâce à la built-in fonction `len`.

# %%
sorted(("Donald", "Bob", "Bill"), key=len)

# %%
sorted(("Donald", "Bob", "Bill"), key=len, reverse=True)

# %%
sorted?

# %% [markdown]
# **Attention**, lorsqu'on référence une `list` existante *l1* avec un nouveam nom *l2*, les modifications de *l2* modifient *l1*. Comme déjà évoqué, les noms en Python ne sont que des références à des objets. Dans le cas ci-dessous, la liste `[1, 2, 3]` est un objet unique auquel on peut accéder par les deux références/noms `l1` et `l2`.

# %%
l1 = [1, 2, 3]
l2 = l1
l2[0] = 99
print(l1, l2)

# %%
l1[1] = 999
print(l1, l2)

# %%
id(l1) != id(l2)

# %% [markdown]
# Copier une `list` est une action qu'on va vouloir faire de temps en temps, il existe deux méthodes. La première effectue une `shallow copy` de la `list` source, c'est-à-dire, seuls les références aux objets que contient la `list` sont copiées.

# %%
l1 = [1, 2, 3]
l2 = l1[:]  # ou l1.copy()
l2[0] = 999
print(l1, l2)

# %%
id(l1) != id(l2)

# %% [markdown]
# Mais si la `list` fait référence à des **containers**, les références aux objets qu'ils contiennent ne sont pas copiées.

# %%
# Première méthode
l1 = [[1], 2, 3]
l2 = l1
l2[0][0] = 999
print(l1, l2)

# %%
# Deuxième méthode
l1 = [[1], 2, 3]
l2 = l1[:]  # ou l1.copy()
l2[0][0] = 999
print(l1, l2)

# %%
id(l1) != id(l2)

# %%
id(l1[0]) != id(l2[0])

# %% [markdown]
# On peut effectuer une **deep copy** pour palier au problème précédent. Cette méthode crée autant d'objet que contient la `list` source.

# %%
import copy
l1 = [[1], 2, 3]
l2 = copy.deepcopy(l1)
l2[0][0] = 999
print(l1, l2)

# %%
id(l1[0]) != id(l2[0])

# %% [markdown]
# Même si les objets de type `list` et `tuple` sont similaires, en général on ne les utilise pas de la même manière. Les `lists` vont plutôt contenir des objets du même type (exemple: liste de courses). Les `tuples` vont contenir une suite d'objets dont on est sûr à l'avance qu'elle n'aura pas besoin d'être modifiée (exemple: prénom et nom).

# %%
%reset -f

# %% [markdown]
# ## Sets

# %% [markdown]
# ---
#
# *Vraiment uniques*
#
# ---

# %% [markdown]
# Les objets de type `set` sont des **containers** et sont **mutables**. Ce ne sont pas des séquences, on ne peut donc pas accéder à leurs item par leur index numérique. Ce type d'objet **ne peut contenir que des objets uniques**.

# %%
s = {1, 2, 3}

# %%
type(s)

# %%
print(dir(s))

# %% [markdown]
# On peut supprimer les objets dupliqués d'une `list` ou d'un `tuple` en le transformat en objet `set`. Attention, **l'ordre est items des objets sources n'est pas préservé** en les transformant en `set`.

# %%
shopping1 = ["banana", "apple", "strawberry", "banana"]
shopping1 = set(shopping1)
shopping1

# %%
len(shopping1)

# %%
shopping1[0]

# %%
shopping1.add("orange")
shopping1

# %%
"orange" in shopping1

# %% [markdown]
# Avec les `sets` on peut facilement effectuer des opérations de la théorie des ensembles (`set theory`) comme l'intersection, l'union, la différence, ou la différence symétrique.

# %%
shopping2 = {"banana", "apple", "mango"}
shopping_intersect = shopping1.intersection(shopping2)
shopping_intersect

# %%
shopping_merged = shopping1.union(shopping2)
shopping_merged

# %% [markdown]
# On peut ensuite convertir un objet `set` en objet `list` avec la fonction `list`.

# %%
shopping_merged = list(shopping_merged)
shopping_merged

# %%
%reset -f

# %% [markdown]
# ## Dictionnaires

# %% [markdown]
# ---
#
# *Ils font la paire*
#
# ---

# %% [markdown]
# Les objets de type `dict` sont des **containers** et sont **mutables**. Tout comme les objets de type `set`, les `dicts` ne sont pas des séquences. Ils sont constitués de paires **key-value**. Les **keys** doivent être des objets **immutables**, les **values** peuvent être n'importe quel type d'objet. Les dictionnaires sont très présents dans le langage Python.

# %%
phonebook = {
    "Bob": 383,
    "Bill": 509,
    "Donald": 102
}
phonebook

# %%
type(phonebook)

# %%
print(dir(phonebook))

# %%
phonebook["Bob"]

# %%
phonebook[383]

# %%
phonebook["John"]

# %%
# Rajouter une key-value entrée
phonebook["John"] = 984
phonebook

# %%
phonebook["John"]

# %%
# Vérifier si une key est dans le dict
"John" in phonebook

# %%
# Cela ne fonctionne que sur les keys, par sur les values
984 in phonebook

# %%
# Supprimer une paire key-value
del phonebook["John"]
phonebook["John"]

# %%
# Les dicts ne sont pas des séquences.
phonebook[0]

# %%
# La longueur d'un dict est le nombre de paires key-value qu'il contient.
len(phonebook)

# %%
# Seuls des immutables peuvent être des keys
mess = {
    "str": "Les strings sont immutables",
    12: "Les ints sont immutables",
    3.53: "Les floats sont immutables",
    (12, 24): "Les tuples sont immutables"
}

# %%
# Les lists sont mutables, elles ne peuvent pas être des keys
mess[["list as a key"]] = 1

# %%
# Ici la key est un tuple, on sait que les tuples sont immutables.
# Mais ce tuple-là elle contient une liste, qui est un objet mutable
# La key n'est donc pas considérée comme une key valide.
mess[(["tuple as a key"], ["containing a list"])] = 1

# %%
# Une autre manière de créer un dict.
{"name": ["Bob", "Bill"], "age": [24, 23]} == dict(name=["Bob", "Bill"], age=[24, 23])

# %%
# Les values d'un dict peuvent être de n'importe quel type.
import math
d = {
    3.13: math,
    "print": print,
    "l": [1, 2, 3],
    123: "123",
    "nested_dicts": {"another_one": {"and_a_last_one": "here I am!"}},
    "sets": {1, 3, 5},
    True: False
}
d

# %%
d["nested_dicts"]["another_one"]["and_a_last_one"]

# %% [markdown]
# La méthode `get` est pratique, elle retourne la **value** de la **key** passée comme argument. Si la **key** n'est pas trouvée, elle retourne `None` par défaut ou la valeur du deuxième argument passé. 

# %%
d.get(123, "found")

# %%
d.get(456, "not found")

# %%
d.get?

# %% [markdown]
# On peut obtenir une `list` des **keys** ou des **values** en convertissant les objets retournés par les méthodes `keys` et `values` avec la fonction `list`.

# %%
list(d.keys())

# %%
list(d.values())

# %% [markdown]
# La méthode `pop` enlève la **key** spécifiée et retourne la **valeur** correspondante. 

# %%
d.pop(3.13)


# %%
d

# %%
%reset -f


# %% [markdown]
# ## Fonctions

# %% [markdown]
# ---
#
# *Don't Repeat Yourself*
#
# ---

# %% [markdown]
# On a déjà vu quelques unes des fonctions intégrées directement dans Python (**built-in functions**). On peut en fait créer nos propres fonctions. Cela est bien utile lorsqu'on souhaite réutiliser un bout de code, et/ou lorsqu'on souhaite faciliter la lecture/compréhension du code en le scindant en blocs logiques. On crée un objet `function` avec le **keyword `def`**. 

# %%
def say_hi():
    print("hi")


# %%
type(say_hi)

# %%
print(dir(say_hi))

# %% [markdown]
# Le code sous la définition de la fonction `say_hi` est exécuté lorsqu'on l'appelle.

# %%
say_hi()


# %% [markdown]
# Une fonction peut avoir des **paramètres**. On les précise sur la ligne de définition de la fonction. Ils peuvent ensuite être utilisés dans la fonction. La fonction `add` a deux paramètres `x` et `y`.

# %%
def add(x, y):
    print(x + y)


# %% [markdown]
# La fonction `add` est appelée avec les **arguments** `3` et `4`.

# %%
add(3, 4)

# %%
result = add(3, 4)

# %%
result

# %%
result is None


# %% [markdown]
# **Une fonction ne retourne qu'un seul et unique objet, qui est `None` par défaut.** On définit l'objet retourné en le précédant du **keyword `return`**.

# %%
def add(x, y):
    return x + y


# %%
result = add(3, 4)

# %%
result


# %% [markdown]
# L'objet `string` entouré de `"""` et positionné au début du bloc de la fonction est la **docstring** de la fonction.

# %%
def add(x, y):
    """Additioner deux objets."""
    return x + y


# %%
add.__doc__

# %%
help(add)

# %% [markdown]
# Comme une fonction est un objet, on peut la manipuler comme les autres objets.

# %%
add2 = add

# %%
add2(2, 3)

# %%
# del add enlève le nom add du namespace
del add
add2(0, 2)

# %% [markdown]
# Certains paramètres peuvent avoir **des valeurs par défaut**. Lorsqu'on appelle la fonction, on n'est donc pas obligé de préciser la valeur de ce paramètre (ce qui équivaut à dire qu'on n'est pas obligé de fournir un argument pour ce paramètre). Dans ce cas-là, la valeur par défaut est utilisée lors de l'exécution du code. Lorsqu'on souhaite utiliser une autre valeur que la valeur par défaut, on peut soit **fournir l'argument si on respecte l'ordre des paramètres**, on peut aussi **fournir l'argument en nommant le paramètre (`param=arg`)**.

# %%
print?


# %%
def function_with_defaults(a, b, c=0):
    return a + b + c
function_with_defaults(1, 4)

# %%
function_with_defaults(1, 4, c=50)

# %%
function_with_defaults(1, 4, 5)

# %%
function_with_defaults(c=50, 1, 4)

# %%
function_with_defaults(c=50, b=4, a=1)


# %% [markdown]
# Une fonction peut appeler une autre fonction.

# %%
def first():
    print("first function called")
    second()

def second():
    print("second function called")


# %%
first()

# %% [markdown]
# Lorsqu'on exécute le bloc de définition d'une fonction (la ligne `def` et le bloc indenté qui suit), **Python se prépare à exécuter la fonction mais ne l'exécute pas encore**, elle ne le sera que lorsqu'elle sera appelée. A part les erreurs de syntaxe (`SyntaxError`) que Python détecte lors de cette étape de préparation, **toutes les autres erreurs sont détectées seulement lorsque la fonction est appelée**. 

# %%
unknown


# %%
# unknown n'est pas une variable définie, malgré ça, on peut exécuter ce code
def dont_even_dare():
    return unknown


# %%
# On obtient une erreur lorsqu'on appelle la fonction dont_even_dare
dont_even_dare()


# %% [markdown]
# L'exécution d'une fonction se passe dans son **scope local**. Les objets référencés par la fonction (`firstname = "Bob"`) sont déférencés lorsque l'exécution prend fin. On ne peut plus y avoir accès après ça.

# %%
def function_scope():
    firstname = "Bob"
function_scope()
firstname


# %% [markdown]
# Même la référence de l'objet retourné par la fonction est supprimée à la fin de l'exécution.

# %%
def function_scope():
    firstname = "Bob"
    return firstname
function_scope()
firstname

# %% [markdown]
# Pour préserver l'objet retourné on lui associe un nom.

# %%
firstname = function_scope()
firstname


# %% [markdown]
# `x` ci-dessous n'est ni un paramètre de la fonction `look_outside` ni un objet créé dans la fonction. Lorsqu'on exécute `look_outside`, Python regarde d'aborde dans le **scope local** de la fonction s'il existe une référence `x`. Comme il ne la trouve pas, Il cherche alors dans le **scope global** de la fonction.
#
# Dans le premier cas ci-dessous, aucune référence `x` n'est créée en dehors du **scope** de la fonction. Une erreur est donc déclenchée.

# %%
def look_outside(b):
    return x + b

look_outside(20)


# %% [markdown]
# Ici, comme la référence `x` est créée (ajoutée au *namespace*) avant l'exécution de `look_outside`, celle-ci peut la trouver et s'exécute dont jusqu'à son terme.

# %%
def look_outside(b):
    return x + b

x = 10
look_outside(20)


# %%
def look_inside_first(b):
    x = 0
    return x + b

x = 10
look_inside_first(20)


# %% [markdown]
# Dans le cas ci-dessous, `outer_function` est appelée avec `b=20`. Lors de son exécution, la fonction `inner_function` est d'abord définie. Puis `outer_function` tente de retourner `x + inner_function() + b`. Elle trouve une référence à `x` dans le **scope global**. Elle exécute ensuite `inner_function`. Cette dernière doit retourne la référence `y`, sauf que cette référence n'est définie nulle part. Une erreur est donc déclenchée.

# %%
def outer_function(b):
    def inner_function():
        return y
    return x + inner_function() + b

x = 10
outer_function(20)


# %% [markdown]
# Le code va s'exécuter correctement tant que la référence à `y` est créée avant ou pendant l'exécution de `inner_function`.

# %%
def outer_function(b):
    y = 100
    def inner_function():
        return y
    return x + inner_function() + b

x = 10
outer_function(20)


# %%
def outer_function(b):
    def inner_function():
        y = 100
        return y
    return x + inner_function() + b

x = 10
outer_function(20)


# %%
def outer_function(b):
    def inner_function():
        return y
    y = 100
    return x + inner_function() + b

x = 10
outer_function(20)


# %%
def outer_function(b):
    def inner_function():
        return y
    return x + inner_function() + b

x = 10
y = 100
outer_function(20)


# %% [markdown]
# **Attention aux objets mutables passés comme argument à une fonction**. Lorsqu'on passe un argument à une fonction, celle-ci utilise directement l'objet référencé.

# %%
def is_same_objet(i, f, s, l, t, se, d):
    print(id(i) == id(io))
    print(id(f) == id(fo))
    print(id(s) == id(so))
    print(id(l) == id(lo))
    print(id(t) == id(to))
    print(id(se) == id(seo))
    print(id(d) == id(do))

io, fo, so, lo, to, seo, do = 1, 2.2, "", list(), tuple(), set(), dict()
is_same_objet(io, fo, so, lo, to, seo, do)


# %% [markdown]
# Si on passe un objet **mutable** comme argument d'une fonction, cette fonction va utiliser directement cet objet. S'il est modifié au cours de l'exécution de la fonction, c'est le bien **mutable source** qui est modifié, même s'il n'a pas la même référence dans la fonction.

# %%
def achtung_mutable(mutable):
    mutable[0] = "John"
    return mutable


# %%
new_names = achtung_mutable(names)
new_names

# %%
# names a aussi été modifié!
names

# %% [markdown]
# Si ce comportement n'est pas souhaité, on peut soit appeler la fonction avec une copie du **mutable**, soit créer une copie directement dans le bloc de la fonction.

# %%
names = ["Bob", "Bill"]
new_names = achtung_mutable(names[:])
print(new_names, names)


# %%
def achtung_mutable(mutable):
    mutable = mutable[:]
    mutable[0] = "John"
    return mutable

names = ["Bob", "Bill"]
new_names = achtung_mutable(names[:])
print(new_names, names)

# %%
%reset -f

# %% [markdown]
# ## Unpacking, Packing

# %% [markdown]
# ---
#
# *Déballer son sac*
#
# ---

# %% [markdown]
# On peut facilement extraire un à un les éléments d'un objet **iterable** (**séquences** et **containers**) pour assigner de nouvelles variables avec la méthode dite de l'**unpacking**. Cela se fait le plus souvent à partir d'un `tuple`.

# %%
t = ("Bob", 27, ["Sarah", "Jim"])

# %%
type(t)

# %% [markdown]
# `t` comprend trois éléments, ces trois éléments sont assignés dans l'ordre aux variables `name`, `age` et `siblings`.

# %%
name, age, siblings = t
print(name, age, siblings)

# %% [markdown]
# Mais on peut aussi le faire avec d'autres types d'objet (avec plus ou moins de succès).

# %%
l = ["Bob", 27, ["Sarah", "Jim"]]
name, age, siblings = l
print(name, age, siblings)

# %%
s = "abc"
a, b, c = s
print(a, b, c)

# %%
# Attention! Les keys des dictionnaires ne sont ordonnées
# que depuis la version 3.6.
d = {"name": "Bob", "surname": "Smith"}
n, s = d
print(n, s)

# %%
# Mauvaise idée!
s = {"a", "b", "c"}
a, b, c = s
print(a, b, c)

# %%
x = 3.4
pint, pdec = 3.4

# %% [markdown]
# Il est préférable que le nombre de variable à assigner soit égal au nombre d'éléments qui constituent l'**iterable**.

# %%
a, b = ("a")

# %%
a, b = ("a", "b", "c")

# %% [markdown]
# Si ce n'est pas le cas, on peut rajouter un symbole `*` devant le nom d'une des variables pour déclencher un comportement spécial.

# %%
l = ("First value of interest", "big", "mess", "after", "that")
myvalue, *mess = l
print(myvalue, mess)

# %% [markdown]
# On peut utiliser l'**unpacking** et le symbole `*` pour passer tous les éléments extraits d'un **iterable** à une fonction.

# %%
names = ["Rachel", "Sarah", "Bob", "Bill"]
print(names)

# %%
print(*names)

# %%
*names

# %% [markdown]
# **Packing** est l'action par laquelle plusieurs objets sont rassemblés dans un `tuple`.

# %%
"Bob", 27, ["Sarah", "Jim"]

# %%
packed = "Bob", 27, ["Sarah", "Jim"]
packed

# %%
type(packed)


# %% [markdown]
# **Lorsqu'on essaie de retourner plusieurs objets dans une fonction, ceux-ci sont en fait toujours rassemblés dans un `tuple`.** **Packing** est à l'oeuvre.

# %%
def person_info():
    return "Anna", 26  # --> return (name, age)

output = person_info()
type(output)

# %% [markdown]
# On peut utiliser l'**unpacking** pour assigner à des variables les objets retournés par la fonction `person_info`.

# %%
name, age = person_info()
print(name, age)

# %%
%reset -f

# %% [markdown]
# ## Boucle `for` et fonctions associées

# %% [markdown]
# ---
#
# *May the for be with you*
#
# ---

# %% [markdown]
# **Les boucles `for` sont très simples et utiles en Python.** Elles permettent de répéter un bloc d'instructions un certain nombre de fois. L'objet qui suit le keyword `in` doit être un **iterable**.

# %%
for i in range(3):
    print(i)

# %%
range?

# %% [markdown]
# `range` est une fonction qui accepte 3 arguments `start`, `stop` et `step`. Par défaut `start` est égal à 0 et `step` à 1. Cette fonction ne retourne pas une liste mais un obtjet de type `range`. Il s'agit d'un objet un peu spécial. Lorsqu'on exécute `range(1_000_001)`, considérant le code de la cellule précédente, on pourrait penser que cette instruction génère des nombres de 0 à 1000000, mais non. Cet objet est une sorte de *distributeur*, il ne fait rien tant qu'on ne lui demande rien. Lorsqu'on lui demande quelque chose, comme dans une boucle `for`, il s'active et commence à distribuer. Dans le cas de `range(1_000_001)`, l'objet distribue des `ints` en commençant à 0, un par un, jusqu'à 1000000.

# %%
for i in range(3):
    print(id(i))

# %%
type(range(3))

# %% [markdown]
# Pour créer une liste croissante d'entiers, on peut convertir un objet `range` en liste avec la fonction `list`. Alors que `range(100_000_001)` occupe très peu de mémoire, `liste(range(100_000_001))` va occuper plus de 900Mb (ne pas exécuter ça!).

# %%
list(range(3))

# %% [markdown]
# Pour itérer au travers d'une `list`, **on pourrait** écrire le code suivant:
# * On génère des `ints` avec la fonction `range`, le nombre d'ìnts` à générer dépend de la longueur de la `list` qu'on calcule avec la fonction `len`
# * On accède à chaque item de la `list` par son indice

# %%
names = ["Sarah", "Rachel", "Bob", "Bill"]
for i in range(len(names)):
    print(names[i])

# %% [markdown]
# Même si la méthode ci-dessus fonctionne, elle n'est en fait pas *pythonic*, elle s'inspire de la manière dont on écrit une boucle `for` dans d'autres langages. Python propose une manière plus claire d'itérer au travers d'un objet. La boucle `for` de Python est en fait similaire à une boucle `for each`, elle extrait chaque élément de l'**iterable** sur laquelle elle agit.

# %%
for name in names:
    print(name)

# %% [markdown]
# On peut pratiquer l'**unpacking** dans la ligne de la boucle `for`.

# %%
fullnames = [("Rachel", "Miller"), ("Bob", "Smith"), ("Anna", "Johnson"), ("Bill", "Davis")]
for first_name, last_name in fullnames:
    print(first_name, last_name)

# %% [markdown]
# On peut utiliser la boucle `for` pour itérer au travers des objets de type `string`, `list`, `tuple`, `dict`, `set` (et plus encore).

# %%
txt = "abcdefghi"
for letter in txt:
    print(letter)

# %%
names = ("Bob", "Bill", "Sarah", "Anna")
for name in names:
    print(name)

# %%
phonebook = {
    "Bob": 383,
    "Bill": 509,
    "Donald": 102
}
for k in phonebook:
    print(k)

# %%
for k, v in phonebook.items():
    print(k, v)

# %%
for v in phonebook.values():
    print(v)

# %% [markdown]
# On peut inverser l'ordre des itérations en appelant la fonction `reversed` sur l'**iterable**.

# %%
for name in reversed(names):
    print(name)

# %% [markdown]
# Un peu comme la fonction `range`, la fonction `reversed` ne retourne pas une `list` mais un objet qualifié d'**iterator**. Il s'agit aussi d'un *distributeur*, il distribue dans ce cas-là les éléments de l'**iterable** en commençant par le dernier. Comme on peut itérer sur un **iterator**, ce type d'objet est aussi un **iterable**.

# %%
reversed(names)

# %%
type(reversed(names))

# %%
reversed(names)[0]

# %% [markdown]
# Les **iterators** sont des objets qui se tarissent. Après leur avoir demandé de distribuer leur \"contenu" une fois, ils ne peuvent plus le redistribuer.

# %%
reversed_names = reversed(names)
list(reversed_names)

# %%
list(reversed_names)

# %% [markdown]
# `reserved_names` est maintenant un **iterator** vide, on ne peut plus le réutiliser. (A noter que l'objet retourné par `range` ressemble à un **iterator** mais n'en est en fait pas un, on peut donc le réutiliser).

# %%
for name in sorted(names):
    print(name)

# %%
for name in sorted(names, key=len):
    print(name)

# %% [markdown]
# `sorted` ne retourne pas un **iterator** mais directement une `list`.

# %%
sorted(names)

# %%
type(sorted(names))

# %% [markdown]
# **La fonction `enumerate` fournit sous la forme d'un `tuple` un compteur et les les éléments de l'iterable avec laquelle elle est appelée.**

# %%
for i, name in enumerate(names):
    print(f"Iteration {i}: {name}")

# %%
for i, name in enumerate(reversed(names)):
    print(f"Iteration {i}: {name}")

# %% [markdown]
# L'objet que la fonction `enumerate` retourne est un **iterator**.

# %%
enumerate(names)

# %%
enumerated_names = enumerate(names)
type(enumerated_names)

# %%
list(enumerated_names)

# %%
list(enumerated_names)

# %% [markdown]
# La function `zip` permet d'itérer sur plusieurs **iterables** en extrayant leur élément en même temps. L'objet qu'elle retourne est un **iterator**.

# %%
ages = [25, 28, 23, 21]
first_letters = ["B", "R", "B", "A"]

# %%
for name, first_letter, age in zip(names, first_letters, ages):
    print(name, first_letter, age, sep="   ---    ")

# %%
for i, (name, first_letter, age) in enumerate(zip(names, first_letters, ages)):
    print(i, name, first_letter, age, sep="   ---    ")

# %%
zipped = zip(names, first_letters, ages)
type(zipped)

# %%
list(zipped)

# %%
list(zipped)

# %% [markdown]
# Mais que se passe-t-il exactement lorsqu'on exécute une boucle `for`? A chaque itération, un élément de l'**iterable** est référencé par le nom défini juste après le *keyword* `for`. On peut voir que les objets extraits d'une `list` sont exactement les objets auxquels elle fait référence.

# %%
for i, name in enumerate(names):
    print(id(names[i]), id(name), sep="   ---   ")

# %% [markdown]
# **On a souvent besoin de modifier un à un les éléments d'une `list`** (exemple: mettre des noms en capitales). On peut **commettre l'erreur** de l'implémenter de la manière suivante.

# %%
for name in names:
    name = name.upper()
names

# %% [markdown]
# Cela ne fonctionne pas car l'instruction `name = name.upper()` crée un nouvel objet dont la valeur est `name.upper()` et qui est associé au nom `name`. La référence à l'élément de `names` par le nom `name` est donc perdue (écrasée, remplacée).

# %%
for i, name in enumerate(names):
    print(f"name(id={id(name)}, valeur=names[{i}])")
    name = name.upper()
    print(f"name(id={id(name)}, valeur=names[{i}].upper()]", end="\n\n")

# %% [markdown]
# Une autre option serait d'accéder à chaque élément de la `list`.

# %%
for i in range(len(names)):
    names[i] = names[i].upper()
names

# %% [markdown]
# **Mais la méthode recommandée est la suivante**:
# * On crée une `list` vide avec `l = []`
# * A chaque itération on vient rajouter un élément à cette liste vide avec la méthode `append` (`l.append(new_item)`)

# %%
names = ["Bob", "Bill", "Sarah", "Rachel"]
upper_names = []
for name in names:
    upper_names.append(name.upper())
upper_names

# %% [markdown]
# On peut inclure des conditions `if` dans le bloc d'une boucle `for` pour préciser les actions à effectuer.

# %%
for name in names:
    if "s" in name.lower():
        if "a" in name.lower():
            if "r" in name.lower():
                print(f"I think you're Sarah, correct? Hmm I'm {name}!")

# %% [markdown]
# Cela génère des fois du code qui est très indenté et pas facile à lire, **on peut utiliser les *keywords* `continue` et `break` pour contrôler l'exécution de la boucle**. `continue` entraîne le démarrage direct de la prochaine itération, ainsi, tout le code qui est situé sous `continue` est passé si `continue` est exécuté. `break` arrête totalement l'exécution de la boucle.

# %%
for name in names:
    if "s" not in name.lower():
        continue
    if "a" not in name.lower():
        continue
    if "r" not in name.lower():
        continue
    # Exécuté si les trois conditions ci-dessus sont fausses
    print(f"I think you're Sarah, correct? Hmm I'm {name}!")
    break

# On aurait aussi pu écrire le code de la manière suivante:
# for name in names:
#     if all(c in name.lower() for c in "sar"):
#         print(f"I think you're Sarah, correct? Hmm I'm {name}!")
#         break

# %%
for name in names:
    if name == "Sarah":
        continue
    print(name)  # Exécuté si name != "Sarah"

# %%
for name in names:
    if name == "Sarah":
        break  # Stoppe la boucle lorsque name == "Sarah"
    print(name)

# %% [markdown]
# Contrairement aux références créés dans le **scope** d'une fonction, les références créés dans un bloc `for` ne sont pas supprimées à la fin de l'exécution du bloc. La référence `name` est donc toujours accessible et sa valeur est celle de la dernière itération. Ici on voit que sa valeur est `'Sarah'`, ce qui a effectivement stoppé l'exécution de la boucle.

# %%
name

# %% [markdown]
# ## Boucle `while`

# %% [markdown]
# ---
#
# *On ne l'arrête plus*
#
# ---

# %% [markdown]
# La boucle `for` en Python est tellement pratique que la boucle `while` est au final assez peu utilisée. Les instructions d'une boucle `while` sont exécutées tant que la condition qui suit le *keyword* `while` est vraie. On peut aussi utiliser les *keywords* `continue` et `break` pour contrôler l'exécution de la boucle.

# %%
i = 0
while i < 5:
    print(i)
    i += 1

# %% [markdown]
# Il peut être plus naturel d'écrire une boucle `while` au lieu d'une boucle `for` lorsque l'on recherche quelque chose dans un **iterable**.

# %%
letters = "abcdefghijklmnopqrstuvwxyz"
index_o = 0
while letters[index_o] != "o":
    index_o += 1
print(f"La lettre `o` est la lettre n°{index_o + 1} de l'alphabet")

# %%
for i, l in enumerate(letters):
    if l == "u":
        index_u = i
        break
print(f"La lettre `u` est la lettre n°{index_u + 1} de l'alphabet")

# %% [markdown]
# Un des **dangers de la boucle `while` est qu'on peut créer une boucle qui ne s'arrête jamais**. Le code ci-dessous va s'exécuter à l'infini, la condition `i < 5` étant toujours vraie (on a oublié d'incrémenter `i`). Il faut alors forcer l'arrêt de l'interpréteur Python.

# %%
# i = 0
#  while i < 5:
#    print(i)

# %% [markdown]
# ## Lire et écrire dans un fichier

# %% [markdown]
# ---
#
# *Cours Primaire*
#
# ---

# %% [markdown]
# On peut facilement lire le contenu d'un fichier texte et écrire du texte dans un fichier. Pour cela, on utilise:
# * la fonction `open` qui permet d'ouvrir un fichier et de le lire ou d'y écrire quelque chose
# * le *keyword* `with` qui signale l'utilisation d'un objet qualifié de **context manager** (ici, la fonction `open`). L'emploi de ce genre d'objet avec un bloc `with` permet de s'assurer de la fermeture de la ressource ouverte (ici, un fichier), même si une erreur se produit dans l'exécution du bloc de code

# %%
%%writefile data.txt
name,age,gender
Sarah,27,F
Bob,28,M
Rachel,24,F
Bill,22,M

# %% [markdown]
# La fonction `open` ouvre le fichier en mode lecture (`"r"` pour *read*) et retourne un objet référencé par `f` (on peut choisir n'importe quel nom) et lié au fichier en cours de lecture.

# %%
with open("data.txt", "r") as f:
    print(type(f))
    print(dir(f))

# %% [markdown]
# On peut vérifier que le fichier est bien fermé par le **context manager**.

# %%
with open("data.txt", "r") as f:
    print(f.closed)

print(f.closed)

# %% [markdown]
# Pour l'instant l'exécution des instructions du bloc `with` s'est déroulée sans erreur. On peut montrer que le **context manager** ferme bien le fichier même si une erreur survient dans le bloc.

# %%
f.closed

# %%
with open("data.txt", "r") as f:
    print("Fichier ouvert?", not f.closed)
    print(f.wrong_attribute_to_trigger_an_error)
    print("Rien ne va plus")

# %%
print("Fichier ouvert?", not f.closed)

# %% [markdown]
# On peut lire le contenu complet du fichier grâce aux méthodes `read` et `readlines`.

# %%
with open("data.txt", "r") as f:
    whole_content = f.read()
whole_content

# %%
print(whole_content)

# %%
with open("data.txt", "r") as f:
    lines = f.readlines()
lines

# %%
for line in lines:
    print(line)

# %% [markdown]
# Chaque ligne du fichier se termine par un caractère *retourne à la ligne*. On peut utiliser la méthode `rstrip` des objets de type `string` pour retirer ce caractère spécial.

# %%
for line in lines:
    print(line.strip())

# %% [markdown]
# Mais **on peut aussi le lire ligne par ligne en itérant sur l'objet retourné par la fonction `open`**. Cet objet est en fait un **iterator**.

# %%
with open("data.txt", "r") as f:
    for line in f:
        print(line.strip())

# %% [markdown]
# Comme `f` est un **iterator**, on ne peut itérer dessus qu'un seule fois.

# %%
with open("data.txt", "r") as f:
    for line in f:
        print(line.strip())
    for line in f:
        print(line.strip())

# %% [markdown]
# L'avantage de lire un fichier ligne par ligne est double:
# * On ne charge pas l'ensemble des données du fichier dans la mémoire
# * On peut arrêter sa lecture avant la fin si on cherche quelque chose de précis

# %%
with open("data.txt", "r") as f:
    for i, line in enumerate(f):
        if "Bob" in line:
            print(f"I've found Bob @line {i + 1} !!!")
            break  # Stoppe la lecture du fichier

# %%
with open("data.txt", "r") as f:
    for i, line in enumerate(f):
        line = line.strip()
        if line.startswith("Bob"):
            age = line.split(",")[1]
            break
print(f"Bob is {age} yo.")

# %% [markdown]
# Pour écrire dans un nouveau fichier, la démarche est tout à fait similare. Au lieu de passer l'argument `r` à la fonction `open`, on lui passe l'argument `w` (pour *write*). La méthode `write` n'accepte comme argument que des objets de type `string`. Au besoin, on convertit les objets (`float`) par exemple en `string` en les passant comme argument à la fonction `str`.

# %%
names = ["Sarah", "Rachel", "Bob", "Bill"]
with open("new_data.txt", "w") as f:
    for name in names:
        f.write(name)

# %%
!type new_data.txt

# %% [markdown]
# Il faut faire attention à inclure le caractère spécial `"\n"` pour marquer les sauts de ligne.

# %%
names = ["Sarah", "Rachel", "Bob", "Bill"]
with open("new_data.txt", "w") as f:
    for name in names:
        f.write(name)
        f.write("\n")

# %%
!type new_data.txt

# %%
names = ["Sarah", "Rachel", "Bob", "Bill"]
with open("new_data.txt", "w") as f:
    for name in names:
        f.write(name + "\n")

# %%
!type new_data.txt

# %%
ages = [26, 24, 29, 25]
with open("new_data.txt", "w") as f:
    for age in ages:
        f.write(str(age) + "\n")

# %%
!type new_data.txt

# %% [markdown]
# On peut aussi utiliser la méthode `writelines` pour écrire directement l'ensemble des éléments d'un objet dans le fichier.

# %%
names = ["Sarah", "Rachel", "Bob", "Bill"]
with open("new_data.txt", "w") as f:
    f.writelines("\n".join(names))

# %%
!type new_data.txt

# %%
!del /f new_data.txt data.txt
%reset -f

# %% [markdown]
# ## Interactions

# %% [markdown]
# ---
#
# *Le client est roi*
#
# ---

# %% [markdown]
# On peut intéragir avec du code Python lors de son exécution de deux manières différentes:
# * En passant des arguments à la suite de la commande `python myscript.py` exécutée dans la **Command Prompt**. On peut récupérer la valeur de ces arguments et l'utiliser dans le code
# * En utilisant la fonction `input` qui met en pause l'exécution du code tant que l'utilisateur n'entre pas une valeur.

# %%
%%writefile argv.py
import sys
age = sys.argv[1]
print(f"You are {age} years old.")

# %%
# Equivalent à `python argv.py 28` dans la command prompt
%run argv.py 28

# %% [markdown]
# Avec la première méthode, on peut facilement créer des outils flexibles sous la forme de scripts

# %%
%%writefile add.py
import sys
a, b = sys.argv[1], sys.argv[2]  # ou a, b = sys.argv[1:]
print(float(a) + float(b))

# %%
%run add.py 3 4.5

# %%
%%writefile showcontent.py
import sys
file = sys.argv[1]
with open(file, "r") as f:
    content = f.read()
print(content)

# %%
%%writefile names.txt
Anna
Rachel
Bob
Bill

# %%
%run showcontent.py names.txt

# %% [markdown]
# La fonction `input` peut accepter un argument de type `string`. Si on lui en fournit un, elle l'affiche puis attent qu'on entre une valeur et tape sur la touche *Entrée*, l'objet qu'elle retourne est une `string` qui contient ce que l'on vient de taper.

# %%
input()

# %%
age = input("How old are you?")

# %%
%%writefile input.py
age = input("How old are you?")
print(f"You are {age} years old.")

# %%
# Equivalent à `python input.py` dans la command prompt
%run input.py

# %%
!del /f input.py argv.py showcontent.py names.txt add.py
%reset -f


# %% [markdown]
# ## Traceback

# %% [markdown]
# ---
#
# *Suivie à la trace*
#
# ---

# %% [markdown]
# Le **traceback** est le long message que Python affiche lorsqu'une erreur survient pendant l'exécution du code. **Le traceback se lit de bas en haut**. Il est très utile pour **débugger** un script.

# %%
def first_level(a, b):
    return second_level(a, b)


def second_level(a, b):
    return third_level(a, b)


def third_level(a, b):
    return a + b


# %%
first_level(1, 2)

# %% [markdown]
# L'addition des paramètres `a` et `b` est réalisée par la fonction `third_level`. On va déclencher une `TypeError` en tentant d'additioner une `string` avec un `int`, ce qui est impossible.

# %%
"Bob" + 1

# %%
first_level("Bob", 1)

# %% [markdown]
# Le **traceback** nous indique que l'erreur s'est produite à la ligne `return a + b` du code dans la fonction `third_level`. Il afficher ensuite (de bas en haut) les appels successifs aux trois fonctions imbriquées.

# %%
%reset -f


# %% [markdown]
# ## Classes

# %% [markdown]
# ---
#
# *Des objets, des objets, des objets*
#
# ---

# %% [markdown]
# On peut définir nos propres types d'objet avec le *keyword* `class`. La `class` définit les attributs et les méthodes des objets qu'elle va engendrer.  

# %%
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def __repr__(self):
        return f"rectangle of width: {self.width} and height: {self.height}"
    
    def __eq__(self, other_rectangle):
        if self.width == other_rectangle.width and self.height == other_rectangle.height:
            return True
        else:
            return False
        
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)


# %%
type(Rectangle)

# %%
print(dir(Rectangle))

# %%
r1 = Rectangle(10, 5)

# %%
type(r1)

# %%
print(dir(r1))

# %%
r1

# %%
print(r1.perimeter(), r1.area())

# %%
r2 = Rectangle(5, 10)
r2 == r1

# %%
r1 > r2

# %%
%reset -f

# %%
