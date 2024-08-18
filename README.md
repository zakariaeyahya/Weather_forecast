<h1 align="center">Modèles de Prédiction Météorologique</h1>

<p align="center">
    <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" alt="Python">
    <img src="https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas">
    <img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy">
    <img src="https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="Scikit-learn">
    <img src="https://img.shields.io/badge/Matplotlib-11557c?style=for-the-badge&logo=matplotlib&logoColor=white" alt="Matplotlib">
</p>

<h2>Introduction</h2>
<p>Ce code implémente des modèles d'apprentissage automatique pour prédire la pluie demain en se basant sur les données météorologiques. Les modèles utilisés sont la Régression Linéaire, les k-plus proches voisins (KNN), l'Arbre de Décision, la Régression Logistique et la Machine à Vecteurs de Support (SVM). Les performances des modèles et les courbes d'apprentissage sont également visualisées.</p>

<img src="https://github.com/user-attachments/assets/c68f5b17-853a-44dd-8b2f-c6694d56d1cc" alt="Modèle de prédiction météorologique" style="max-width: 100%; height: auto;">

<h2>Explication du Code</h2>
<h3>Importation des Bibliothèques :</h3>
<ul>
    <li>pandas pour la manipulation des données.</li>
    <li>scikit-learn pour les modèles et les métriques d'apprentissage automatique.</li>
    <li>numpy pour les opérations numériques.</li>
    <li>warnings pour ignorer les avertissements.</li>
    <li>urllib.request pour le téléchargement des données.</li>
    <li>matplotlib pour les graphiques.</li>
</ul>

<h3>Téléchargement et Chargement des Données :</h3>
<p>Les données sont téléchargées à partir de l'URL fournie et chargées dans un DataFrame Pandas.</p>

<h2>Prétraitement :</h2>
<ul>
    <li>Les données sont prétraitées, notamment avec l'encodage one-hot et le remplacement des valeurs catégorielles.</li>
    <li>Les caractéristiques et la variable cible sont séparées.</li>
</ul>

<h3>Régression Linéaire :</h3>
<p>Le modèle de régression linéaire est entraîné et évalué à l'aide de l'Erreur Absolue Moyenne, de l'Erreur Quadratique Moyenne et du Coefficient de Détermination R2. La courbe d'apprentissage est tracée.</p>

<h3>k-plus Proches Voisins (KNN) :</h3>
<p>Le modèle KNN est entraîné et évalué en utilisant l'exactitude, l'indice Jaccard, le F1-Score et la Matrice de Confusion.</p>

<h3>Arbre de Décision :</h3>
<p>Le modèle d'arbre de décision est entraîné et évalué en utilisant l'exactitude, l'indice Jaccard, le F1-Score et la Matrice de Confusion.</p>

<h3>Régression Logistique :</h3>
<p>Le modèle de régression logistique est entraîné et évalué en utilisant l'exactitude, l'indice Jaccard, le F1-Score et la Matrice de Confusion.</p>

<h3>Machine à Vecteurs de Support (SVM) :</h3>
<p>Le modèle SVM est entraîné et évalué en utilisant l'exactitude, l'indice Jaccard, le F1-Score et la Matrice de Confusion.</p>

<h2>Output</h2>
<ul>
    <li>Tailles des ensembles d'entraînement et de test.</li>
    <li>Métriques pour le modèle de régression linéaire.</li>
    <li>Métriques pour le modèle KNN.</li>
    <li>Métriques pour le modèle d'arbre de décision.</li>
    <li>Métriques pour le modèle de régression logistique.</li>
    <li>Métriques pour le modèle SVM.</li>
</ul>

<img src="https://github.com/zakariaeyahya/ML_Projects/assets/155691167/18d44ead-a93b-4d50-80ec-e37c57d821a8" alt="Résultats des modèles" style="max-width: 100%; height: auto;">

<h2>Conclusion</h2>
<p>Les performances des modèles et les courbes d'apprentissage fournissent des informations sur les capacités prédictives de chaque algorithme pour les données météorologiques fournies.</p>

<p>N'hésitez pas à personnaliser et étendre le code pour des analyses ou des expérimentations supplémentaires.</p>

<style>
    body {
        font-family: Arial, sans-serif;
        line-height: 1.6;
        color: #333;
        max-width: 800px;
        margin: 0 auto;
        padding: 20px;
    }
    h1, h2, h3 {
        color: #2c3e50;
    }
    img {
        display: block;
        margin: 20px auto;
        max-width: 100%;
        height: auto;
    }
    ul {
        padding-left: 20px;
    }
    p {
        margin-bottom: 15px;
    }
</style>
