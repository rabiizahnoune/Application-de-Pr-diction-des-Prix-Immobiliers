# 🏠 Prédiction des Prix Immobiliers

## **Description du Projet**  
Ce projet consiste à développer une application interactive en **Streamlit** pour prédire les prix des biens immobiliers à partir de caractéristiques telles que la surface, le nombre de pièces, la présence d’un balcon, et d’autres facteurs.  

Le projet inclut également la gestion d'une base de données PostgreSQL hébergée dans un conteneur Docker pour stocker et analyser les données.  

---

## **Technologies Utilisées**  
- **Python**  
- **Streamlit** pour l'interface utilisateur  
- **Scikit-learn** pour la modélisation  
- **Pandas** pour l'analyse des données  
- **Docker** pour la conteneurisation  
- **PostgreSQL** comme système de gestion de base de données  

---

## **Étapes Principales du Projet**  

### 1. **Préparation des Données**  
- Normalisation des colonnes (`price`, `surface_area`, etc.) avec **MinMaxScaler**.  
- Division des données en ensembles d’entraînement (80%) et de test (20%).  

### 2. **Modélisation**  
- Plusieurs modèles de régression ont été testés, dont **Gradient Boosting**, **Random Forest**, et **KNN**.  
- Le modèle **Gradient Boosting** a été retenu comme le plus performant (MSE : 0.0061, R² : 0.7228).  

### 3. **Développement de l'Application**  
- **Streamlit** a été utilisé pour créer une interface interactive permettant d'entrer les caractéristiques des biens et d'afficher le prix prédit.  

### 4. **Base de Données avec Docker**  
- Un conteneur Docker a été configuré pour héberger une base de données **PostgreSQL**.  
- Les données sont extraites depuis cette base pour l’analyse et la prédiction.  

---

## **Fonctionnalités de l'Application**  
- Entrer des informations sur le bien immobilier :  
  - Surface (m²)  
  - Nombre de pièces  
  - Cluster (segmentation géographique)  
  - Présence d’un balcon et/ou d’un ascenseur  
- Prédiction du prix estimé en MAD.  
- Gestion des erreurs lors des prédictions.  

---

## **Installation et Déploiement**

### **Prérequis**  
- Docker installé sur votre machine.  
- Python 3.9 ou plus récent.  

### **Étapes d’Installation**   
   ```bash
   git clone https://github.com/rabiizahnoune/Application-de-Pr-diction-des-Prix-Immobiliers
   cd base_de donnes
   docker-compose up
   docker start immobilier_db-ml
   streamlit run streamlit.py
