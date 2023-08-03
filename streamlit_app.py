from collections import namedtuple
import altair as alt
import math
import pandas as pd
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt

def main():
    st.title("Application Streamlit pour l'analyse de données CSV")

    # Ajout d'un sélecteur de fichiers CSV
    uploaded_file = st.file_uploader("Choisissez un fichier CSV", type=["csv"])

    if uploaded_file is not None:
        # Chargement du fichier CSV dans un DataFrame pandas
        df = pd.read_csv(uploaded_file)
        
        # Affichage du nombre d'enregistrements
        num_records = len(df)
        st.write("Nombre d'enregistrements :", num_records)
        st.write()
        
        # Affichage du tableau issu de df.describe()
        st.write("Tableau panda issu de df.describe() :")
        st.write(df.describe())
        st.write()
        
        # Affichage du nombre de valeurs nulles et non nulles de chaque colonne
        null_counts = df.isnull().sum()
        non_null_counts = df.notnull().sum()
        st.write("Nombre de valeurs nulles par colonne :")
        st.write(null_counts)
        st.write()
        st.write("Nombre de valeurs non nulles par colonne :")
        st.write(non_null_counts)
        st.write()
        
        # Affichage d'un histogramme pour chaque colonne
        st.write("Histogrammes :")
        for col in df.columns:
            plt.hist(df[col], bins=20)
            plt.title(col)
            st.pyplot()
            plt.clf()  # Nettoyer la figure après chaque itération
        
        # Affichage de la heatmap avec seaborn
        st.write("Heatmap :")
        plt.figure(figsize=(10, 8))
        sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
        st.pyplot()

if __name__ == "__main__":
    main()
