<h1 align="center">Modèles de Prédiction Météorologique</h1>

<p align="center">
    <img src="https://github.com/user-attachments/assets/c68f5b17-853a-44dd-8b2f-c6694d56d1cc" alt="Modèle de prédiction météorologique" style="max-width: 100%; height: auto;">
</p>

<h2>Introduction</h2>
<p>Ce code implémente des modèles d'apprentissage automatique pour prédire la pluie demain en se basant sur les données météorologiques. Les modèles utilisés sont la Régression Linéaire, les k-plus proches voisins (KNN), l'Arbre de Décision, la Régression Logistique et la Machine à Vecteurs de Support (SVM). Les performances des modèles et les courbes d'apprentissage sont également visualisées.</p>

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

<h3>Modèles et Évaluation :</h3>
<ul>
    <li><strong>Régression Linéaire :</strong> Entraînée et évaluée avec MAE, MSE et R2. Courbe d'apprentissage tracée.</li>
    <li><strong>k-plus Proches Voisins (KNN) :</strong> Évalué avec exactitude, indice Jaccard, F1-Score et Matrice de Confusion.</li>
    <li><strong>Arbre de Décision :</strong> Évalué avec exactitude, indice Jaccard, F1-Score et Matrice de Confusion.</li>
    <li><strong>Régression Logistique :</strong> Évaluée avec exactitude, indice Jaccard, F1-Score et Matrice de Confusion.</li>
    <li><strong>Machine à Vecteurs de Support (SVM) :</strong> Évaluée avec exactitude, indice Jaccard, F1-Score et Matrice de Confusion.</li>
</ul>

<h2>Output</h2>
<ul>
    <li>Tailles des ensembles d'entraînement et de test.</li>
    <li>Métriques pour chaque modèle.</li>
</ul>

<p align="center">
    <img src="https://github.com/zakariaeyahya/ML_Projects/assets/155691167/18d44ead-a93b-4d50-80ec-e37c57d821a8" alt="Résultats des modèles" style="max-width: 100%; height: auto;">
</p>

<h2>Conclusion</h2>
<p>Les performances des modèles et les courbes d'apprentissage fournissent des informations sur les capacités prédictives de chaque algorithme pour les données météorologiques fournies.</p>

<p>N'hésitez pas à personnaliser et étendre le code pour des analyses ou des expérimentations supplémentaires.</p>

<h2>Technologies Utilisées</h2>
<p align="center">
    <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" alt="Python">
    <img src="https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas">
    <img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy">
    <img src="https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="Scikit-learn">
    <img src="https://img.shields.io/badge/Matplotlib-11557c?style=for-the-badge&logo=matplotlib&logoColor=white" alt="Matplotlib">
</p>
## 📞 Contact

Pour plus d'informations, vous pouvez contacter  zakariae yahya : zakariae.yh@gmail.com.
