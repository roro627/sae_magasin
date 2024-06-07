# SAE Magasin

## Description

**SAE Magasin** est une application de gestion de magasin développée en Python avec PyQt6. Ce projet vise à simplifier les courses en supermarché en permettant de simplifié et optimisé la recherche de produits dans un magasin à l'aide d'un chemin optimisé. Il est constitué de deux principales applications :

1. **Gestion du Plan du Magasin** : Permet de choisir les produits présent dans le magasin et de les positionnés sur un plan de magasin.
2. **Optimisation du Chemin** : Permet de créer une liste de course et de génèrer un chemin pour collecter les produits.

## Table des matières

- [Prérequis](#prérequis)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Fonctionnalités](#fonctionnalités)
  - [Gestion du Plan du Magasin](#gestion-du-Plan-du-Magasin)
  - [Optimisation du Chemin](#optimisation-du-Chemin)
- [Contributeurs](#contributeurs)

## Prérequis

Avant de démarrer, assurez-vous d'avoir les éléments suivants :

- **Python 3.8+** : Installez Python depuis [python.org](https://www.python.org/downloads/).
- **PyQt6** : Installez PyQt6 en utilisant pip.

```bash
pip install PyQt6
```

## Installation

1. Clonez le dépôt du projet :

    ```bash
    git clone https://github.com/roro627/sae_magasin
    ```

2. Accédez au répertoire du projet :

    ```bash
    cd sae_magasin
    ```

3. Installez les dépendances nécessaires [indiqué plus haut](#prérequis) 

## Utilisation

### Lancement de l'application 1

Pour lancer la première application, exécutez le fichier `.\application_1\SoftwareController.py` :

```bash
python .\application_1\SoftwareController.py
```

### Lancement de l'application 2

Pour lancer la deuxième application, exécutez le fichier `.\application_2\ClientSoftwareController.py` :

```bash
python .\application_2\ClientSoftwareController.py
```

### Gestion du Plan du Magasin

Cette application sécurisé permet de :
- Définir les informations du projet (nom, auteur, date, etc.).
- Ouvrir un projet existant.
- Créer un quadrillage ajustable sur le plan.
- Sélectionner les produits vendus par le magasin.
- Associer chaque produit à une position spécifique dans le magasin.
- Enregistrer le projet avec toutes les données associées.
- Supprimer un projet.

### Optimisation du Chemin

Cette application permet de :
- Choisir un magasin.
- Voir la position des produits sur le plan.
- Établir une liste de courses.
- Afficher le chemin le plus efficace pour prendre tous les produits de la liste de courses.

## Fonctionnalités

### Gestion du Plan du Magasin

- **Création d'un Projet** :
  - Définir les détails du projet.
  - Charger un plan du magasin.
  - Créer un quadrillage sur le plan.
  - Sélectionner et positionner les produits.

- **Enregistrement et Gestion** :
  - Enregistrer les projets.
  - Ouvrir et supprimer des projets.

- **Sécurité de l'application** :
  - Accès via nom d'utilisateur et mot de passe à l'application.

### Optimisation du Chemin

- **Affichage des Produits** :
  - Sélectionner un magasin.
  - Affichage d'un carré rouge à la postion du produit survollé.

- **Liste de Courses** :
  - Établir une liste de courses.
  - Afficher le chemin optimal sur le plan.

## Contributeurs

Ce projet a été réalisé par :

- **Lambert Romain**
- **Cocquerel Alexis**
- **Siame Romain**
