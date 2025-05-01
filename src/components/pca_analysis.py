"""import streamlit as st
import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

def perform_pca(data):
    pca = PCA(n_components=2)
    components = pca.fit_transform(data.select_dtypes(include=['float64', 'int64']))
    explained_variance = pca.explained_variance_ratio_

    return components, explained_variance

def display_pca_results(components, explained_variance):
    fig, ax = plt.subplots()
    ax.scatter(components[:, 0], components[:, 1])
    ax.set_xlabel('Principal Component 1')
    ax.set_ylabel('Principal Component 2')
    ax.set_title(f'PCA - Explained Variance: {explained_variance}')
    st.pyplot(fig)

def pca_analysis(data):
    if st.button("Perform PCA"):
        components, explained_variance = perform_pca(data)
        display_pca_results(components, explained_variance)"""

import streamlit as st
import pandas as pd
from sklearn.decomposition import PCA
import plotly.express as px

def perform_pca(data):
    pca = PCA(n_components=2)
    components = pca.fit_transform(data.select_dtypes(include=['float64', 'int64']))
    explained_variance = pca.explained_variance_ratio_
    return components, explained_variance

def display_pca_results(components, explained_variance):
    df_pca = pd.DataFrame(components, columns=['PC1', 'PC2'])
    fig = px.scatter(
        df_pca,
        x='PC1',
        y='PC2',
        title=f'PCA - Explained Variance: PC1 {explained_variance[0]:.2f}, PC2 {explained_variance[1]:.2f}',
    )
    st.plotly_chart(fig)

def pca_analysis(data):
    if st.button("Perform PCA"):
        components, explained_variance = perform_pca(data)
        display_pca_results(components, explained_variance)
