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
# # Numpy, Pandas et Matplotlib en express

# %% [markdown]
# `Numpy`, `pandas` et `Matplotlib` sont trois librairies incontournables de l'écosystème scientifique de *Python*:
# * `Numpy` permet de créer des tableaux à plusieurs dimensions contenant des nombres, et de les transformer facilement à l'aide de nombreuses formules mathématique, elle a l'avantage d'accélérer les calculs comparé à Python,
# * `pandas` permet de créer des tableaux contenant des objets de type différent, et d'effectuer des opérations très similaires à celles qu'on peut effectuer avec *Excel*,
# * `Matplotlib` permet de créer des figures et de les personnaliser dans les moindres détails.  
#
# Ces trois librairies, développées depuis des années et des années, sont très fournies. L'objectif de ce tutoriel est de donner une impression de ce qu'il est possible de faire avec elles.

# %% [markdown]
# ## Numpy

# %% [markdown]
# On importe `Numpy` de la manière suivante, établie par convention.

# %%
import numpy as np

# %% [markdown]
# Les calculs réalisés avec `Numpy` sont plus rapides que les calculs effectués avec du pur Python.

# %%
%timeit sum(range(100_000))
%timeit np.sum(np.arange(100_000, dtype=np.int64))

# %% [markdown]
# On a maintenant à disposition des dizaines et des dizaines de fonctions pour réaliser des opérations mathématiques.

# %%
print(dir(np))

# %% [markdown]
# L'objet le plus important est le `ndarray`, pour tableau à *n* dimensions.

# %%
arr = np.array([1, 2, 3])
type(arr)

# %%
arr = np.array([[1, 2, 3], [4, 5, 6]])
arr

# %%
arr.shape

# %%
arr.T

# %%
arr.T.shape

# %%
np.arange(10, 50, 3)

# %%
np.zeros(shape=10)

# %%
np.zeros(shape=(2, 3))

# %%
np.zeros(shape=(2, 3, 1, 5))

# %%
np.ones(shape=(2, 5))

# %%
arr = np.array([[1, 2, 3], [10, 20, 30]]).T
arr

# %% [markdown]
# On accède à un élément d'un objet `ndarray` en précisant sa position (en partant de 0) suivant les axes de l'objet, séparés de virgules. Pour un tableau à deux dimensions (une matrice), le premier axe est celui des lignes, le deuxième celui des colonnes.

# %%
arr[0, 0]

# %%
arr[2, 1]

# %% [markdown]
# Pour accéder à tous les éléments suivant un axe (les colonnes, les lignes, etc.), on utilise le symbole `:`.

# %%
arr[:, 0]

# %%
arr[:, 1]

# %%
arr[0, :]

# %% [markdown]
# On peut effectuer des opérations mathématiques sur tous les éléments d'un `ndarray`.

# %%
arr + 1

# %%
arr * 3

# %% [markdown]
# Les `ndarray` sont des objets **mutables**.

# %%
arr[0, 0] = -1
arr

# %%
arr[0, :] = 1
arr

# %%
arr[:, 1] = 3
arr

# %%
arr[:, 1] = arr[:, 1] * arr[:, 0]
arr

# %% [markdown]
# On peut sélectionner des éléments d'un `ndarray` suivant une condition.

# %%
arr > 5

# %%
arr[arr > 5]

# %% [markdown]
# On peut piocher dans les dizaines de fonction dont `Numpy` dispose pour transformer les données

# %%
np.sum(arr)

# %% [markdown]
# `axis=0` signifie que l'addition est réalisée suivant le dimension `0`, ce sont donc les lignes qui sont additionnées. `axis=1` indique que ce sont les colonnes qui sont additionnées.

# %%
np.sum(arr, axis=0)

# %%
np.sum(arr, axis=1)

# %% [markdown]
# ## pandas

# %% [markdown]
# On importe `pandas` de la manière suivante, établie par convention.

# %%
import pandas as pd

# %% [markdown]
# L'objet le plus important est le `DataFrame` (tableau de données). On peut en créer de plusieurs manières différentes.

# %%
df = pd.DataFrame({
    "name": ["Rachel", "Bob", "Bill", "Anna", "Leila", "John"],
    "age": [23, 25, 24, 30, 19, 26],
    "height": [1.85, 1.79, 1.82, 1.72, 1.95, 1.65]
})

