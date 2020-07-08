Installation
============

Dans un environnement scientifique, il est souvent recommandé d'installer Python et les packages
que l'on souhaite utiliser grâce à **conda**. Il est possible d'installer deux versions différentes:

* **Anaconda**: Intègre **conda** avec un environnement (nommé *base*) contenant beaucoup de
  packages utiles pour la *data science*,
* **Miniconda**: Intègre seulement **conda** et **python**, il est donc beaucoup plus léger qu'**Anaconda**.

**Il est recommandé dans ce tutoriel d'installer Miniconda** et de l'utiliser de la manière suivante.
L'environnement *base*, qui est l'environnement créé par défaut dans lequel se trouve installé **conda**, doit 
rester le plus simple possible. **Il ne doit servir que pour conda lui-même**, qu'on mettra à jour lorsque nécessaire 
avec la commande ``conda update conda`` à exécuter directement depuis cet environnement *base*. Si l'on souhaite installer d'autres packages (comme **pandas**), on 
le fera dans un ou plusieurs environnement(s) dédié(s). On exécutera par exemple ``conda create -n data_analysis pandas``
pour créer un environnement *data_analysis* incluant **pandas**, et ``conda create -n spyder spyder`` pour
créer un environnement incluant **Spyder**. Cette approche permet de bien séparer les outils qu'on utilise, 
de pouvoir les mettre à jour plus facilement, et évite donc bien des problèmes.

La procédure pour installer **Miniconda**, **Spyder** et créer des environnements **conda** est décrite ci-dessous.

1. Télécharger `Miniconda <https://docs.conda.io/en/latest/miniconda.html>`_, la version 64bits de Windows
   étant celle qu'il faudra vraisemblablement choisir. Lancer l'executable pour démarrer l'installation et
   garder les paramètres par défaut, sauf ceux ci-dessous. Même si avoir **conda** dans le ``PATH`` pourrait
   être pratique, désactiver cette option évite quelques problèmes potentiels.

   .. image:: images/miniconda_install.png
      :scale: 50 %
      :alt: Paramètres de l'installation de Miniconda

2.  Chercher la console **Anaconda Prompt** dans le menu *Démarrer* et la lancer. On voit qu'elle s'ouvre dans l'environnement
    *base* qui est créé par défaut lors de l'installation. Dans cet environnement se trouve **python**, **conda** et 
    quelques autres packages.

   .. image:: images/anaconda_prompt.png
      :scale: 50 %
      :alt: Anaconda Prompt

3. Dans la console **Anaconda Prompt**, exécuter la commande suivante pour installer **Spyder**
   dans un environnement dédié nommé *spyder* dans lequel se trouve la version *3.7* de **Python**.
   **pandas** est installé pour permettre au *Variable Explorer* de **Spyder** de visualiser 
   des *DataFrame*. Plus d'information est disponible sur le 
   `Wiki de Spyder <https://github.com/spyder-ide/spyder/wiki/Working-with-packages-and-environments-in-Spyder>`_ à ce sujet.

   .. code::
  
       conda create -n spyder python=3.7 spyder pandas

4. Dans la console **Anaconda Prompt**, exécuter la commande suivante pour installer un environnement avec
   les packages que l'on souhaite utiliser pour réaliser une tâche. L'exemple ci-dessous crée un environnement
   *gis* dans lequel vont être installés les packages **geopandas** et **rasterio**, plus leurs dépendances.
   Le package **spyder-kernels** permettra de connecter **Spyder** à cet environnement. Sans cela, il aurait été
   nécessaire de l'installer à nouveau.

   .. code::
  
       conda create -n gis python=3.7 geopandas rasterio spyder-kernels

5. Dans les options de **Spyder**, on paramètre l'interpréteur pour qu'il pointe vers la version de **Python** 
   de l'environnement qu'on souhaite utiliser. Se référer à nouveau au
   `Wiki de Spyder <https://github.com/spyder-ide/spyder/wiki/Working-with-packages-and-environments-in-Spyder>`_ pour obtenir la manière de paramétrer
   **Spyder** pour qu'il fonctionne ainsi.

   .. image:: images/spyder_interpreter_setting.png
      :scale: 70 %
      :alt: Sélection de l'environnement conda actif dans Spyder

L'installation ci-dessus a les effets suivants:

* Des raccourcis pour la console **Anaconda Prompt** et l'IDE **Spyder** sont disponibles dans le menu *Démarrer* de *Windows*,
* Trois environnements (exécuter ``conda info --envs`` dans l'**Anaconda Prompt** pour lister les environnement installés) ont été créés:
  *base*, *spyder* et *gis*.
* **Spyder** est paramétré de tel sorte qu'il est connecté à l'environnement *gis* et a donc accès aux packages
  qu'il contient tel que **geopandas**.

.. attention:: 

    L'installation présentée ci-dessus est une option, il en existe d'autres. Il aurait par exemple été possible de:

    * installer *Anaconda* au lieu de *Miniconda*. *Anaconda* contient un environnement *base* qui
      comprend une suite complète de packages dédiés à l'analyse de données. Cette suite est assez lourde, contient 
      des packages que l'on n'utilisera pas forcément, et est difficile à mettre à jour,
    * privilégier le *channel conda-forge* pour installer des packages depuis cette source-là qui en contient plus 
      et qui sont parfois plus à jour,
    * ajouter **conda** et **python** directement au ``PATH`` pour qu'ils soient disponibles directement
      depuis la **Command Prompt** classique de *Windows* sans passer par l'**Anaconda Prompt**.
    * exécuter la commande ``conda init`` pour modifier la **Command Prompt** de manière à ce qu'elle 
      démarre toujours en activant l'environnement *base*.
