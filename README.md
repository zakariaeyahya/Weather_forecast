# Projet Machine Learning avec Python
Bienvenue dans le référentiel des projets de machine learning ! Ce dépôt regroupe une série de projets que j'ai réalisés dans le cadre du cours "Machine Learning with Python" sur Coursera. Chaque projet met en lumière l'application pratique d'un modèle spécifique de machine learning.

# Objectif du Projet
L'objectif principal de ce projet est de partager mes expériences et compétences en matière de machine learning en mettant en avant des implémentations concrètes. Chaque dossier du projet représente une exploration détaillée d'un modèle particulier, illustrant son utilisation, son code source, et les résultats obtenus.

# Projets Inclus
Projet 1 - regression_lineaire :
Ce projet met en œuvre un modèle de régression linéaire pour prédire les émissions de CO2 en fonction de la taille du moteur, du nombre de cylindres et de la consommation de carburant. La régression linéaire est un choix naturel pour modéliser cette relation linéaire entre les variables d'entrée et la variable cible (émissions de CO2). Cette application pratique permet de comprendre comment les caractéristiques du moteur affectent les émissions de CO2, ce qui peut être crucial pour la conception de véhicules plus respectueux de l'environnement.
[Liens vers le dossier du projet pour plus de détails]
Projet 2 - [Knn] :
Ce script Python utilise le modèle des k plus proches voisins (k-NN) pour effectuer une classification sur un ensemble de données client. Les étapes comprennent le chargement des données, une brève analyse exploratoire, la préparation des données pour la classification, la gestion des valeurs aberrantes, l'entraînement du modèle k-NN, et l'évaluation de sa performance. L'objectif est de comprendre comment les caractéristiques des clients peuvent être utilisées pour prédire leur catégorie, ce qui peut être utile dans des scénarios tels que le ciblage marketing.
[Liens vers le dossier du projet pour plus de détails]
Projet 3 - [arbre de décision] :
Ce script Python met en œuvre un modèle d'arbre de décision pour la classification médicale basée sur des caractéristiques telles que l'âge, le sexe, la pression artérielle, le taux de cholestérol et le ratio sodium/potassium (Na_to_K). L'objectif est de prédire le médicament approprié pour un patient en fonction de ces caractéristiques. Les variables catégorielles sont encodées, et le modèle d'arbre de décision est entraîné avec un critère d'entropie et une profondeur maximale de 4. Le script évalue ensuite la précision du modèle sur un ensemble de test et visualise la structure de l'arbre de décision.
[Liens vers le dossier du projet pour plus de détails]
Projet 4 - [logistic_reg] :
Ce script Python met en œuvre un modèle de régression logistique pour la prédiction de la résiliation de services ('churn') en fonction de diverses caractéristiques telles que la durée de l'abonnement ('tenure'), l'âge, l'adresse, le revenu, le niveau d'éducation ('ed'), l'ancienneté dans l'emploi ('employ') et l'équipement ('equip'). Voici une brève description du modèle et de son application :

Le modèle de régression logistique est utilisé pour anticiper la résiliation de services (churn) en se basant sur des caractéristiques spécifiques des clients. Les étapes clés du script incluent le chargement des données, la normalisation des caractéristiques, la division des données en ensembles d'entraînement et de test, l'entraînement du modèle de régression logistique, et l'évaluation de la performance du modèle.

Le script génère des métriques telles que le score Jaccard, la matrice de confusion, le rapport de classification, et la perte logarithmique (log loss). Ces métriques offrent une évaluation approfondie de la capacité du modèle à prédire la résiliation de services. De plus, une matrice de confusion est graphiquement représentée pour une meilleure compréhension des performances du modèle en termes de faux positifs, faux négatifs, vrais positifs et vrais négatifs.
[Liens vers le dossier du projet pour plus de détails]
Projet 5- [Nom du modèle 3] :

Ce script Python met en œuvre un modèle de machine à vecteurs de support (SVM) pour la classification de cellules cancéreuses en fonction de caractéristiques telles que la taille des grappes, l'uniformité de la taille, la forme de l'uniformité, l'adhésion marginale, la taille des cellules épithéliales individuelles, la nudité des noyaux, la chromatine légèrement colorée, la nucléoléose normale et la mitose.

Le modèle de machine à vecteurs de support (SVM) est utilisé pour classifier les cellules cancéreuses en fonction de leurs caractéristiques. Le script charge les données, effectue une visualisation en nuage de points pour deux classes de cellules (bénignes et malignes), effectue une conversion des types de données, supprime les valeurs manquantes, et entraîne un modèle SVM avec un noyau radial de base (RBF). Ensuite, il évalue la performance du modèle en utilisant une matrice de confusion, un rapport de classification, et calcule les scores F1 et Jaccard.

Le script génère également une matrice de confusion graphique pour une représentation visuelle de la performance du modèle en termes de faux positifs, faux négatifs, vrais positifs et vrais négatifs. Les scores F1 et Jaccard complètent l'évaluation en fournissant des mesures de la précision du modèle.
[Liens vers le dossier du projet pour plus de détails]
Projet 6 - [Nom du modèle 3] :
Ce script Python met en œuvre plusieurs modèles d'apprentissage automatique (Régression Linéaire, k-Nearest Neighbors, Decision Tree, Logistic Regression et Support Vector Machine) pour la prédiction de la pluie le lendemain en se basant sur diverses caractéristiques météorologiques.

Le script commence par charger un ensemble de données météorologiques depuis une URL. Ensuite, il effectue un prétraitement des données, notamment la gestion des valeurs manquantes, la conversion des données catégorielles en variables indicatrices, et la transformation des valeurs binaires "Yes/No" en 0 et 1.

Il divise ensuite l'ensemble de données en ensembles d'entraînement et de test, puis entraîne différents modèles sur les données d'entraînement. Pour chaque modèle, il évalue les performances en utilisant des métriques telles que l'accuracy, l'index Jaccard, le F1-Score, et la matrice de confusion.

Le script inclut également une courbe d'apprentissage pour la Régression Linéaire, montrant comment l'erreur d'entraînement et de validation évolue en fonction de la taille de l'ensemble d'entraînement.

Enfin, les résultats de chaque modèle sont affichés, y compris les métriques d'évaluation et les matrices de confusion.
[Liens vers le dossier du projet pour plus de détails]

