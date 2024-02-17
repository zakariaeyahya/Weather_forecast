# Modèles de Prédiction Météorologique

## Introduction
Ce code implémente des modèles d'apprentissage automatique pour prédire la pluie demain en se basant sur les données météorologiques. Les modèles utilisés sont la Régression Linéaire, les k-plus proches voisins (KNN), l'Arbre de Décision, la Régression Logistique et la Machine à Vecteurs de Support (SVM). Les performances des modèles et les courbes d'apprentissage sont également visualisées.

## Explication du Code
Importation des Bibliothèques :

pandas pour la manipulation des données.
scikit-learn pour les modèles et les métriques d'apprentissage automatique.
numpy pour les opérations numériques.
warnings pour ignorer les avertissements.
urllib.request pour le téléchargement des données.
matplotlib pour les graphiques.
Téléchargement et Chargement des Données :

Les données sont téléchargées à partir de l'URL fournie et chargées dans un DataFrame Pandas.
## Prétraitement :

Les données sont prétraitées, notamment avec l'encodage one-hot et le remplacement des valeurs catégorielles.
Les caractéristiques et la variable cible sont séparées.
Régression Linéaire :

Le modèle de régression linéaire est entraîné et évalué à l'aide de l'Erreur Absolue Moyenne, de l'Erreur Quadratique Moyenne et du Coefficient de Détermination R2.
La courbe d'apprentissage est tracée.
k-plus Proches Voisins (KNN) :

Le modèle KNN est entraîné et évalué en utilisant l'exactitude, l'indice Jaccard, le F1-Score et la Matrice de Confusion.
Arbre de Décision :

Le modèle d'arbre de décision est entraîné et évalué en utilisant l'exactitude, l'indice Jaccard, le F1-Score et la Matrice de Confusion.
Régression Logistique :

Le modèle de régression logistique est entraîné et évalué en utilisant l'exactitude, l'indice Jaccard, le F1-Score et la Matrice de Confusion.
Machine à Vecteurs de Support (SVM) :

Le modèle SVM est entraîné et évalué en utilisant l'exactitude, l'indice Jaccard, le F1-Score et la Matrice de Confusion.
## Output
Tailles des ensembles d'entraînement et de test.
Métriques pour le modèle de régression linéaire.
Métriques pour le modèle KNN.
Métriques pour le modèle d'arbre de décision.
Métriques pour le modèle de régression logistique.
Métriques pour le modèle SVM.
##Notes Importantes
Les figures sont affichées dans le panneau des graphiques par défaut. Pour les afficher également en ligne dans la console, décochez "Mute inline plotting" dans le menu des options des graphiques.
Exécution
Exécutez le code dans un environnement Python, en vous assurant que les bibliothèques requises sont installées. Des ajustements peuvent être nécessaires en fonction de votre environnement spécifique.

## Conclusion
Les performances des modèles et les courbes d'apprentissage fournissent des informations sur les capacités prédictives de chaque algorithme pour les données météorologiques fournies.

N'hésitez pas à personnaliser et étendre le code pour des analyses ou des expérimentations supplémentaires.