# %%
type(df)

# %%
df

# %%
df.head()

# %%
df.tail()

# %%
df.info()

# %%
df.describe()

# %%
df.shape

# %% [markdown]
# Les entrées d'un tableau sont son *index* (ses lignes) et ses *colonnes*.

# %%
df.index

# %% [markdown]
# Pour l'instant l'index du `DataFrame` est juste un indice numérique démarrant à 0. On peut définir un index plus intéressant en utilisant la colonne `name`.

# %%
df = df.set_index("name")
df

# %%
df.columns

# %% [markdown]
# On peut `indexer` le tableau avec les méthodes `loc` et `iloc`.

# %%
df.loc["Bob"]

# %%
df.loc["Bob", "height"]

# %%
df.iloc[1, 1]

# %% [markdown]
# On peut sélectionner une colonne entière pour l'utiliser et la modifier

# %%
df["height"]

# %%
df["height"] = df["height"] + 0.2
df.head()

# %% [markdown]
# On peut ajouter des colonnes.

# %%
df["age_plus_10"] = df["age"] + 10
df.head()

# %% [markdown]
# Lorsqu'on les données d'une colonne sont des nombres, on a en fait à disposition toutes les fonctions de `Numpy`. On a aussi bien d'autres fonctions (des méthodes en fait) disponibles.

# %%
df["age"].sum()

# %% [markdown]
# On peut facilement lire et écrire des fichiers (`.csv` par exemple) avec `pandas`.

# %%
%%writefile data.csv
name,age,height,gender
Sarah,27,1.67,F
Bob,28,1.89,M
Rachel,24,1.81,F
Bill,22,1.73,M
John,26,1.67,M
Leila,19,1.78,F

# %%
people = pd.read_csv("data.csv")
people

# %% [markdown]
# On peut compter le nombre d'éléments identiques dans une colonne avec la méthode `value_counts`. Cette méthode est disponible pour les objets de type `Series` qui représentent en fait les colonnes. La méthode retourne aussi un objet de type `Series.

# %%
people["gender"].value_counts()

# %% [markdown]
# On peut grouper les données et agréger les groupes obtenus à l'aide de fonctions.

# %%
people.groupby("gender").agg({"age": ["max", "min"], "height":["mean", "std"]})

# %% [markdown]
# On peut sélectionner des données suivant des conditions.

# %%
people["gender"] == "F"

# %%
girls = people[people["gender"] == "F"]
girls

# %% [markdown]
# On peut supprimer une colonne avec la méthode `drop`.

# %%
girls = girls.drop(columns=["gender"])
girls

# %%
girls.to_csv("girls.csv", index=False)

# %%
!type  girls.csv

# %%
!del /f data.csv girls.csv

# %% [markdown]
# ## Matplotlib

# %% [markdown]
# On importe `Matplotlib` de la manière suivante, établie par convention.

# %%
import matplotlib.pyplot as plt

# %% [markdown]
# `Matplotlib` a un mode similaire à celui de `Matlab`, on enchaîne juste des appels à des fonctions pour réaliser des actions sur le même objet.

# %%
plt.scatter([1, 3, 10], [-2, 3, 0])
plt.title("Titre")
plt.xlabel("X axis")
plt.savefig("comme_matlab.png")

# %%
!comme_matlab.png

# %% [markdown]
# On va **préférer la méthode par laquelle on modifier directement la figure au travers des objets qui la constituent**.

# %%
fig, ax = plt.subplots()
ax.scatter([1, 3, 10], [-2, 3, 0])
ax.set_title("Titre")
ax.set_xlabel("X Axis")
fig.savefig("avec_des_objets.jpg")

# %%
!image_with_matplotlib.png

# %% [markdown]
# On peut utiliser `Matplotlib` directement mais on retrouve en fait la librairie un peu partout, dans `pandas` notamment.

# %%
ax = df.plot(x="age", y="height", kind="scatter", title="Titre")
fig = ax.get_figure()
fig.savefig("avec_pandas.pdf")

# %%
!avec_pandas.pdf

# %%
!del /f comme_matlab.png avec_des_objets.jpg avec_pandas.pdf
