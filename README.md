# Projet Machine Learning avec Python
Bienvenue dans le référentiel des projets de machine learning !Le projets que j'ai réalisés dans le cadre du cours "Machine Learning with Python" sur Coursera. Chaque projet met en lumière l'application pratique des modèles spécifique de machine learning.

# Objectif du Projet
L'objectif principal de ce projet est de partager mes expériences et compétences en matière de machine learning en mettant en avant des implémentations concrètes.  Dossier du projet représente une exploration détaillée d'un modèle particulier, illustrant son utilisation, son code source, et les résultats obtenus.

# Projets 

Ce script Python met en œuvre plusieurs modèles d'apprentissage automatique (Régression Linéaire, k-Nearest Neighbors, Decision Tree, Logistic Regression et Support Vector Machine) pour la prédiction de la pluie le lendemain en se basant sur diverses caractéristiques météorologiques.

Le script commence par charger un ensemble de données météorologiques depuis une URL. Ensuite, il effectue un prétraitement des données, notamment la gestion des valeurs manquantes, la conversion des données catégorielles en variables indicatrices, et la transformation des valeurs binaires "Yes/No" en 0 et 1.

Il divise ensuite l'ensemble de données en ensembles d'entraînement et de test, puis entraîne différents modèles sur les données d'entraînement. Pour chaque modèle, il évalue les performances en utilisant des métriques telles que l'accuracy, l'index Jaccard, le F1-Score, et la matrice de confusion.

Le script inclut également une courbe d'apprentissage pour la Régression Linéaire, montrant comment l'erreur d'entraînement et de validation évolue en fonction de la taille de l'ensemble d'entraînement.

Enfin, les résultats de chaque modèle sont affichés, y compris les métriques d'évaluation et les matrices de confusion.
