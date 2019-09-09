Installation
============

1. Télécharger `Miniconda <https://docs.conda.io/en/latest/miniconda.html>`_
   et lancer son installation. Garder les paramètres par défaut, sauf
   ceux ci-dessous.

   .. image:: images/miniconda_install.png
      :scale: 50 %
      :alt: Paramètres de l'installation de Miniconda

2.  Ouvrir l'**Anaconda Prompt** (voir dans les raccourcis)

   .. image:: images/anaconda_prompt.png
      :scale: 50 %
      :alt: Anaconda Prompt

3. Exécuter le code ci-dessous pour installer tous les packages indiqués
   après la commande ``conda``. **conda** va travailler un moment
   avec de proposer une liste de tous les packages à installer et dont
   les versions sont cohérentes les unes avec les autres. Taper ``y``
   pour accepter la proposition faite, ou ``n`` pour la refuser.

   .. code::
  
       conda install geoviews rasterio jupyterlab hvplot

   .. note:: 

       `geoviews <http://geoviews.org/>`_ est un package qui permet
       d'explorer et visualiser des données géographiques. Il dépend
       de beaucoup d'autres packages, dont **Numpy**, **pandas**, **Scipy**,
       **Matplolib**, **Geopandas**, **pyshp**, **GDAL**, **GEOS**,
       **requests**, **Click**, **Jupyter**, etc. Tous ces packages-là
       seront installés par *conda*, il n'est donc pas nécessaire de
       les lister.
       `rasterio <https://rasterio.readthedocs.io/en/stable/>`_ permet
       de traiter des données de type *raster*. Son utilisation est
       plus simple que celle de *GDAL* à partir de *Python*.
       `jupyterlab <https://jupyterlab.readthedocs.io/en/stable/>`_
       est la dernière version des **Jupyter Notebooks**.
       `hvplot <https://hvplot.pyviz.org/>`_ permet d'intégrer facilement
       des graphiques intéractifs dans un *notebook*.

4. Toujours dans la console **Anaconda Prompt**, exécuter les deux commandes
   ci-dessous pour installer **Spyder**. Celui-ci étant
   en version *beta*, il n'est toujours pas disponible sur la *channel*
   par défaut d'Anaconda. Il est cependant téléchargeable depuis une
   autre *channel* (nommée *spyder-ide*).

   .. code::
  
       conda update qt pyqt
       conda install -c spyder-ide spyder=4.0.0b4

L'installation ci-dessus a les effets suivants:

* Des raccourcis pour l'**Anaconda Prompt** et **Spyder** sont disponibles,
* Un seul et uniquement environnement *conda* nommé *base* et qui contient
  l'ensemble des packages installés.

.. attention:: 

    L'installation présentée ci-dessus est relativement simple. Il est
    bien sûr possible de personnaliser cette installation:
    
    * utiliser le *channel conda-forge* pour installer plus de packages
    * ajouter **conda** et **python** directement au ``PATH`` pour
      qu'ils sont disponibles directement depuis la **Command Prompt**
