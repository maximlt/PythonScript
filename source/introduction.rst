Introduction
============

Motivations
-----------

L'ordinateur est un outil qui nous facilite la vie. Le système d'opération
(*Windows* dans notre cas) effectue une grosse partie du travail: il
nous permet de contrôler la souris et le clavier, affiche des informations
sur l'écran, nous donne la possibilité de créer des fichiers et de 
les lires, etc. Les *logiciels* qu'on installe en plus, comme la suite
*Microsoft Office* nous facilitent encore plus la vie. On peut aisément
formater un rapport, créer des tableaux, envoyer des emails, etc. Malgré
tous ces outils, on se retrouve souvent à entreprendre des tâches
répétitives. On va par exemple copier le contenu de
dizaines de fichiers un à un dans un tableau Excel, télécharger
quotidiennement sur un site internet les mêmes informations, etc.   

Les outils comme *Windows* ou la suite *Microsoft Office* ne sont au
final que des logiciels: ils se résument à (beaucoup) de lignes de code.
La programmation permet de créer des outils, l'ordinateur n'est 
donc pas qu'un outil, c'est un outil avec lequel on peut créer 
d'autres outils.

La motivation est donc là, on va utiliser la programmation pour
créer nos propres outils et venir compléter notre suite initiale
d'outils. De cette manière, on limitera le temps passé à réaliser 
des tâches répétitives. On pourra aussi complémenter nos outils initiaux
pour les améliorer.

Le langage qui va être utilisé dans ce tutoriel est **Python**, 
mais ce n'est pas le seul qu'on pourrait utiliser. On peut
bien sûr mentionner **VBA** (dans *Excel*), ou encore le 
langage **R** qui est bien pratique lorsqu'il s'agit de faire
des statistiques.

Python
------

``Python`` est un langage informatique qui a été conçu par
*Guido van Rossum* en 1990. C'est un langage très polyvalent.
Il est depuis des années très présent dans le *Web*
(*Dropbox*, *Instagram*, etc.) et
est récemment devenu le langage de la *data science*. Sa forte popularité
actuelle vient aussi de la facilité avec laquelle on peut l'aborder, sa
syntaxe est simple et épurée, ses outils intégrés sont nombreux, 
en peu de temps on peut arriver à écrire du code qui va fonctionner et 
être utile. Il attire beaucoup de débutants en programmation, mais 
ne limite pas les développeurs expérimentés qui peuvent coder
des applications complexes.

La popularité du langage a des effets secondaires intéressants: la 
documentation (tutoriels, vidéos, etc.) disponible sur internet 
est incomparable, toutes nos questions vont trouver réponse.

``Python`` est un langage **interprété**. Cela signifie qu'il n'y 
a pas besoin de le compiler (créer un *.exe*) pour exécuter du 
code. On peut donc tester très rapidement un bout de code pour 
voir s'il s'exécute rapidement. Ce cycle court favorise
l'apprentissage du code.

``Python`` est un langage de **haut niveau** et un langage **dynamiquement
typé**. Pour résumer, il travaille beaucoup pour nous et nous évite
d'écrire du code superflu, on peut aller droit à l'essentiel.

``Python`` ne désigne en fait qu'un langage, défini par un vocabulaire et 
son lot de règles. ``Python`` lui-même est écrit dans un autre 
langage de programmation, le langage `C`. L'implémentation
de ``Python`` en ``C`` est nommée `CPython`. Il s'agit de
l'implémentation la plus utilisée 
et c'est celle qui sera utilisée dans ce tutoriel.

Au cours du temps, les utilisateurs de ``Python`` ont construit 
beaucoup de packages codés dans ce langage. Le langage étant gratuit 
et open-source, on retrouve beaucoup d'outils ``Python`` qui sont 
aussi gratuits et open-source. Le site `PyPi <https://pypi.org/>`_
héberge des milliers et des milliers de ces outils, qui sont appelés
**packages**. Étant donné
qu'il est très facile de les installer, on a à notre disposition 
une énorme boite à outils avec laquelle on peut construire tout 
ce que l'on veut.

Scripts
-------

Un script est un programme relativement simple contenu dans un
fichier texte. On peut écrire un script qui va:

* analyser les fichiers d'un dossier et de ses sous-dossiers,
* zipper des fichiers,
* supprimer des fichiers,
* analyser le contenu d'un ou plusieurs fichier(s),
* modifier le contenu d'un fichier texte,
* convertir le format d'un fichier (image, vidéo, etc.),
* gérer l'exécution d'autres programmes,
* générer des fichiers PDF,
* récupérer des données sur internet,
* envoyer des emails,
* etc.

Comme on peut le voir, toutes ces tâches peuvent être réalisées
manuellement. Mais on peut aussi toutes les programmer en ``Python``!

Contenu du tutoriel
-------------------

Environnement de travail
************************

* Où enregistrer son code? Comment installer un package?
* Comment avoir plusieurs versions de ``Python``?

Toutes ces questions peuvent se poser même lorsqu'on sait coder
en ``Python``. La configuration d'un environnement de 
travail constitué de logiciels supports permet d'adresser
chacune de ces questions.

Installation
************

Une méthode est proposée pour installer les programmes
nécessaires à l'écriture de scripts en  ``Python``.

Découverte de Python
*********************

Ici ``Python`` est introduit rapidement. Ses concepts
les plus abordables sont présentés, spécialement ceux
qui peuvent être utiles pour écrire un simple script.

Les librairies ``Numpy``, ``pandas`` et
``Matplotlib``, incontournables dans l'écosystème
scientifique de Python, sont aussi rapidement introduites.

Écriture et exécution d'un script
***********************************

Ici on présente comment s'y prendre pour écrire un script
en ``Python`` et comment l'exécuter. Cette dernière
tâche n'est pas aussi facile qu'exécuter un fichier
``.exe`` sur *Windows*, il faut donc savoir se l'approprier.

Exercices
**********

Des exercices d'application sont proposés afin d'utiliser
les outils présentés dans le tutoriel ainsi que les
concepts du langage et certaines de ses librairies:

1. Récupération d'informations dans un fichier et analyse,
2. Ajout de texte à un fichier PDF.
