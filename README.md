# Projet Software Engineering - Compression et décompression par Bit Packing

## Description

Ce projet implémente différentes méthodes de compression de tableaux d’entiers basées sur la technique du bit packing.  
L’objectif est de réduire la taille des données transmises tout en permettant un accès direct rapide aux éléments compressés.

---

## Organisation du projet

- **src/** : Code source des classes de compression.  
- **scripts/** : Scripts d’usage (démonstration, visualisation).  
- **benchmarks/** : Mesures de performance et outils associés.  
- **tests/** : Tests unitaires.  
- **docs/** : Documentation et rapport PDF final.  
- **Makefile** : Automatisation des tâches (ex. `make run_demo`, `make run_gui` , `make test`).  
- **requirements.txt** : Dépendances Python.  

---

## Fonctionnalités principales

- Compression bit packing classique (split bits sur deux entiers de sortie).  
- Compression bit packing stricte (bits non scindés, chaque entier dans un bloc seul).  
- Gestion avancée de valeurs extrêmes via une zone overflow.  
- Support optionnel des nombres négatifs via un décalage automatique.  
- Programme de benchmarking pour mesurer les performances.  
- Script de démonstration facile à utiliser avec affichage des résultats et temps d’exécution.  
- Tests unitaires complets.

---

## Prérequis

- Python 3.8+.  
- Librairies Python suivantes (à installer via pip) :
  
  pip install -r requirements.txt


Le fichier `requirements.txt` contient :
matplotlib

---

## Technologies et environnement

Langage : Python 3.x
Interface graphique : Tkinter
Tests unitaires : unittest
Mesure des performances : time et scripts de benchmark dédiés
Organisation du projet : architecture modulaire avec répertoires src/, tests/, benchmarks/, scripts/, et docs/
Système d’exploitation recommandé : Windows (Linux supportés)
Outils de développement : éditeur de code (VS Code) et terminal avec Makefile

## Installation

Cloner le dépôt, puis installer les dépendances :
git clone 'https://github.com/kadridiaa/Software-engineer-project-2026---KADRI-Dia-eddine.git'
cd .\Software-engineer-project-2026---KADRI-Dia-eddine\

pip install -r requirements.txt (meme si il y a pas il marche)

---


### Exécuter la démonstration

Montre un exemple de compression/décompression avec mesures de temps :
  
  -avec une simple interface gui , en utilisant la commande : 
    make run_gui
    ou sur terminal :
    python -m scripts.run_gui
  
  - execution sans interface directement sur terminal : 
    make run_demo
    ou en utilisant la commande :
    python -m scripts.run_demo


### Lancer les tests unitaires

Pour vérifier que toutes les fonctionnalités fonctionnent :
-python -m unittest discover tests
 ou
-make test

---


## Rapport final

Le rapport docs/rapport.pdf présente le projet de compression et décompression de tableaux d’entiers par Bit-Packing. Il comprend :

Introduction : motivation du projet et contexte.
Algorithmes de compression : présentation des trois modes utilisés : Classic, Strict et Overflow.
Gestion des valeurs négatives : traitement et solutions appliquées pour chaque mode.
Architecture logicielle : structure des classes et organisation des fichiers du projet.
Protocole de benchmark : méthodologie et données de test utilisées pour mesurer les performances.
Analyse des performances : comparaison des trois modes selon taille compressée et temps de traitement.
Conclusion et perspectives : synthèse des résultats et suggestions d’améliorations futures.

---

## Conseils

- Utiliser le fichier `Makefile` pour lancer facilement les scripts et tests.  
  en exeutant les commandes : make 'nom de commande dans Makefile'
- Bien respecter la structure des packages pour éviter les erreurs d’import.





