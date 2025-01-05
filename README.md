# Générateur de flocon de Koch

Ce programme Python génère le célèbre Flocon de Koch, une figure fractale découverte par le mathématicien suédois Helge von Koch en 1904.

## Description

Le programme utilise le module `turtle` pour dessiner le flocon de Koch à différents niveaux de récursion. Il est composé de deux fonctions principales :

- `Kock(l, n)` : Génère une courbe de Koch avec :
    - `l` : la longueur du segment initial
    - `n` : le niveau de récursion

- `Flocon(l, n)` : Crée un flocon de Koch complet en combinant trois courbes de Koch avec :
    - `l` : la longueur de chaque côté
    - `n` : le niveau de récursion

## Fonctionnement

Le programme construit le flocon de Koch en utilisant un processus récursif :
1. Pour n=0, dessine un simple segment
2. Pour n>0, remplace chaque segment par quatre segments formant une pointe
3. Le processus est répété n fois

Le programme affiche automatiquement 5 flocons de complexité croissante (n=1 à n=5).

## Utilisation

Pour exécuter le programme :
```python
python3 "Flocon de Koch.py"
```