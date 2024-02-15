#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn import preprocessing
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import svm
from sklearn.metrics import jaccard_score, f1_score, log_loss, confusion_matrix, accuracy_score,mean_absolute_error, mean_squared_error, r2_score
import sklearn.metrics as metrics
import warnings
warnings.filterwarnings("ignore")
import urllib.request
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import learning_curve


# In[5]:


url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ML0101EN-SkillUp/labs/ML-FinalAssignment/Weather_Data.csv' 
df = pd.read_csv(url)


# In[6]:


df.head()


# In[7]:


# Prétraitement des données pour le modèle
df_sydney_processed = pd.get_dummies(data=df, columns=['RainToday', 'WindGustDir', 'WindDir9am', 'WindDir3pm'])
df_sydney_processed.replace(['No', 'Yes'], [0,1], inplace=True)
df_sydney_processed.drop('Date', axis=1, inplace=True)
df_sydney_processed = df_sydney_processed.astype(float)


# In[8]:


features = df_sydney_processed.drop(columns='RainTomorrow', axis=1)


# In[9]:


Y = df_sydney_processed['RainTomorrow']
X_train, X_test, y_train, y_test = train_test_split(features, Y, test_size=0.2, random_state=10)


# In[10]:


print("Taille de l'ensemble d'entraînement (X_train, y_train):", X_train.shape, y_train.shape)
print("Taille de l'ensemble de test (X_test, y_test):", X_test.shape, y_test.shape)


# In[11]:


LinearReg = LinearRegression()
LinearReg.fit(X_train, y_train)
y_pred = LinearReg.predict(X_test)


# In[12]:


# Calcule l'erreur absolue moyenne (Mean Absolute Error)
mae = mean_absolute_error(y_test, y_pred)
# Calcule l'erreur quadratique moyenne (Mean Squared Error)
mse = mean_squared_error(y_test, y_pred)
# Calcule le coefficient de détermination (R2 Score)
r2 = r2_score(y_test, y_pred)


# In[13]:


# Créer un DataFrame pour afficher les résultats
results_df = pd.DataFrame({
    'Metric': ['Mean Absolute Error (MAE)', 'Mean Squared Error (MSE)', 'R2 Score'],
    'Value': [mae, mse, r2]
})
print("Linear Model Metrics:")
print(results_df)


# In[14]:


# Calcule la courbe d'apprentissage
train_sizes, train_scores, test_scores = learning_curve(LinearReg, X_train, y_train, cv=5, scoring='neg_mean_squared_error')
# Calcule la moyenne des scores pour chaque taille d'ensemble d'entraînement
train_scores_mean = -train_scores.mean(axis=1)
test_scores_mean = -test_scores.mean(axis=1)


# In[15]:


import matplotlib.pyplot as plt
# Tracez la courbe d'apprentissage
plt.figure(figsize=(8, 6))
plt.title("Courbe d'apprentissage pour la régression linéaire")
plt.plot(train_sizes, train_scores_mean, 'o-', label='Erreur d\'entraînement (MSE)')
plt.plot(train_sizes, test_scores_mean, 'o-', label='Erreur de validation (MSE)')
plt.xlabel("Taille de l'ensemble d'entraînement")
plt.ylabel("Moyenne des erreurs quadratiques moyennes (MSE)")
plt.legend(loc="best")
plt.show()


# In[16]:


from sklearn.neighbors import KNeighborsClassifier
# Création d'une instance du modèle KNN avec n_neighbors fixé à 4
knn_model = KNeighborsClassifier(n_neighbors=4)
# Entraîner le modèle KNN sur les données d'entraînement
X_train_np = X_train.values
X_test_np = X_test.values
knn_model = KNeighborsClassifier(n_neighbors=4)
knn_model.fit(X_train_np, y_train)
predictions_knn = knn_model.predict(X_test_np)


# In[17]:


