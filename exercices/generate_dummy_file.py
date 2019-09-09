# -*- coding: utf-8 -*-
"""Script pour créer les données sources des exercices.

Les données que le script crée contiennent les caractéristiques de culverts.

Comme des données aléatoires sont créés, on utilise
random.seed() pour s'assurer qu'on obtient toujours
les mêmes sorties.

Historique:
- ML (10/09/2019): Création du script
"""
import random

# Nombre de branches créés dans le fichier de sortie
BR_COUNT = 50
# Nombre minimum de culverts par branche
NMIN_CULV_PER_BRANCH = 30
# Nombre maximum de culverts par branche
NMAX_CULV_PER_BRANCH = 100

random.seed(1)

nculv_per_branch = []
with open("culvert_logfile.txt", "w") as f:
    for br_idx in range(BR_COUNT):
        upstream_chainage = random.randint(5, 15)
        slope = random.random()
        upstream_invert = random.choice([200, 300, 400, 500])
        nculv_per_branch = random.randint(
            NMIN_CULV_PER_BRANCH,
            NMAX_CULV_PER_BRANCH
        )
        for culv_idx in range(nculv_per_branch):
            f.write(30 * "*" + "START CULVERT" + 30 * "*" + "\n")
            f.write(f"Culvert_branch = 'Branch_{br_idx + 1}'\n")
            f.write(f"Culvert_name = 'OH_{culv_idx + 1}'\n")
            culv_type = random.choices(
                ["concrete", "steel", "plastic"],
                weights=[10, 2, 5]
            )[0]
            diameter = random.choices(
                [0.3, 0.5, 0.8, 1, 1.5, 2],
                weights=[20, 15, 10, 5, 3, 1]
            )[0]
            length = random.triangular(2, 50, 10)
            manning = random.choice([0.033, 0.025, 0.02, 0.015])
            upstream_chainage += random.random() * 100
            upstream_invert -= random.random() * slope
            f.write(
                f"Culvert_params = {culv_type},{diameter},{length},{manning},{upstream_chainage},{upstream_invert}\n"
            )
            f.write(30 * "*" + "END CULVERT" + 30 * "*" + "\n")
