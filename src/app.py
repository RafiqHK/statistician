import streamlit as st
import pandas as pd
from components.file_upload import upload_file
from components.pca_analysis import perform_pca
from components.pca_analysis import display_pca_results
from components.regression_analysis import perform_regression

def main():
    st.title("Excel Data Analysis Tool")

    # File upload
    uploaded_file = upload_file()
    if uploaded_file is not None:
        df = uploaded_file 
        
        st.subheader("Data Preview")
        st.dataframe(df.head())

        # PCA Analysis
        st.subheader("Principal Component Analysis")
        if st.button("Perform PCA"):
            pca_results, explained_variance = perform_pca(df)
            #st.plotly_chart(pca_results)
            display_pca_results(pca_results, explained_variance)
        # Linear Regression
        st.subheader("Linear Regression")
        dependent_var = st.selectbox("Select Dependent Variable", df.columns)
        independent_vars = st.multiselect("Select Independent Variables", df.columns)

        if st.button("Perform Linear Regression"):
            regression_results = perform_regression(df, dependent_var, independent_vars)
            st.write(regression_results)

if __name__ == "__main__":
    main()