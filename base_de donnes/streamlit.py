import streamlit as st
import joblib
import numpy as np
import pandas as pd 

model = joblib.load('Gradient Boosting_model.pkl')


# Streamlit app title
st.title("Prédiction de prix de l'immobilier")

# Input fields
surface_area = st.number_input('Surface de l\'appartement (m²)', min_value=0, step=1)
nb_rooms = st.number_input('Nombre de chambres', min_value=1, max_value=5, step=1)
cluster = st.number_input('Nombre de clusters', min_value=1, max_value=7, step=1)
balcon = st.number_input('Balcon (1: Oui, 0: Non)', min_value=0, max_value=1, step=1)
ascenseur = st.number_input('Ascenseur (1: Oui, 0: Non)', min_value=0, max_value=1, step=1)

if st.button('Faire la prédiction'):
    
    try:
        input_features = pd.DataFrame([[surface_area, nb_rooms, cluster, balcon, ascenseur]], 
                              columns=model.feature_names_in_)
        prediction = model.predict(input_features)
        
        # Display the result
        st.write(f"Le prix estimé de l'appartement est : {prediction[0]:,.2f} MAD")
    except Exception as e:
        st.error(f"Erreur lors de la prédiction : {e}")