# Calcule de l'accuracy
accuracy_knn = accuracy_score(y_test, predictions_knn)
print("Accuracy (KNN):", accuracy_knn)
# Calcule de l'index Jaccard
jaccard_knn = jaccard_score(y_test, predictions_knn)
print("Jaccard Index (KNN):", jaccard_knn)
# Calcule du F1-Score
f1_knn = f1_score(y_test, predictions_knn)
print("F1-Score (KNN):", f1_knn)


# In[18]:


# Calcule de la matrice de confusion
conf_matrix_knn = confusion_matrix(y_test, predictions_knn)
print("Confusion Matrix (KNN):")
print(conf_matrix_knn)


# In[19]:


# Créer une instance du modèle Decision Tree
tree_model = DecisionTreeClassifier()
# Entraîner le modèle sur l'ensemble d'entraînement
tree_model.fit(X_train, y_train)
# Prédictions sur l'ensemble de test
predictions_tree = tree_model.predict(X_test)


# In[20]:


# Calcule l'accuracy
accuracy_tree = accuracy_score(y_test, predictions_tree)
print("Accuracy (Decision Tree):", accuracy_tree)
# Calcule l'index Jaccard
jaccard_tree = jaccard_score(y_test, predictions_tree)
print("Jaccard Index (Decision Tree):", jaccard_tree)
# Calcule le F1-Score
f1_tree = f1_score(y_test, predictions_tree)
print("F1-Score (Decision Tree):", f1_tree)


# In[21]:


# Calcule la matrice de confusion
conf_matrix_tree = confusion_matrix(y_test, predictions_tree)
print("Confusion Matrix (Decision Tree):")
print(conf_matrix_tree)


# In[22]:


# Logistic regression
from sklearn.linear_model import LogisticRegression
# Séparer les données pour la régression logistique
X_train_lr, X_test_lr, y_train_lr, y_test_lr = train_test_split(features, Y, test_size=0.2, random_state=1)
# Afficher la taille des ensembles d'entraînement et de test
print("Taille de l'ensemble d'entraînement (X_train, y_train):", X_train_lr.shape, y_train_lr.shape)
print("Taille de l'ensemble de test (X_test, y_test):", X_test_lr.shape, y_test_lr.shape)


# In[23]:


# Création d'une instance du modèle de régression logistique
LR = LogisticRegression(solver='liblinear')
# Entraîner le modèle sur l'ensemble d'entraînement
LR.fit(X_train_lr, y_train_lr)
# Prédictions sur l'ensemble de test
predictions_LR = LR.predict(X_test_lr)


# In[25]:


# Calcul de l'accuracy
accuracy_LR = accuracy_score(y_test_lr, predictions_LR)
print("Accuracy (Logistic Regression):", accuracy_LR)
# Calcul de l'index Jaccard
jaccard_LR = jaccard_score(y_test_lr, predictions_LR)
print("Jaccard Index (Logistic Regression):", jaccard_LR)
# Calcul du F1-Score
f1_LR = f1_score(y_test_lr, predictions_LR)
print("F1-Score (Logistic Regression):", f1_LR)


# In[26]:


# Calcul de la matrice de confusion
conf_matrix_LR = confusion_matrix(y_test_lr, predictions_LR)
print("Confusion Matrix (Logistic Regression):")
print(conf_matrix_LR)


# In[27]:


from sklearn import svm
SVM = svm.SVC()
SVM.fit(X_train, y_train)
predictions_svm = SVM.predict(X_test)


# In[28]:


accuracy_svm = accuracy_score(y_test, predictions_svm)
print("Accuracy (SVM):", accuracy_svm)
jaccard_svm = jaccard_score(y_test, predictions_svm)
print("Jaccard Index (SVM):", jaccard_svm)
f1_svm = f1_score(y_test, predictions_svm)
print("F1-Score (SVM):", f1_svm)
conf_matrix_svm = confusion_matrix(y_test, predictions_svm)


# In[29]:


print("Confusion Matrix (SVM):")
print(conf_matrix_svm)


# In[ ]:




