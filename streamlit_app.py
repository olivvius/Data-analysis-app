from collections import namedtuple
import altair as alt
import math
import pandas as pd
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt

def main():
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.title("Exploratory Data analysis of data from a CSV file")

    # Ajout d'un sélecteur de fichiers CSV
    uploaded_file = st.file_uploader("Please choose a CSV file", type=["csv"])

    if uploaded_file is not None:
        # Chargement du fichier CSV dans un DataFrame pandas
        df = pd.read_csv(uploaded_file)
        
        # Affichage du nombre d'enregistrements
        num_records = len(df)
        st.write("Records number :", num_records)
        st.write()
        
        # Affichage du tableau issu de df.describe()
        st.write("General infos:")
        st.write(df.describe())
        st.write()

         # Affichage des 10 premiers lignes
        st.write("First lines:")
        st.write(df.head())
        st.write()   
        
        # Obtenir le nombre de valeurs nulles et non nulles par colonne
        null_counts = df.isnull().sum()
        non_null_counts = df.notnull().sum()

        # Créer un DataFrame à partir des séries null_counts et non_null_counts
        counts_df = pd.DataFrame({"Number of Null Values": null_counts, "Number of Non-Null Values": non_null_counts})

        # Afficher le tableau des nombres de valeurs nulles et non nulles
        st.write("Number of null and non-null values by columns")
        st.table(counts_df)

        
        # Affichage d'un histogramme pour chaque colonne
        st.write("Histograms :")
        for col in df.columns:
            try:
                plt.hist(df[col], bins=20)
                plt.title(col)
                st.pyplot()
                plt.clf()  # Nettoyer la figure après chaque itération
            except:
                print("error")
               # st.write("Cannot draw histogram for column {}".format(col)

        
         # Afficher la heatmap interactive avec Plotly
        st.write("Heatmap :")
        if not numeric_columns.empty:
            heatmap_df = df[numeric_columns]
            fig_heatmap = go.Figure(data=go.Heatmap(z=heatmap_df.corr(), x=heatmap_df.columns, y=heatmap_df.columns, colorscale="Viridis"))
            st.plotly_chart(fig_heatmap)
            else:
                st.write("Aucune colonne numérique disponible pour la heatmap.")

if __name__ == "__main__":
    main()
